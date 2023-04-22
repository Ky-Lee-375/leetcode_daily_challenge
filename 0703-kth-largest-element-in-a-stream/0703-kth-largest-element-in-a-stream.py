class KthLargest:

    def __init__(self, k, nums):
        self.arr = sorted(nums)
        self.k = k

    def add(self, val):
        bisect.insort(self.arr, val)
        return self.arr[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)