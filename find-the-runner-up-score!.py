# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?h_r=next-challenge&h_v=zen

def main(n, arr):
	winner = max(arr)
	runner = min(arr)
	for i in range(n):
		if arr[i] > runner and arr[i] < winner:
			runner = arr[i]

	print(runner)


if __name__ == '__main__':
	main(4, [1,1,-1,1])