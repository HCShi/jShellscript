#!/usr/bin/python3
# coding: utf-8
# 参考: [国外大牛](https://machinelearningmastery.com/predict-sentiment-movie-reviews-using-deep-learning/)
# Accuracy was achieved above 97% with winners achieving 99%.
import numpy as np
from keras.datasets import imdb
from keras.preprocessing import sequence
import matplotlib.pyplot as plt
##################################################################
## 加载数据; 详细介绍见 jptkeras
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=5000)  # only interested in the first 5,000 most used words in the dataset.
print(X_train.shape, X_test.shape)  # (25000,) (25000,)
# The layer takes arguments that define the mapping including the maximum number of expected words also called the vocabulary size
# Therefore our vocabulary size will be 5,000. We can choose to use a 32-dimension vector to represent each word.
# Finally, we may choose to cap the maximum review length at 500 words, truncating reviews longer than that
#     and padding reviews shorter than that with 0 values.
# We would then use the Keras utility to truncate or pad the dataset to a length of 500 for each observation using the sequence.pad_sequences()
X_train = sequence.pad_sequences(X_train, maxlen=500)  # 将 X_train 的每一项变成 500 长, 截断 或 padding
X_test = sequence.pad_sequences(X_test, maxlen=500)
print(X_train.shape, X_test.shape)  # (25000, 500) (25000, 500); 一旦长度统一了, 第二维就出来了
# Finally, later on, the first layer of our model would be an word embedding layer created using the Embedding class as follows:
# Embedding(5000, 32, input_length=500)
# The output of this first layer would be a matrix with the size 32×500 for a given review training or test pattern in integer format.
# Now that we know how to load the IMDB dataset in Keras and how to use a word embedding representation for it
##################################################################
## 上面代码只是分析数据, 下面开始尝试各种模型; develop and evaluate some models; 代码完全重新开始
##################################################################
## (一) Simple Multi-Layer Perceptron Model for the IMDB Dataset
## MLP(多层感知机) for the IMDB problem
##################################################################
# We can start off by developing a simple multi-layer perceptron model with a single hidden layer.
# The word embedding representation is a true innovation and we will demonstrate what would have been considered world class
#     results in 2011 with a relatively simple neural network.
# Let’s start off by importing the classes and functions required for this model and
#     initializing the random number generator to a constant value to ensure we can easily reproduce the results.
import numpy
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
numpy.random.seed(7)  # fix random seed for reproducibility
##################################################################
## 加载数据
# Next we will load the IMDB dataset. We will simplify the dataset as discussed during the section on word embeddings.
# Only the top 5,000 words will be loaded.
# We will also use a 50%/50% split of the dataset into training and test. This is a good standard split methodology.
top_words, max_words = 5000, 500
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=top_words)  # load the dataset but only keep the top n words, zero the rest
# We will bound reviews at 500 words, truncating longer reviews and zero-padding shorter reviews.
X_train = sequence.pad_sequences(X_train, maxlen=max_words)
X_test = sequence.pad_sequences(X_test, maxlen=max_words)
##################################################################
## create the model
# Now we can create our model. We will use an Embedding layer as the input layer, setting the vocabulary to 5,000,
#     the word vector size to 32 dimensions and the input_length to 500. The output of this first layer will be a 32×500 sized matrix
# We will flatten the Embedded layers output to one dimension, then use one dense hidden layer of 250 units with a rectifier activation function.
#     The output layer has one neuron and will use a sigmoid activation to output values of 0 and 1 as predictions.
# The model uses logarithmic loss and is optimized using the efficient ADAM optimization procedure.
model = Sequential()
model.add(Embedding(top_words, 32, input_length=max_words))
model.add(Flatten())
model.add(Dense(250, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())  # 查看各层的状态
##################################################################
## Fit the model
# We can fit the model and use the test set as validation while training.
#     This model overfits very quickly so we will use very few training epochs, in this case just 2.
# There is a lot of data so we will use a batch size of 128. After the model is trained, we evaluate its accuracy on the test dataset.
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=2, batch_size=128, verbose=2)
scores = model.evaluate(X_test, y_test, verbose=0)  # Final evaluation of the model
print("Accuracy: %.2f%%" % (scores[1]*100))
# Train on 25000 samples, validate on 25000 samples
# Epoch 1/2
# 39s - loss: 0.5160 - acc: 0.7040 - val_loss: 0.2982 - val_acc: 0.8716
# Epoch 2/2
# 37s - loss: 0.1897 - acc: 0.9266 - val_loss: 0.3143 - val_acc: 0.8694
# Accuracy: 86.94%

# Running this example fits the model and summarizes the estimated performance. We can see that this very simple model
#     achieves a score of nearly 86.94% which is in the neighborhood of the original paper, with very little effort.
# I’m sure we can do better if we trained this network, perhaps using a larger embedding and adding more hidden layers.
##################################################################
## (二) One-Dimensional Convolutional Neural Network Model for the IMDB Dataset
## CNN for the IMDB problem
##################################################################
# Convolutional neural networks were designed to honor the spatial structure in image data whilst
#     being robust to the position and orientation of learned objects in the scene.
# This same principle can be used on sequences, such as the one-dimensional sequence of words in a movie review.
#     The same properties that make the CNN model attractive for learning to recognize objects in images
#     can help to learn structure in paragraphs of words, namely the techniques invariance to the specific position of features.
# Keras supports one-dimensional convolutions and pooling by the Conv1D and MaxPooling1D classes respectively.
# Again, let’s import the classes and functions needed for this example and initialize our random number generator
#     to a constant value so that we can easily reproduce results.
import numpy
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
numpy.random.seed(7)  # fix random seed for reproducibility
##################################################################
## load dataset
# We can also load and prepare our IMDB dataset as we did before; load the dataset but only keep the top n words, zero the rest
top_words, max_words = 5000, 500
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=top_words)
# pad dataset to a maximum review length in words
X_train = sequence.pad_sequences(X_train, maxlen=max_words)
X_test = sequence.pad_sequences(X_test, maxlen=max_words)
##################################################################
## build model
# We can now define our convolutional neural network model. This time, after the Embedding input layer,
#     we insert a Conv1D layer. This convolutional layer has 32 feature maps and reads embedded word
#     representations 3 vector elements of the word embedding at a time.
# The convolutional layer is followed by a 1D max pooling layer with a length and stride of 2 that halves the size of the feature maps from the convolutional layer. The rest of the network is the same as the neural network above.
model = Sequential()
model.add(Embedding(top_words, 32, input_length=max_words))
model.add(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(250, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
# Fit the model; We also fit the network the same as before.
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=2, batch_size=128, verbose=2)
scores = model.evaluate(X_test, y_test, verbose=0)  # Final evaluation of the model
print("Accuracy: %.2f%%" % (scores[1]*100))
# Train on 25000 samples, validate on 25000 samples
# Epoch 1/2
# 38s - loss: 0.4451 - acc: 0.7640 - val_loss: 0.3107 - val_acc: 0.8660
# Epoch 2/2
# 39s - loss: 0.2373 - acc: 0.9064 - val_loss: 0.2909 - val_acc: 0.8779
# Accuracy: 87.79%

# Running the example, we are first presented with a summary of the network structure. We can see our convolutional layer
#     preserves the dimensionality of our Embedding input layer of 32-dimensional input with a maximum of 500 words.
#     The pooling layer compresses this representation by halving it.
# Running the example offers a small but welcome improvement over the neural network model above with an accuracy of nearly 87.79%.
# Again, there is a lot of opportunity for further optimization, such as the use of deeper and/or larger convolutional layers.
#     One interesting idea is to set the max pooling layer to use an input length of 500. This would compress each feature
#     map to a single 32 length vector and may boost performance.
##################################################################
## Summary
# In this post, you discovered the IMDB sentiment analysis dataset for natural language processing.
# You learned how to develop deep learning models for sentiment analysis including:
#     How to load and review the IMDB dataset within Keras.
#     How to develop a large neural network model for sentiment analysis.
#     How to develop a one-dimensional convolutional neural network model for sentiment analysis.
