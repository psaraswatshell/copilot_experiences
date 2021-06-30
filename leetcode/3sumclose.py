def threesumclosest(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    return target
        return res

def threesum(nums, target):       
        nums.sort()       
        res = sum(nums[:3])       
        for i in range(len(nums) - 2):       
            j, k = i + 1, len(nums) - 1       
            while j < k:       
                s = nums[i] + nums[j] + nums[k]       
                if abs(s - target) < abs(res - target):       
                    res = s       
                if s < target:       
                    j += 1       
                elif s > target:       
                    k -= 1       
                else:       
                    return target       
        return res