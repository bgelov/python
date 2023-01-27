#https://www.hackerrank.com/challenges/decorators-2-name-directory/problem
#About decorators: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

def person_lister(f):
    def inner(people):
        result = people.sort(key=lambda x: int(x[2]))
        return [f(p) for p in people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')