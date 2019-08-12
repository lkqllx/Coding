class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        hash_ = hash(key)
        self.dict[hash_] = key

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        hash_ = hash(key)
        del self.dict[hash_]

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.dict.keys():
            hash_ = hash(key)
            return (key == self.dict[hash_])
        else:
            return False

    @staticmethod
    def hash(key):
        return (key % 1000000)

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(2)
param_3 = obj.contains(1)
print(param_3)