class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reverse=True)

        total_cost = 0
        
        //Pop 3 number with free if length of array is equal or greater than 3
        while(len(cost) >= 3):
            num1 = cost.pop(0)
            num2 = cost.pop(0)
            free = cost.pop(0)          //free toffee which isnt counted
            total_cost += num1 + num2

        total_cost += sum(cost)

        return total_cost

// if __name__ == "__main__":
//     sol = Solution()

//     print(sol.minimumCost([1, 2, 3]))          # Expected: 5
//     print(sol.minimumCost([6, 5, 7, 9, 2, 2])) # Expected: 23
//     print(sol.minimumCost([5, 5]))             # Expected: 10