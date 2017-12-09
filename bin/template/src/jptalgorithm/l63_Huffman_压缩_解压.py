#!/usr/bin/python3
# coding: utf-8
# 卜东波老师算法课 第三次作业编程
# 参考: [Python 实现 Huffman 编码压缩和解压缩文件](http://www.jianshu.com/p/4cbbfed4160b)
# 算法上面讲的很详细, 但是代码很不 Python!, 写 Huffman 为什么不用 heapq 呢!
# 这个实现了树, 结构很好, 版本二中参考的 [Huffman Coding - Python Implementation](http://bhrigu.me/blog/2017/01/17/huffman-coding-python-implementation/)
##################################################################
## 版本一: 没有用 Tree
import heapq
from bitarray import bitarray
from collections import Counter
def encode(frequency):
    # 最后并没有建立一棵 Huffman 树, 所以不方便维护, 但是一般只是得到频率就够了...
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]  # 按原来顺序生成 list
    # print(heap)  # [[1, ['T', '']], [4, ['h', '']], [7, ['e', '']], [13, [' ', '']], [5, ['f', '']], ...]
    heapq.heapify(heap)  # 按照 item[0] 实现一个最小堆
    # print(heap)  # [[1, ['T', '']], [1, ['b', '']], [1, ['d', '']], [1, ['c', '']], [4, ['h', '']], ...]
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]: pair[1] = '0' + pair[1]  # 因为下面用了 [lo[0] + hi[0]] + lo[1:] + hi[1:], 所以后面可能有多个
        for pair in hi[1:]: pair[1] = '1' + pair[1]  # 这种每次遍历都要把所有的节点修改一次编码, 很慢, 但想想只有 200 个节点, 呵呵..., 还建什么树啊
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))  # 先按长度排, 再按字典序排
##################################################################
## 上面是核心算法, 下面是对文件实现压缩
# 计算频率 和 字典, 压缩率
frequency = Counter(open('./TSP_Data').read()); print(frequency.items())  # dict_items([('5', 116), ('3', 114), ('.', 200), ...])
dictionary = dict([(item[0], bitarray(item[1])) for item in encode(frequency)]); print(dictionary)  # {' ': bitarray('111'), '.': bitarray('010'), ...}
for key, value in dictionary.items(): print(key.ljust(10) + str(frequency[key]).ljust(10) + value.to01())
compress_rate = sum([len(value.to01()) * frequency[key] for key, value in dictionary.items()]) / (8. * len(open('./TSP_Data').read())); print(compress_rate)
# 实现原始编码和解码
a = bitarray()
a.encode(dictionary, open('./TSP_Data').read())
encode_text = a.to01(); print(encode_text)  # 实现了编码
print(''.join(bitarray(encode_text).decode(dictionary)))  # 实现了解码
# 在前面进行填充, 先补全 0 至长度为 8 的倍数(pad_encode_text), 然后将补充 0 的个数记录在最前面(ultra_text)
pad_length = 8 - len(encode_text) % 8
pad_encode_text = ''.join(['0' for _ in range(pad_length)]) + encode_text; print(pad_encode_text)
padded_info = "{0:08b}".format(pad_length); print(padded_info)  # 将 padding_length 转换为二进制, 长度不足 8 的补零; 第一个 byte 确定前面补了多少 0
ultra_text = padded_info + pad_encode_text  # 很高明的方法
open('tmp.bin', 'w').write(''.join(chr(int(ultra_text[i*8:i*8+8], 2)) for i in range(len(ultra_text)//8)))
# 解码 ultra_text
ultra_text = ''.join([bin(ord(byte))[2:].zfill(8) for byte in open('./tmp.bin').read()])  # jptstring/l*_format*.py 中介绍了很多种方法
padded_info = ultra_text[:8]; print(padded_info)  # 读一个 byte, 判断填充 0 的个数
pad_encode_text = ultra_text[8:]; print(pad_encode_text)
encoded_text = ultra_text[8:][:-1 * int(padded_info, 2)]; print(encode_text)
print(''.join(bitarray(encode_text).decode(dictionary)))  # 实现了解码

##################################################################
## 版本二: 构造了一棵树, 并使用软件工程学方法
import heapq
import os
class HeapNode:
	def __init__(self, char, freq):
		self.char, self.freq = char, freq
		self.left, self.right = None, None
	def __cmp__(self, other):  # 为最小堆排序准备的...
		if(other == None): return -1
		if(not isinstance(other, HeapNode)): return -1
		return self.freq > other.freq
class HuffmanCoding:
	def __init__(self, path):
		self.path = path
		self.heap = []  # 存放一个 HeapNode 最小堆, 排序会按照 __cmp__
		self.codes = {}  # 存放编码表
		self.reverse_mapping = {}  # 反向查询编码表, 感觉真啰嗦...
##################################################################
## functions for compression:
	def make_heap(self, frequency):
		for key in frequency:
			node = HeapNode(key, frequency[key])
			heapq.heappush(self.heap, node)  # 按照 HeapNode 的 __cmp__ 排序
	def merge_nodes(self):
		while(len(self.heap) > 1):  # 将 heap 整合成一个 tree, 见上面的核心算法
			node1 = heapq.heappop(self.heap)
			node2 = heapq.heappop(self.heap)
			merged = HeapNode(None, node1.freq + node2.freq)
			merged.left = node1
			merged.right = node2
			heapq.heappush(self.heap, merged)  # 树的节点都放到了 Heap 中, 方便排序
	def make_codes_helper(self, root, current_code):
		if(root == None): return
		if(root.char != None):  # 是叶子节点的时候 char 非空
			self.codes[root.char] = current_code
			self.reverse_mapping[current_code] = root.char  # 顺便构建反向查询的编码表
			return
		self.make_codes_helper(root.left, current_code + "0")
		self.make_codes_helper(root.right, current_code + "1")
	def make_codes(self):  # 遍历树, 生成编码表
		root = heapq.heappop(self.heap)  # 在这里用完 heapq 就没用了, 拿出来 root 就永远为空了...
		current_code = ""
		self.make_codes_helper(root, current_code)
## 上面 4 个函数构建编码表..., 也就相当于 版本一中的 encode(), 写的好啰嗦; 下面是对文件实现压缩
	def pad_encoded_text(self, encoded_text):  # 8 的整数倍长度才能写入文件
		extra_padding = 8 - len(encoded_text) % 8
		for i in range(extra_padding): encoded_text += "0"
		padded_info = "{0:08b}".format(extra_padding)  # 将 extra_padding 转换为二进制, 长度不足 8 的补零; 第一个 byte 确定前面补了多少 0
		encoded_text = padded_info + encoded_text  # 很高明的方法
		return encoded_text
	def get_byte_array(self, padded_encoded_text):
		if(len(padded_encoded_text) % 8 != 0):
			print("Encoded text not padded properly")
			exit(0)
		b = bytearray()
		for i in range(0, len(padded_encoded_text), 8):
			byte = padded_encoded_text[i:i+8]
			b.append(int(byte, 2))  # 2 进制转换为 10 进制
		return b
	def compress(self):
		filename, file_extension = os.path.splitext(self.path)
		output_path = filename + ".bin"
		with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
			text = file.read().rstrip()
            frequency = Counter(text);
			self.make_heap(frequency)
			self.merge_nodes()
			self.make_codes()
            encoded_text = "".join([self.codes[character] for character in text])  # 编码压缩和解压缩文件
			padded_encoded_text = self.pad_encoded_text(encoded_text)  # 填充开头, 并标记填充的个数
			b = self.get_byte_array(padded_encoded_text)  # 转化为 byte, 因为最后写文件一定要用 byte
			output.write(bytes(b))
		print("Compressed")
		return output_path
##################################################################
## functions for decompression:
	def remove_padding(self, padded_encoded_text):
		padded_info = padded_encoded_text[:8]  # # 读一个 byte, 判断填充 0 的个数
		padded_encoded_text = padded_encoded_text[8:]
		encoded_text = padded_encoded_text[:-1 * int(padded_info, 2)]
		return encoded_text
	def decode_text(self, encoded_text):
		current_code = ""
		decoded_text = ""
		for bit in encoded_text:
			current_code += bit
			if(current_code in self.reverse_mapping):
				character = self.reverse_mapping[current_code]
				decoded_text += character
				current_code = ""
		return decoded_text
	def decompress(self, input_path):
		filename, file_extension = os.path.splitext(self.path)
		output_path = filename + "_decompressed" + ".txt"
		with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = ''.join([bin(ord(byte))[2:].zfill(8) for byte in file.read()])  # jptstring/l*_format*.py 中介绍了很多种方法
			encoded_text = self.remove_padding(bit_string)
			decompressed_text = self.decode_text(encoded_text)
			output.write(decompressed_text)
		print("Decompressed")
		return output_path
# After we have converted the text into some series of bits, we need to store it as a binary file. Bytes are stored in the binary file. So we will take up 8 bits at a time and convert them into bytes and store them in file (line 96-97).
# But what if the number of bits in our encoded text were not a multiple of 8? Some bits would be left out during conversion to bytes. So we pad our encoded text with some '0's to make it multiple of 8 (lines 80-82).
# Now, during decompression we need to know how many padded bits were added, so we remove it before decoding our encoded text. Thus, how many padded bits were added, this extra info is stored in the beginning of our encoded text using 8 bits (line 84-85).
# Thus during decompression, we read padding info -> remove padded bits -> then start our decompression by reading on further bits.

path = "/home/ubuntu/Downloads/sample.txt"
h = HuffmanCoding(path)
output_path = h.compress()
h.decompress(output_path)
