if __name__ == '__main__':
    s = input()

containAlnum = containAlpha = containDigit = containLower = containUpper = False
i = 0

for i in range(len(s)):
    if s[i].isalnum() == True: containAlnum = True
    if s[i].isalpha() == True: containAlpha = True
    if s[i].isdigit() == True: containDigit = True
    if s[i].islower() == True: containLower = True
    if s[i].isupper() == True: containUpper = True

print(containAlnum)
print(containAlpha)
print(containDigit)
print(containLower)
print(containUpper)
