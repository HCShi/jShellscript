#!/usr/bin/python3
# coding: utf-8
from keras.preprocessing import sequence
##################################################################
## pad_sequence(); 默认填充 0
tmp = np.array([[1, 2, 3], [4, 5, 6], [7]]); print(tmp.shape)  # (3,); 因为每行的长度不同
print(sequence.pad_sequences(tmp, maxlen=10))  # 默认是向前填充
# [[0 0 0 0 0 0 0 1 2 3]
#  [0 0 0 0 0 0 0 4 5 6]
#  [0 0 0 0 0 0 0 0 0 7]]
print(sequence.pad_sequences(tmp, maxlen=10, padding='post'))  # 向后填充
# [[1 2 3 0 0 0 0 0 0 0]
#  [4 5 6 0 0 0 0 0 0 0]
#  [7 0 0 0 0 0 0 0 0 0]]
print(sequence.pad_sequences(tmp, maxlen=2))  # 长的从头剪断
# [[2 3]
#  [5 6]
#  [0 7]]
print(sequence.pad_sequences(tmp, maxlen=2, padding='post'))  # 长的从尾剪断
# [[2 3]
#  [5 6]
#  [7 0]]
