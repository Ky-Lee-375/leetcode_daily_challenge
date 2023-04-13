class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1
        sort_dict = sorted(dictionary,  key=lambda x : dictionary[x])
        return sort_dict[-k:]