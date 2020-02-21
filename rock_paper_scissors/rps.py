#!/usr/bin/python

import sys
moves=[["rock"],["paper"],["scissors"]]

def rock_paper_scissors(n):

	if n == 0:
		return [[]]
	if n == 1:
		return moves
	
	answer = []

	arrN = rock_paper_scissors(n-1)

	for i in arrN:
		for j in moves:
			newMove = i + j
			answer.append(newMove)
	
	return answer


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')