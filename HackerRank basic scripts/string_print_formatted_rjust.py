def print_formatted(number):
    max_width = len(str(bin(number)[2:]))
    for i in range(1,number+1):
        d = str(i).rjust(max_width)
        o = str(oct(i)[2:]).rjust(max_width)
        h = str(hex(i)[2:]).rjust(max_width)
        b = str(bin(i)[2:]).rjust(max_width)
        print(d,o,h,b) 

    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
