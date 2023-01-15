def merge_the_tools(string, k):
    lastIndex = 0
    for i in range(k,len(string)+1,k):
        substring = list(map(str, string[lastIndex:i]))
        lastIndex = i
        
        newSubstring = ""
        for i in range(len(substring)):
            if substring[i] not in newSubstring:
                newSubstring += substring[i]
        
        print(newSubstring)
            
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
