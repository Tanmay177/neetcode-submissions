class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 = {}
        for n in nums:
            if n in map1:
                map1[n] += 1
            else:
                map1[n] = 1

        sorted_items = sorted(map1.items(), key=lambda item: item[1], reverse = True) 
        print(sorted_items)
        #item_list = list(sorted_items)

        list1 = [0]*k

        for n in range(k):
            list1[n] = sorted_items[n][0]
        return list1