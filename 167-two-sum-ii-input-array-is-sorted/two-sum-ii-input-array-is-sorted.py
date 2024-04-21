class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # if len(numbers) == 2:
        #     return [1,2]

        # p1, p2 = 0, 1
        # while numbers[p1]+numbers[p2]!=target:
        #     # print(numbers[p1], numbers[p2])
        #     if p2 == len(numbers)-1:
        #         p2 = p1+2
        #         p1 += 1
        #     else:
        #         p2 = p2+1
        
        # print(p1, p2)
        # return [p1+1,p2+1]

        for (i, val) in enumerate(numbers):
            req1 = target - val
            if req1 == val:
                indices = [i for i, x in enumerate(numbers) if x == val]
                return [indices[0]+1, indices[0]+2]
            if req1 in numbers:
                ind = numbers.index(req1)
                return [i+1, ind+1]
            # if req2 in numbers:
            #     ind = numbers.index(req2)
            #     return [i+1, ind+1]
