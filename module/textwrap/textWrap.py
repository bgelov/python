import textwrap

#textwrap examples:
#https://www.tutorialspoint.com/python-text-wrapping-and-filling

def wrap(string, max_width):
    result = textwrap.fill(string,max_width)
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
