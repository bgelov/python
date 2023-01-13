def solve(s):
    result = s[0].capitalize()
    for i in range(1,len(s)):      
        if ((not (s[i-1].isalnum())) and (s[i].isalpha())):
            result += s[i].capitalize()
        else:
            result += s[i]
    return(result)
