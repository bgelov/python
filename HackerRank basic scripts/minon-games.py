def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if (string[i:].startswith(sub_string)):
            count += 1
    return count

def minion_game(string):
    vowels = "A","E","I","O","U"
    KevinResult = StuartResult = 0
    KevinList = []
    StuartList = []
    for i in range(0,len(string)):
        if (string[i] in vowels):
            if (string[i] not in KevinList):
                KevinResult += count_substring(string,string[i])
                KevinList.append(string[i])
            for j in range(i+1,len(string)+1):
                if (string[i:j] not in KevinList):
                    KevinResult += count_substring(string,string[i:j])
                    KevinList.append(string[i:j])
        elif (string[i] not in vowels):
            if (string[i] not in StuartList):
                StuartResult += count_substring(string,string[i])
                StuartList.append(string[i])
            for j in range(i+1,len(string)+1):
                if (string[i:j] not in StuartList):
                    StuartResult += count_substring(string,string[i:j])
                    StuartList.append(string[i:j])
                
    if (KevinResult > StuartResult):
        print(f"Kevin {KevinResult}")
    elif (StuartResult > KevinResult):
        print(f"Stuart {StuartResult}")
    else:
        print(f"Draw")

print(minion_game("BANANA"))


