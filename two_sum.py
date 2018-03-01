class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

            
        
        nums_dict = {}
        
        dict_build_index = 0
        
        for numbers in nums:
            
            complement = target - numbers
            
            if nums_dict.has_key(complement):
                
                return [ nums_dict[complement], dict_build_index ]
            
            else:
                
                nums_dict[numbers] = dict_build_index
            
            dict_build_index += 1


