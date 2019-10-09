#!/usr/bin/python

import argparse

def find_max_profit(prices):
  small_price = prices[0]
  largest_profit = prices[1] - prices[0]
  print(largest_profit)
  # loop through to find the smallest item in the array that is not the last
  for lowest in range(0,len(prices) - 1):
        if prices[lowest] != small_price and prices[lowest] - small_price > largest_profit:
              largest_profit = prices[lowest] - small_price
              
        if prices[lowest] < small_price:
              small_price = prices[lowest]
        
  return largest_profit
              

        
print(find_max_profit([100, 90, 80, 50, 20, 10]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))