#!/usr/bin/python3
# coding: utf-8
# [Kaggle 官方 Tutorial](https://www.kaggle.com/c/word2vec-nlp-tutorial#part-1-for-beginners-bag-of-words)
# 参考自: https://github.com/ziyanfeng/kaggle-bag-of-words-meets-bags-of-popcorn/blob/master/notebook.ipynb
# 这里只是第一个: Part 1 For Beginners Bag Of Words; 剩下的在后面整理
import os
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
# This notebook was created following the tutorial from Kaggle. In this notebook, we will clean and construct bag-of-words on
#     IMDB review texts and use a classifier to predict the semtiment labels of the review.
##################################################################
## Load Labeled Training Data
# For Bag-of-words approach, we're going to use labeled training data for supervised learning.
train = pd.read_csv('./tmp_dataset/Kaggle-Bag-of-Words-Meets-Bags-of-Popcorn/labeledTrainData.tsv', header=0, delimiter="\t", quoting=3)
print(type(train))  # <class 'pandas.core.frame.DataFrame'>
# Here, header=0 indicates the first line of the tsv file contains the column names, delimiter="\t" means the file uses tap as delimiter,
#     and quoting=3 tells Python to ignore double quotes.
print(train.shape)  # (25000, 3). There are 25000 samples and 3 variables in the training data.
print(train.head())  # 输出前 5 个
print(train.review[0])  # 第一条评论长度, 发现有 html 标签
##################################################################
## Data Cleaning and Text Preprocessing
# Removing HTML Markup with The BeautifulSoup Package
train['review_bs'] = train['review'].apply(lambda x: BeautifulSoup(x, 'html.parser'))
print(train.review_bs[0].get_text())  # 去掉了 html 标签
# Dealing with Punctuation, Numbers and Stopwords: NLTK and regular expressions
# Use re package to remove digits and punctuations. To build a simplified Bag-of-words model, we remove both digits and punctuations.
train['review_letters_only'] = train['review_bs'].apply(lambda x: re.sub(r'[^a-zA-Z]', ' ', x.get_text()))
print(train['review_letters_only'][0])  # The reviews are now strings of letters only.
# Convert words into lower case and tonkenize, i.e. split the text into individual words.
train['review_words'] = train['review_letters_only'].apply(lambda x: x.lower().split())
print(train['review_words'][0])  # The reviews are now list of word strings.
# Remove stop words with ntlk.
set_of_stopwords = set(stopwords.words("english"))  # 这个不能写到下面的 for 里面, 否则太慢了, python 居然没有优化...
train['review_meaningful_words'] = train['review_words'].apply(lambda x: [w for w in x if not w in set_of_stopwords])
print(len(train['review_words'][0]) - len(train['review_meaningful_words'][0]))  # 218; For the first review entry
# We can also stem the words with PorterStemmer() and Lemmatizer() to consider only word stems.
# But for this training data, better results was produced without stemming. 所以下面这部分注释掉了
# porter_stemmer = PorterStemmer()
# wordnet_lemmatizer = WordNetLemmatizer()
# train['review_stemmed'] = train['review_meaningful_words'].apply(lambda x: [porter_stemmer.stem(w) for w in x])
# train['review_stemmed'] = train['review_cleaned'].apply(lambda x: [wordnet_lemmatizer.lemmatize(w) for w in x])
# As the final step, we join the list of words into a single string.
# train['review_cleaned'] = train['review_stemmed'].apply(lambda x: ' '.join(x))  # uncomment if using stemming
train['review_cleaned'] = train['review_meaningful_words'].apply(lambda x: ' '.join(x))  # comment if using stemming
# Add revies_cleaned as a new column to the training data. 删掉中间过程, 只保留最终结果, pandas...
train.drop(['review', 'review_bs', 'review_letters_only', 'review_words', 'review_meaningful_words'], axis=1, inplace=True)
print(train.head())
print(train['review_cleaned'][0])
##################################################################
## 上面 Pandas 使用的简直逆天
##################################################################
## Now the training data is ready for using Bag of Words.
# Creating Features from a Bag of Words (Using scikit-learn)
# Initialize the CountVectorizer object, which is scikit-learn's bag of words tool. CountVectorizer converts a collection of text documents
#     to a matrix of token counts.
vectorizer = CountVectorizer(analyzer="word", preprocessor=None, tokenizer=None, stop_words=None, max_features=5000)  # 除了 max_features 其他的都是默认值
# analyzer="word" indicates the feature we are using are words;
# preprocessor=None, tokenizer=None and stop_words=None mean the data needes no more
#     preprocessing, tokenization and removing stop sords since we've already done these in the Data Cleaning and Text Processing step;
# max_features=5000 means we only take the top 5000 frequent words as our words in the bag
#     thus limiting the size of the feature vector and speeding up the modeling process.
train_data_features = vectorizer.fit_transform(list(train['review_cleaned'].values))
# fit_transform() method does two functions: First, it fits the model and learns the vocabulary; second, it transforms our training data
#     into feature vectors. The input to fit_transform should be a list of strings.
# Numpy arrays are easy to work with, so convert the result to an array
train_data_features = train_data_features.toarray()  # default is sparse Matrix, so we transform it to array
# The resulting train_data_features is a array which contains the occurrence of bag of words in our training data. Take a look at the first row.
print(train_data_features[0])  # array([0, 0, 0, ..., 0, 0, 0], dtype=int64)
# The train_data_feature should be an array with 25000 rows and 5000 columns. Let's check it out,
print(train_data_features.shape)  # The dimension of train_data_features is (25000, 5000).
# With get_feature_names() method, we can take a look at the bag of words which is a list of 5000 words.
vocab = vectorizer.get_feature_names()
print(len(vocab))  # 5000
##################################################################
## Modularizing the Cleaning Process; 下面才是进入正题
def clean_reviews(reviews, remove_stopwords=False, stem=False):
    """
    to clean review strings
    review: a list of review strings
    remove_stopwords: whether to remove stop words
    stem: whether to use stem
    output: a list of clean reviews
    """
    reviews_text = list(map(lambda x: BeautifulSoup(x, 'html.parser').get_text(), reviews))  # 1. Remove HTML
    reviews_text = list(map(lambda x: re.sub("[^a-zA-Z]"," ", x), reviews_text))             # 2. Remove non-letters
    words = list(map(lambda x: x.lower().split(), reviews_text))                             # 3. Convert words to lower case and split them
    if remove_stopwords:                                                                     # 4. Optionally remove stop words (false by default)
        set_of_stopwords = set(stopwords.words("english"))
        meaningful_words = list(map(lambda x: [w for w in x if not w in set_of_stopwords], words))
    if stem:                                                                                 # 5. Optionally stem the words
        porter_stemmer = PorterStemmer()
        wordnet_lemmatizer = WordNetLemmatizer()
        stemmed_words = list(map(lambda x: [porter_stemmer.stem(w) for w in x], meaningful_words))
        stemmed_words = list(map(lambda x:[wordnet_lemmatizer.lemmatize(w) for w in x], stemmed_words))
        # 6. Join the words to a single string
        clean_review = map(lambda x: ' '.join(x), stemmed_words)
    else:
        clean_review = list(map(lambda x: ' '.join(x), meaningful_words))
    return clean_review
##################################################################
## Load and Clean Test Data
test = pd.read_csv('./tmp_dataset/Kaggle-Bag-of-Words-Meets-Bags-of-Popcorn/testData.tsv', header=0, delimiter='\t', quoting=3)  # Read the test data
print(test.shape)  # (25000, 2); Verify that there are 25,000 rows and 2 columns
# Get a bag of words for the test set, and convert to a numpy array
clean_test_reviews = clean_reviews(list(test['review'].values), remove_stopwords=True)
test_data_features = vectorizer.transform(clean_test_reviews)
test_data_features = test_data_features.toarray()
##################################################################
## Random Forest; Spend 7 mins
# Let's try a random forest with the features we just created.
rf_clf = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=0)  # Initialize a Random Forest classifier with 100 trees
# Use cross validation to evaluate the performance of Random Forest
rf_clf_error = 1 - cross_val_score(rf_clf, train_data_features, train['sentiment'], cv=5, scoring='accuracy', n_jobs=-1).mean()
print(rf_clf_error)  # Random Forest training error: 0.1573
##################################################################
## XGBoost; 比上面的还要慢好多
# Let's try a XGBoost with the features we created.
dtrain = xgb.DMatrix(train_data_features, label=train['sentiment'])  # Create xgb trianing set and parameters
params = {'silent': 1, 'nthread': -1, 'eval_metric': 'error'}
print('The cross validation may take a while...')  # Use cross validation to evaluate the performance of XGBoost
xgb_cv_results = xgb.cv(params, dtrain, num_boost_round=100, nfold=5, show_stdv=False, seed=0)  # 好慢啊, 忍不住 kill 了
xgb_error = xgb_cv_results['test-error-mean'].mean()
print(xgb_error)  # XGBoost trianing error: 0.1829
# It seems that Random Forest out-performed XGBoost. Thus we'll create a submission file with Random Forest.
##################################################################
## Creating a Submission of Random Forest; 经过上面在 test 上面的对比, 最终采用 Random Forest
# Fit the forest to the training set, using the bag of words as features and the sentiment labels as labels
rf_clf.fit(train_data_features, train['sentiment'])  # This may take a few minutes to run, 比上面的 XGBoost 快多了
# Use the random forest to make sentiment label predictions
result = rf_clf.predict(test_data_features); print(result)
# Copy the results to a pandas dataframe with an "id" column an a "sentiment" column
output = pd.DataFrame(data={"id":test["id"], "sentiment":result})
##################################################################
## 保存结果, 提交到比赛页面
# Use pandas to write the comma-separated output file
output.to_csv("tmp-Bag_of_Words_rf_clf_results.csv", index=False, quoting=3)
# This Bag_of_words with Random Forest model produced a score of 0.84628 without stemming and 0.84476 with stemming.
