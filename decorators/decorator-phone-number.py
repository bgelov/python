#https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
#About decorators: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

def wrapper(f):
    def fun(l):
        f([f"+91 {num[-10:-5]} {num[-5:]}" for num in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
