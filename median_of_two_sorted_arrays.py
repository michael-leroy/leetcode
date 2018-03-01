class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # Important to note the arrays are sorted!
        # Likely the best method is to build a bin tree and choose the lowest value
        # Between both lists so the tree is built in order. This will help maintain
        # Balance and keep searching the tree fast.
        
        bin_tree = BinTree()
        
        for nums, value in nums1, nums2:
            
        

class BinNode(object):
    
    def __init__(self, key):
        
        self.key = value
        
        self.l = None
        
        self.r = None
        
class BinTree(object):
    
    def __init__(self, new_node):
        
        if new_node:
            
            return self.root = BinNode(new_node):
            
        self.root = None
        
        
    def add_to_tree(self, node, new_key):
        
        if not self.root:
            
            return self.root = BinNode(new_key):
        
        if new_key < node.key:
            
            if not node.l:
                
                node.l = BinNode(new_key)
            
            else:
                
                add_to_tree(node.l, new_key)
                
        else:
            
            if not node.r:
                
                node.r = BinNode(new_key)
                
            else:
                
                add_to_tree(node.r, new_key)
            
