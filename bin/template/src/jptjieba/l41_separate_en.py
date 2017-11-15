#!/usr/bin/python3
# coding: utf-8
"""Uses dynamic programming to infer the location of spaces in a string without spaces."""
# Reference: https://stackoverflow.com/questions/8870261/how-to-split-text-without-spaces-into-list-of-words
# Rife https://github.com/keredson/wordninja/blob/master/wordninja.py
# A naive algorithm won't give good results when applied to real-world data.
# Here is a 20-line algorithm that exploits relative word frequency to give accurate results for real-word text.
# (If you want an answer to your original question which does not use word frequency,
#     you need to refine what exactly is meant by "longest word": is it better to have a 20-letter word and ten 3-letter words,
#     or is it better to have five 10-letter words? Once you settle on a precise definition, you just have to change the line defining
#     wordcost to reflect the intended meaning.)

# The idea
# The best way to proceed is to model the distribution of the output. A good first approximation is to assume all words are
#     independently distributed. Then you only need to know the relative frequency of all words. It is reasonable to assume that they
#     follow Zipf's law, that is the word with rank n in the list of words has probability roughly 1/(n log N)
#     where N is the number of words in the dictionary.
# Once you have fixed the model, you can use dynamic programming to infer the position of the spaces. The most likely sentence is
#     the one that maximizes the product of the probability of each individual word, and it's easy to compute it with dynamic programming.
# Instead of directly using the probability we use a cost defined as the logarithm of the inverse of the probability to avoid overflows.
from math import log
words = open("/home/coder352/dataset/125k-words-sorted-by-frequency.txt").read().split()  # Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
wordcost = dict((k, log((i+1)*log(len(words)))) for i, k in enumerate(words))  # cost 越小用的越多
# print(sorted([word for word in words if len(word) == 1]))  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
maxword = max(len(x) for x in words);
# print(maxword)  # 58, Wikipedia show that it is the second longest name
def split(s):  # s is a long str without spaces
    # Find the best match for the i first characters, assuming cost has been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))  # candidates 是 cost list 的带序号字典
        return min((c[0] + wordcost.get(s.lower()[i-k-1:i], 9e999), k+1) for k, c in candidates)  # k:[0,i)
        # reversed 很重要, 表示 cost[i-1-k] 对 s[:i] 来说, 后面多添加了 k+1 长度的 str, 动态规划的思想...

    # Build the cost array. 核心就是动态规划思想...
    cost = [(0, 0)]  # cost[i] 表示在 str[0:i] 的最小 cost, 和从上一个 最小的 cost 到这个 cost 添加的那部分字符串的长度
    for i in range(1, len(s)+1):  # 根据 s 的长度来暴力求出各个长度 str 的 cost, 没有在词典中的 str cost 无穷大
        c, k = best_match(i)  # 对每一个长度的 s[0:i] 都计算一个 cost
        cost.append((c, k))

    out = []
    l = len(s)
    while l > 0:
        out.append(s[l - cost[l][1]:l])  # 这里 cost 长度比 s 多 1, 所以可以这样写
        l = l - cost[l][1]
    return list(reversed(out))
if __name__ == '__main__':
    print(split("sheisABOY"))
    print(split('thumbgreenappleactiveassignmentweeklymetaphor'))
    print(split('thereismassesoftextinformationofpeoplescommentswhichisparsedfromhtmlbuttherearenodelimitedcharactersinthemforexamplethumbgreenappleactiveassignmentweeklymetaphorapparentlytherearethumbgreenappleetcinthestringialsohavealargedictionarytoquerywhetherthewordisreasonablesowhatsthefastestwayofextractionthxalot'))
##################################################################
## Optimization
# The implementation consumes a linear amount of time and memory, so it is reasonably efficient.
#     If you need further speedups, you can build a suffix tree from the word list to reduce the size of the set of candidates.
# If you need to process a very large consecutive string it would be reasonable to split the string to avoid excessive memory usage.
#     For example you could process the text in blocks of 10000 characters plus a margin of 1000 characters on either side to
#     avoid boundary effects. This will keep memory usage to a minimum and will have almost certainly no effect on the quality.
