### Description
主要参考自官方文档
l1_download-dataset.py 数据获取
l2 - l20 文档集探索
l21 - 一些工具的探索
### 术语
Token (词例): 对输入文本做任何实际处理前, 都需要将其分割成诸如词、标点符号、数字或纯字母数字(alphanumerics) 等语言单元(linguistic units), 这些单元被称为词例。
句子: 由有序的词例序列组成

Tokenization (词例还原): 将句子还原成所组成的词例; 以分割型语言(segmented languages)英语为例, 空格的存在使词例还原变得相对容易同时也索然无味
    然而, 对于汉语和阿拉伯语, 因为没有清晰的边界, 这项工作就稍显困难, 另外, 在某些非分割型语言(non-segmented languages) 中,
    几乎所有的字符(characters)都能以单字(one-character) 存在, 但同样也可以组合在一起形成多字(multi-characterwords)形式

语料库: 通常是由丰富句子组成的海量文本

Part-of-speech(POS) Tag (词性标签): 任一单词都能被归入到至少一类词汇集(set of lexical)或词性条目(part-of-speech categories)中,
    例如: 名词、动词、形容词和冠词等; 词性标签用符号来代表一种词汇条目—— NN(名词)、 VB(动词)、 JJ(形容词)和 AT(冠词)

Parse Tree(剖析树): 利用形式语法(formal grammar)的定义, 可以用树状图来表示给定句子的句法(syntactic)结构

### 下面让我们了解 NLP 常见的任务:
POS Tagging (词性标注): 给定一个句子和组词性标签, 常见的语言处理就是对句子中的每个词进行标注;
    举个例子, The ball is red, 词性标注后将变成 The/AT ball/NN is/VB red/JJ
    最先进的词性标注器准确率高达 96%; 文本的词性标注对于更复杂的 NLP 问题,
    例如我们后面会讨论到的句法分析(parsing) 和机器翻译(machine translation) 非常必要

Computational Morphology (计算形态学): 大量建立在 "语素"(morphemes/stems) 基础上的词组成了自然语言, 语素虽然是最小的语言单元, 却富含意义
    计算形态学所关心的是用计算机发掘和分析词的内部结构

Parsing (句法分析): 在语法分析的问题中, 句法分析器(parser) 将给定句子构造成剖析树; 为了分析语法, 某些分析器假定一系列语法规则存在,
    但目前的解析器已经足够机智地借助复杂的统计模型[1]直接推断分析树
    多数分析器能够在监督式设置 (supervised setting) 下操作并且句子已经被词性标注过了; 统计句法分析是自然语言处理中非常活跃的研究领域

Machine Translation(MT) (机器翻译): 机器翻译的目的是让计算机在没有人工干预的情况下, 将给定某种语言的文本流畅地翻译成另一种语言文本;
    这是自然语言处理中最艰巨的任务之一, 这些年来已经用许多不同的方式解决; 几乎所有的机器翻译方法都依赖了词性标注和句法分析作为预处理

### NLTK 语料库
NLTK 囊括数个在 NLP 研究圈里广泛使用的实用语料库; 我们来看看三个下文会用到的语料库
Brown Corpus (布朗语料库): Brown Corpus of Standard American English 被认为是第一个可以在计算语言学处理中使用的通用英语语料库
    它包含了一百万字 1961 年出版的美语文本; 它代表了通用英语的样本, 采样自小说, 新闻和宗教文本; 随后, 在大量的人工标注后, 诞生了词性标注过的版本

Gutenberg Corpus (古登堡语料库): 古登堡语料库从最大的在线免费电子书平台 古登堡计划(Gutenberg Project) 中选择了 14 个文本,
    整个语料库包含了一百七十万字。

Stopwords Corpus: 除了常规的文本文字, 另一类诸如介词, 补语, 限定词等含有重要的语法功能, 自身却没有什么含义的词被称为停用词(stop words);
    NLTK 所收集的停用词语料库(Stopwords Corpus)包含了来自 11 种不同语言(包括英语)的 2400 个停用词
