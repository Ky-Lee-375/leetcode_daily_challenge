class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ValueCounter = list(collections.Counter(tasks).values()) 
        
        maxCount = max(ValueCounter) 
        num_of_chars_with_max_count = ValueCounter.count(maxCount) 
        
        num_of_chunks_with_idles = maxCount-1 

        length_of_a_chunk_with_idle = n+1  

        length_of_the_final_chunk = num_of_chars_with_max_count  

        length_of_all_chunks = (num_of_chunks_with_idles*length_of_a_chunk_with_idle) + length_of_the_final_chunk 

        return max(len(tasks), length_of_all_chunks)
        