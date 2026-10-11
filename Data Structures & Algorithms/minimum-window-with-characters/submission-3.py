class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = dict()
        for x in t:
            if x in needed:
                needed[x] += 1
            else:
                needed[x] = 1
        
        current = dict()
        have = 0
        need = len(needed)
        result = len(s)+1
        result_str = [-1, -1]
        left = 0

        for right, ch in enumerate(s):
            if ch in current:
                current[ch] += 1
            else:
                current[ch] = 1
            
            if ch in needed and current[ch] == needed[ch]:
                have += 1
            
            while have == need:
                print(right-left+1)
                if right-left+1 < result:
                    result = right-left+1
                    result_str[0] = left
                    result_str[1] = right
                left_ch = s[left]
                current[left_ch] -= 1
                if left_ch in needed and current[left_ch] < needed[left_ch]:
                    have -= 1
                left += 1

        print(current)
        return s[result_str[0]:result_str[1]+1]
        