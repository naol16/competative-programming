string = ""
        strs = sorted(strs)
        first_string = strs[0]
        last_string= strs[-1]
            
        for i in range(len(first_string)):
            for element_s in strs:
                if i==len(element_s) or element_s[i]!=strs[0][i]:
                   return string
            else:
                 string+=element_s[i]
        return string
            
