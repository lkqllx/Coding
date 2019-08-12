class hashtable:

    def __init__(self, size):
        self.size = size
        self.slot = [None] * self.size
        self.data = [None] * self.size


    def hash(self, key):
        return key % self.size

    def rehash(self, key):
        return (key + 1) % self.size

    def put(self, key, data):
        HashValue = self.hash(key)

        if self.slot[HashValue] is None:
            self.slot[HashValue] = key
            self.data[HashValue] = data

        else:
            if self.slot[HashValue] == key:
                self.data[HashValue] = data # replace

            else:
                    ReHashValue = self.rehash(key)

                    while self.slot[ReHashValue] is not None and self.slot[ReHashValue] != key:
                        ReHashValue = self.rehash(ReHashValue)

                    if self.slot[ReHashValue] is None:
                        self.slot[ReHashValue] = key
                        self.data[ReHashValue] = data

                    elif self.slot[ReHashValue] == key:
                        self.data[ReHashValue] = data # replace


H = hashtable(11)
H.put(0,'cat0')
H.put(1,'cat1')
H.put(2,'cat2')
H.put(3,'cat3')
H.put(4,'cat4')
H.put(5,'cat5')
H.put(6,'cat6')
H.put(7,'cat7')
H.put(12,'cat12')

print(H.slot, '\n', H.data)

