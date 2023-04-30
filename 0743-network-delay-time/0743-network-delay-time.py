class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        #bellman-ford
        array = [0] + [float("inf")] * N
        array[K] = 0
        for node in range(1,N): 
            for u,v,w in times:
                if array[u] + w < array[v]:
                    array[v] = array[u] + w
        if max(array) < float("inf"):
            return max(array)
        else:
            return -1