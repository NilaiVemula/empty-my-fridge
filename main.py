#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main script for Empty My Fridge project. Provides a CLI for the Spoonacular API.

"""

import requests

import config


def get_missing_ingredients(available_ingredients, amount_recipes):
    """

    :param available_ingredients: comma separated list of ingredients the user has
    :type available_ingredients: str
    :param amount_recipes: number of recipes that the user wants
    :type amount_recipes: int
    :return: None
    """

    # explanation of API parameters: https://spoonacular.com/food-api/docs#Search-Recipes-by-Ingredients
    # ingredients (string): A comma-separated list of ingredients that the recipes should contain.
    # number (number): The maximum number of recipes to return (between 1 and 100). Defaults to 10.
    # limitLicense (bool): Whether the recipes should have an open license that allows display with proper attribution.
    # ranking (number): Whether to maximize used ingredients (1) or minimize missing ingredients (2) first.
    # ignorePantry (bool): Whether to ignore typical pantry items, such as water, salt, flour, etc.
    parameters = {
        'apiKey': config.API_KEY,
        'ingredients': available_ingredients,
        'number': amount_recipes,
        'ranking': 2,
        'ignorePantry': True
    }

    r = requests.get('https://api.spoonacular.com/recipes/findByIngredients', params=parameters)
    print(r.url)
    print(r.json())
    # TODO: add text formatting of json output and make it pretty with https://github.com/willmcgugan/rich


def main():
    ingredients = input("Enter the ingredients you have (each separated by a space): ")
    amount_recipes = int(input("How many recipes do you want to see? "))
    while amount_recipes < 1:
        amount_recipes = input("Please enter 1 or higher: ")

    temp = ingredients.split()  # separate the individual ingredients into a list

    # creating a string of ingredients separated by a comma
    ingredients = ""
    for item in temp:
        ingredients = ingredients + item
        ingredients = ingredients + ", "

    if len(ingredients) != 0:
        ingredients = ingredients[:-2]  # remove the last space and comma

    get_missing_ingredients(ingredients, amount_recipes)


if __name__ == "__main__":
    main()
