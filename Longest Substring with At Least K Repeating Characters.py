class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def getMaxUniqueLetters(s):
            # Get the number of unique letters in the string
            return len(set(s))
        
        max_unique = getMaxUniqueLetters(s)
        result = 0

        # Try all possible counts of distinct characters in the substring
        for curr_unique in range(1, max_unique + 1):
            count_map = [0] * 26  # Frequency map for 26 lowercase letters
            window_start = 0
            window_end = 0
            unique = 0
            count_at_least_k = 0
            
            # Sliding window logic
            while window_end < len(s):
                if unique <= curr_unique:
                    # Expand the window
                    idx = ord(s[window_end]) - ord('a')
                    if count_map[idx] == 0:
                        unique += 1
                    count_map[idx] += 1
                    if count_map[idx] == k:
                        count_at_least_k += 1
                    window_end += 1
                else:
                    # Shrink the window
                    idx = ord(s[window_start]) - ord('a')
                    if count_map[idx] == k:
                        count_at_least_k -= 1
                    count_map[idx] -= 1
                    if count_map[idx] == 0:
                        unique -= 1
                    window_start += 1
                
                # Update result if the conditions are satisfied
                if unique == curr_unique and unique == count_at_least_k:
                    result = max(result, window_end - window_start)
        
        return result
