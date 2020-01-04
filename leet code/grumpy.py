class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # grumpy -> number of customers that are grumpy
        # customers - > numbe of customers that are satisfied
        for i in range(len(grumpy)):
            grumpy[i]  = grumpy[i] * customers[i]
            if grumpy[i] != 0: customers[i] = 0
        
        # find the highest concentration of grumpy customers within the window
        max_grumpy = cur_grumpy = sum(grumpy[:X])           
        for i in range(1, len(grumpy) - X + 1):    
            cur_grumpy = cur_grumpy - grumpy[i-1] + grumpy[i+X-1]
            if cur_grumpy > max_grumpy: max_grumpy = cur_grumpy
  
        return sum(customers) + max_grumpy