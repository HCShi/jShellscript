部分参考自:[复杂网络分析库NetworkX学习笔记](http://blog.sciencenet.cn/blog-404069-337$2.html)
### draw 样式
NetworkX提供了一系列样式参数，可以用来修饰和美化图形，达到我们想要的效果。常用的参数包括：
      - `node_size`:  指定节点的尺寸大小(默认是300，单位未知，就是上图中那么大的点)<br>
      - `node_color`:  指定节点的颜色 (默认是红色，可以用字符串简单标识颜色，例如'r'为红色，'b'为绿色等，具体可查看手册)<br>
      - `node_shape`:  节点的形状（默认是圆形，用字符串'o'标识，具体可查看手册）<br>
      - `alpha`: 透明度 (默认是1.0，不透明，0为完全透明) <br>
      - `width`: 边的宽度 (默认为1.0)<br>
      - `edge_color`: 边的颜色(默认为黑色)<br>
      - `style`: 边的样式(默认为实现，可选： solid|dashed|dotted,dashdot)<br>
      - `with_labels`: 节点是否带标签（默认为True）<br>
      - `font_size`: 节点标签字体大小 (默认为12)<br>
      - `font_color`: 节点标签字体颜色（默认为黑色）<br>
灵活运用上述参数，可以绘制不同样式的网络图形，例如：nx.draw(G,node_size = 30,with_labels = False) 是绘制节点尺寸为30、不带标签的网络图。

### draw 布局
NetworkX在绘制网络图形方面提供了布局的功能，可以指定节点排列的形式。这些布局包括：

* circular_layout：节点在一个圆环上均匀分布
* random_layout：节点随机分布
* shell_layout：节点在同心圆上分布
* spring_layout： 用Fruchterman-Reingold算法排列节点（这个算法我不了解，样子类似多中心放射状）
* spectral_layout：根据图的拉普拉斯特征向量排列节点？我也不是太明白

布局用pos参数指定，例如：nx.draw(G,pos = nx.circular_layout(G))。
在上一篇笔记中，四个不同的模型分别是用四种布局绘制的，可以到那里去看一下效果，此处就不再重复写代码了。

另外，也可以单独为图中的每个节点指定一个位置（x、y坐标），不过比较复杂，我还没有这样做过。感兴趣的朋友可以看一下NetworkX文档中的一个例子
