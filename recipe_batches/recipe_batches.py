#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  arr = []
  for incredient in recipe:
        if ingredients.get(incredient) == None:
              return 0 
        else:
              diff = ingredients[incredient] // recipe[incredient]
              arr.append(diff)
  sorted_arr = sorted(arr)
  return sorted_arr[0]
              

print(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }))

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))