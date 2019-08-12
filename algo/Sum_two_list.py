class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        ResultDict = {}
        dict2 = {}

        # for idx in range(len(list1)):
        #     dict1[list1[idx]] = idx

        for idx in range(len(list2)):
            dict2[list2[idx]] = idx

        for idx, val in enumerate(list1):
            if val in dict2.keys():
                ResultDict[val] = idx + dict2[val]

        sorted(ResultDict.items(), key=lambda t: t[1])
        LeastValue = list(ResultDict.values())
        LeastValue = LeastValue[0]

        return [x for x in ResultDict.keys() if ResultDict[x] == LeastValue]

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]

s = Solution()
a = s.findRestaurant(list1, list2)
print(a)
