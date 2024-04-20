class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_seq_len = 0
        sequence_len = 0
        for n in nums:

            if n-1 not in nums and n+1 in nums:
                sequence_len = 1
                check_val = n
                while check_val+1 in nums:
                    check_val += 1
                    sequence_len += 1
                if sequence_len>longest_seq_len:
                    longest_seq_len = sequence_len                

        if len(nums)==0:
            return 0  
        if len(nums)==1 or longest_seq_len==0:
            return 1  
        
        
        return longest_seq_len