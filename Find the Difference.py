 from collections import Counter
        string1=Counter(s)
        string2=Counter(t)
        for i in string2.keys():
            if i not in string1.keys():
               return i
            else:
                 if string1[i]!=string2[i]:
                    return i
