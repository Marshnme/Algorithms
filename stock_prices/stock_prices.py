#!/usr/bin/python

import argparse
my_list = [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]
def find_max_profit(prices):
	profit = prices[1] - prices[0]
	buy = prices[0]
	
	

	for p in prices[1:]:
		print("p",p)
		if p - buy > profit:
			profit = p - buy
			print("profit",profit)
		if p<buy:
			buy = p
			print("buy",buy)
	return profit

find_max_profit(my_list)





# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))