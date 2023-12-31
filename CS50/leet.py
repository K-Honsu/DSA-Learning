class PlusOne:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits = digits[::-1]
        one, i = 1, 0
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] +=1
                    one = 0
            else:
                digits.append(i)
                one = 0
            # i += 1
        return digits

so = PlusOne()
# print(so.plusOne([1,2,3,9]))

def plus1One(digits):
    carry = 1  # Start with a carry of 1 to increment by one
    
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += carry
        # print(digits)
        carry = digits[i] // 10
        # print(carry)
        digits[i] %= 10
        print(digits)
        
    if carry:
        digits.insert(0, carry)
    
    return digits


print(plus1One([1,2,3,9]))
print(10//10)

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        first , last = 0, len(nums) -1
        while first <= last:
            middle = first + (last - first) // 2 
            if nums[middle] == target:
                return middle
            elif nums[middle] >= nums[first]:
                if target >= nums[first] and target < nums[middle]:
                    last = middle - 1
                else:
                    first = middle + 1
            else:
                if target > nums[middle] and target <= nums[last]:
                    first = middle + 1
                else:
                    last = middle - 1
        return -1
    
print(1//2)
    # first,last = 0, len(nums) -1
    #     while first <= last:
    #         middle = first + (last - first) //2 
    #         if nums[middle] == target:
    #             return nums[middle]
    #         elif nums[middle] > target:
    #             first = middle + 1
    #             if target in nums[first:]:
    #                 return nums[target]
    #         else:
    #             last = middle -1
    #     return -1