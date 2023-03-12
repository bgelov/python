# Counting sort
# Yandex Academy https://www.youtube.com/watch?v=Nb5mW1yWVSs&list=PL6Wui14DvQPySdPv5NUqV3i8sDbHkCKC5&index=4

def isdigitpermutation(x, y):
    def countdigits(num)
	    digitcount = [0] * 10
		while num > 0:
		    lastdigit = num % 10
			digitcount[lastdigit] += 1
			num //= 10
	    return digitcount
	
	digitsx = countdigits(x)
	digitsy = countdigits(y)
	for digit in range(10):
	    if digitsx[digit] != digitsy[digit]:
		    return False
	return True