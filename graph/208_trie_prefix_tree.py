"""
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
 

示例：

输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
 

提示：

1 <= word.length, prefix.length <= 2000
word 和 prefix 仅由小写英文字母组成
insert、search 和 startsWith 调用次数 总计 不超过 3 * 104 次

"""
# dict + 暴力检索 （空间占用低，但是时间复杂度高）
class Trie:
    def __init__(self):
        self.word_pool = dict()

    def insert(self, word: str) -> None:
        self.word_pool[word] = len(word)

    def search(self, word: str) -> bool:
        if word in self.word_pool:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        for word in self.word_pool:
            if len(prefix) > self.word_pool[word]:
                continue # 超过原单词长度，直接下一个
            else: # 可以利用dfs去把这个题目转换成79.单词搜索
                # for i, ch in enumerate(word):
                    if word[0] == prefix[0]:
                        if self.dfs(0, 0, prefix, word) == True:
                            return True

        return False

    def dfs(self, ind, k, prefix, word):
        if word[ind] != prefix[k]:
            return False 

        else:# 二者相等
            if ind == len(word)-1 and k != len(prefix)-1:
                # word到头但是prefix还没有到头
                return False
            elif k == len(prefix)-1:
                # k到头
                return True

        # 两个都没到头，下一轮
        return self.dfs(ind+1, k+1, prefix, word)


# 正常前缀树
class TrieNode:
    def __init__(self):
        # key: char, value: TrieNode
        self.children = {} 
        # 标记是否是单词结尾（比如 'apple' 里的 'e' 是 True，中间的 'p' 是 False）
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # 如果当前字符不在子节点中，创建一个新节点
            if char not in node.children:
                node.children[char] = TrieNode()
            # 移动到子节点
            node = node.children[char]
        # 单词遍历完，在最后一个节点标记为单词结束
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        # 两个条件：
        # 1. 节点存在 (即路径走通了)
        # 2. isEnd 为 True (必须是完整单词，不能只是别人的前缀)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        # 只要能走完前缀的路径，就返回 True，不需要管 isEnd
        return node is not None

    # 辅助函数：专门用来走路径
    def searchPrefix(self, prefix: str) -> TrieNode:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None # 路径断了，说明不存在
            node = node.children[char]
        return node
