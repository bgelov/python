#https://docs.python.org/3.5/tutorial/datastructures.html#dictionaries

n = int(input())
phoneDict = {}

for i in range(n):
    name, phone = input().split(" ")
    phoneDict[name] = phone
        
while True:
    try:
        searchName = input()
        print(f"{searchName} = {phoneDict[searchName]}")
    except EOFError:
        break
    except:
        print("Not found")
