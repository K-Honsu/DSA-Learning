# arr = [1,2,3,4,5,3,4,5,6,1,2,3]
# # for i in arr:
# #     # print(arr[i])
# #     if arr.count(i) > 1:
# #         arr.pop(i)
# #     else:
# #         print('y')
# #     print(i)

# # dic = {'name':'bola', 'age':25}
# # print(list(dic.values()))
# class Solution:
#     def removeDuplicates(self, nums) -> int:
#         if not nums:
#             return 0
#         k = 1
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i-1]:
#                 # print(nums[k])
#                 nums[k] = nums[i]
#                 k += 1
#         return k
                
# lis = Solution()
# print(lis.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
        
        
class Solution:
    def containsDuplicate(self, nums:list[int]) -> bool:
        for i in range(len(nums)):
            if nums.count(nums[i]) > 1:
                return True
        return False
    
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
# lis = Solution()
# print(lis.containsDuplicate([3,3]))
# print(lis.isAnagram('aacc', 'ccac'))

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else:
                potentialProfit = prices[i] - minPrice
                if potentialProfit > maxProfit:
                    maxProfit = potentialProfit
        return maxProfit
    
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '{':'}','[':']'}
        sl = s.split(' ')
        print(sl)
        
s = Solution()
s.isValid("()[]{}")