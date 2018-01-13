#!/usr/bin/python3
# coding: utf-8
import numpy as np
A = np.eye(3); print(A)
u, s, v = np.linalg.svd(A); print(u, s, v)
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]

# [ 1.  1.  1.]

# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]

a = np.array([[1, 1], [0, 1], [1, 0]]); print(a)
u, s, v = np.linalg.svd(A); print(u, s, v)
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]

# [ 1.  1.  1.]

# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]
