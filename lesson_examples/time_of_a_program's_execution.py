import time

def myfunction():
	start_time = time.time()

	s = 0

	for i in range(1, n+1):
		s = s + i

	end_time = time.time()

	return s, end_time - start_time

n = 139897
print(myfunction())