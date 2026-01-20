"""
146. LRU 缓存

请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

 

示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
 

提示：

1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 105
最多调用 2 * 105 次 get 和 put

medium

"""
class node:
    def __init__(self, key=0, val=0 ):
        # 当缓存满了，我们需要删除链表最前面的那个节点（最久未使用的）。
        # 删除后，我们还得去哈希表里把对应的 key 也删掉。
        # 如果 Node 里只有 value，就不知道该去哈希表里删哪个key。
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    # 双向链表 + hash 保证 O(1)
    def __init__(self, capacity: int):
        # 注意：hash的value是node而不是题目中给的数值value
        self.hash = {} # 内容： key -> Node
        self.head = node() # dummy head，形成上界
        self.tail = node() # dummy tail，形成下界
        self.cap = capacity

        self.head.next = self.tail
        self.tail.prev = self.head

    # 从链表中删除一个节点, 双向均要考虑
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # 把节点插到 tail.prev 和 tail 之间，因为tail是None
    def add_to_tail(self, node):
        # 注意：要更新两头，既要更新node，也要更新tail
        node.prev = self.tail.prev
        node.next = self.tail
        
        self.tail.prev.next = node # 原本的倒数第一指向新节点
        self.tail.prev = node      # tail 指向新节点

    def move_to_end(self, node):
        self.remove_node(node)
        self.add_to_tail(node)

    def get(self, key: int) -> int:
        if key in self.hash:
            # 读取也要更新链表
            cur_node = self.hash[key]
            self.move_to_end(cur_node)
            return cur_node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            cur_node = self.hash[key]
            cur_node.val = value # 更新数值
            # 更新链表
            self.move_to_end(cur_node)
        else:
            if len(self.hash) == self.cap:
                # 清除头部, 即head.next
                cur_del_node = self.head.next
                self.remove_node(cur_del_node)
                # 这里用到了之前定义的key
                del self.hash[cur_del_node.key]
            # 创建新node
            cur_node = node(key, value)
            self.hash[key] = cur_node
            self.add_to_tail(cur_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)