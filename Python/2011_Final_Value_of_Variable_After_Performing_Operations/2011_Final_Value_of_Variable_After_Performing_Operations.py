class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        i = 0

        for op in operations:
            if op == '++X' or op == 'X++':
                i += 1
            else:
                i -= 1
        
        return i