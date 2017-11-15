### 本地数据处理流程 raw_str -> tokens -> text
1. 读文件
``` zsh
raw = open(file).read()  # <class 'str'>; 以 单个字符 为单位; open(file) 默认是以 .readlines(), 所以要加上 .read()
```
2. 将 整个文件的 'str' 词条化, 包括 punctuation
``` zsh
tokens = nltk.word_tokenize(raw)  # <class 'list'>
# nltk.corpus.names.words('male.txt') 就是 list 类型的, 可以直接 nltk.Text()
# 常用方法:
#     tokens.count(word)
```
3. 转为 Text() 对象
``` zsh
text = nltk.Text(tokens)  # <class 'nltk.text.Text'>
# nltk.book.text1 默认就是 <class 'nltk.text.Text'>
# 常用方法:
#     text.collocations(num=20) 双词搭配
#     text.concordance(word) 查询单词
#     text.similar(word) 用来识别文章中和搜索词相似的词语, 可以用在搜索引擎中的相关度识别功能中
#     text.common_contexts(words) 列出用法相似词语前后的词语, 所比较的词语用 "_" 表示; 这里 words 是 list 类型
#     text.dispersion_plot(words) 查看词语在一篇语料中的位置分布
```
### 常见 nltk 类型
1. nltk.corpus
``` zsh
# nltk.corpus.gutenberg / brown /stopwords 等常见的语料库都是
# 常用方法: 介绍见 gutenberg
#     fileids()        # 所有文件的 id, 字符串形式, 表示文件名
#     raw(filename)    # 字符方式读入
#     words(filename)  # tokens 方式读入, 和 wc filename 有误差
#     sents(filename)  # 句子方式读入, 每个句子是 list

#     abspaths()         # 所有文件了路径列表
#     abspath(filename)  # 指定文件路径
```
2. nltk.corpus.reader.tagged
``` zsh
# nltk.corpus.brown 等带标签的, ConditionalFreqDist() 就是专门为这些语料库准备的
# 常用方法: 介绍见 brown
#     categories()  # 标签类别
#     fileids(categories='barley')  # 在有 categories() 的类里面, fileids(), sents() 等都可以加参数
#     sents(categories=['news', 'editorial', 'reviews'])  # raw(), words(), sents() 方法有更多的参数
#     tagged_paras()
#     tagged_sents()
#     tagged_words()
```
3. nltk.corpus.reader.plaintext.CategorizedPlaintextCorpusReader
``` zsh
# nltk.corpus.reuters
# 常用方法: 介绍见 reuters
#     categories()  # 标签类别
```
4. nltk.corpus.reader.nps_chat
``` zsh
# nltk.corpus.nps_chat
# 常用方法:
#     posts()
#     categories()  # 标签类别
```
### 不同子模块类型
``` python
# 直接在 from nltk.corpus import gutenberg; 后查看类型是不行的, 要调用 fileids() 等方法后才会检测到具体类型
nltk.corpus.gutenberg                                 # <class 'nltk.corpus.reader.plaintext.PlaintextCorpusReader'>
nltk.corpus.gutenberg.words()                         # <class 'nltk.corpus.reader.util.ConcatenatedCorpusView'>
nltk.corpus.gutenberg.words('austen-persuasion.txt')  # <class 'nltk.corpus.reader.util.StreamBackedCorpusView'>
nltk.corpus.webtext  # <class 'nltk.corpus.reader.plaintext.PlaintextCorpusReader'>
nltk.corpus.inaugural  # <class 'nltk.corpus.reader.plaintext.PlaintextCorpusReader'>
nltk.corpus.reuters  # <class 'nltk.corpus.reader.plaintext.CategorizedPlaintextCorpusReader'>

nltk.corpus.brown                # <class 'nltk.corpus.reader.tagged.CategorizedTaggedCorpusReader'>
nltk.corpus.brown.words()        # <class 'nltk.corpus.reader.util.ConcatenatedCorpusView'>
nltk.corpus.brown.words('ca01')  # <class 'nltk.corpus.reader.tagged.TaggedCorpusView'>

nltk.corpus.nps_chat  # <class 'nltk.corpus.reader.nps_chat.NPSChatCorpusReader'>

nltk.corpus.stopwords  # <class 'nltk.corpus.reader.wordlist.WordListCorpusReader'>
nltk.corpus.words  # <class 'nltk.corpus.reader.wordlist.WordListCorpusReader'>

nltk.corpus.names.words('male.txt')  # <class 'list'>;
nltk.book.text1  # <class 'nltk.text.Text'>
```
