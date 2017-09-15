### Description
参考自:

莫烦 Python: 大致的听一遍, 虽然讲的不是特别的详细..., 但是比一般的视频教程都好
[莫烦 Python github.io](https://morvanzhou.github.io/tutorials/machine-learning/sklearn/)
[源码地址 Github](https://github.com/MorvanZhou/tutorials/tree/master/sklearnTUT)
l1 - l8

入门推荐: [实验楼 -> Python科学计算(二) -> 3、scikit-learn 机器学习 - 实验楼]
l41 - l44 都是参考的上面的链接..., 很适合学习

[实验楼 -> scikit-learn 实战之监督学习 -> 2、广义线性模型用于分类和回归预测]
./l51_广义线性模型用于回归预测_linear-model-diabetes.py
./l52_广义线性模型用于分类预测_Perceptron-classification.py

[实验楼 -> scikit-learn 实战之监督学习 -> 3、支持向量机用于分类和回归预测]     # 这个需要仔细参考
./l53_支持向量机进行线性分类_svm-linear-perceptron.py
./data.csv  # 将数据分成了两部分
./l54_支持向量机进行非线性分类_digits-svm.py
./l55_支持向量机进行回归预测_boston_price.py

[实验楼 -> scikit-learn 实战之监督学习 -> 4、常见的监督学习模型对比评价]
./l56_常见监督学习模型对比_classification-comparison.py
./data_circles.csv  # make_* 命令生成的数据
./data_moons.csv  # make_* 命令生成的数据
./class_data.csv  # 这三个数据文件都是 l51 使用的

[实验楼 -> scikit-learn 实战之非监督学习 -> 1、K-Means 聚类算法]
./l57_KMeans-聚类算法初探_cluster.py
./cluster_data.csv

[实验楼 -> scikit-learn 实战之非监督学习 -> 2、K 值选择与聚类评估]
./l58_K值选择与聚类评估_肘部法则_轮廓系数cluster_evaluate_inertia_silhouette.py
./cluster_data.csv

[实验楼 -> scikit-learn 实战之非监督学习 -> 3、聚类算法对比与选择]
./l59_聚类算法对比与选择.py
./data_blobs.csv

[实验楼 -> scikit-learn 实战之非监督学习 -> 4、主成分分析（PCA 降维）]
./l60_主成分分析_PCA-降维.py
./l61_主成分分析_PCA-KMeans-处理-digits.py

### 机器学习简介
监督学习被用于解决分类和回归问题, 而非监督学习主要是用于解决聚类问题;
聚类, 顾名思义就是将具有相似属性或特征的数据聚合在一起;
聚类算法有很多, 最简单和最常用的就算是 K-Means 算法了

scikit-learn 中的聚类算法都包含在 sklearn.cluster 方法

.fit() 是 scikit-learn 训练模型的通用方法, 但是该方法本身返回的是模型的参数; 所以, 通常我们会使用 PCA.fit_transform() 方法直接返回降维后的数据结果
