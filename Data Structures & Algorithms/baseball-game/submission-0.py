class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        # list = []
        # ietrate thorugh the operations
        # keep on adding the value in list.
        # prforms checks for +, C and D
        # for +, take the sum of last 2 elements from the list, and append the sum value
        # for C, remove the last element from the list, and do not add C
        # for D, just take the double of the last element, and append the result

        list_ = []

        for ops in operations:
            if ops == "+":
                sum_last_two = list_[-1] + list_[-2]
                list_.append(sum_last_two)
            elif ops == "C":
                list_.pop()
            elif ops == "D":
                double_last_element = 2 * list_[-1]
                list_.append(double_last_element)
            else:
                list_.append(int(ops))
            
        return sum(list_)


