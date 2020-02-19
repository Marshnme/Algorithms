#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    #Compare lowest values of recipe specifcs vs ingred specfics
    #if ingred<recipe 0
    #elif ingred>recipe divide recipe into ingred
    #count how many times 
    batches = 0
    # index_left = index_right = 0

    # recipe_temp = min(recipe.values()) 
    # ingredients_temp = min(ingredients.values()) 

    # recipe_res = [key for key in recipe if recipe[key] == recipe_temp] 
    # ingredients_res = [key for key in ingredients if ingredients[key] == ingredients_temp]

    # print(recipe_res)
    # print(ingredients_res)
    # print(recipe['milk'])

    if len(recipe) > len(ingredients):
        return batches 
    for recipe_key, recipe_value in recipe.items():
        # print(recipe_key,recipe_value)
        for ingredients_key, ingredients_value in ingredients.items():
            # print(ingredients_key,ingredients_value)
            if ingredients_key == recipe_key:
                if ingredients_value // recipe_value >=1:
                    number = ingredients_value // recipe_value
                    print(number)
                    if ingredients_value // recipe_value == number:
                        batches += number
                        return batches             
                else:
                    batches = 0
                    return batches 



    return batches

    
    
  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 50, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))