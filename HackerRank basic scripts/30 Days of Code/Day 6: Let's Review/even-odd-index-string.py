if __name__ == '__main__':
    T = int(input())
   

for i in range(T):
    string = str(input())
    strEven = strOdd = ""
    for j in range(len(string)):
        if (j % 2 == 0):
            strEven += string[j]
        else:
            strOdd += string[j]
    print(f"{strEven} {strOdd}")
    
