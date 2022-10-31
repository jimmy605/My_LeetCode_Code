class Solution:
    def pushDominoes(self, dominoes):
        # Have a variable that tracks what the currect domino is doing
        # Have a variable that tracks to next domino
        # Store the output in a list till the end of iteration
        
        # CASES
        cases = {
            'RR': 'R', 
            'RL': 'R', 
            'R.': 'R',
            'LL': 'L',
            'LR': 'L',
            'L.': 'L',
            '..': '.',
            '.L': 'L',
            '.R': '.'
        }
        
        dom_len = len(dominoes)
        dom_list = []
        
        for d in range(dom_len - 1):
            dom_case =f'{dominoes[d]}{dominoes[d + 1]}'
            
            dom_list.append(cases[dom_case])
        
        print(dom_list)


test = Solution()
test.pushDominoes("RR.L")