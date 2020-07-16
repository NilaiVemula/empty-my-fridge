#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main script for Empty My Fridge project. Provides a CLI for the Spoonacular API.

"""

import requests
from rich import print
from rich.console import Console

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

    r = requests.get('https://api.spoonacular.com/recipes/findByIngredients/', params=parameters)
    data = r.json()
    recipes = []
    missing_ingredients = []
    links = []
    for recipe in data:

        # get recipe information
        param = {
            'apiKey': config.API_KEY,
            'includeNutrition': False
        }

        a = requests.get('https://api.spoonacular.com/recipes/' + str(recipe['id']) + '/information', params=param)
        d = a.json()

        recipes.append(recipe['title'])
        list_of_missing = recipe['missedIngredients']
        missing_string = ''
        for item in list_of_missing:
            missing_string += item['originalString']
            missing_string += ', '
        missing_ingredients.append(missing_string)
        links.append(d['sourceUrl'])

    return recipes, missing_ingredients, links
    # TODO: add text formatting of json output and make it pretty with https://github.com/willmcgugan/rich
    # return tuple of lists with recipe name, missing ingredients, etc


def main():
    # initialize the rich environment for command line formatting
    console = Console()

    # get user inputs
    ingredients = console.input("Enter the ingredients you have (each separated by a comma and a space): ")
    amount_recipes = int(console.input("How many recipes do you want to see? "))
    while amount_recipes < 1:
        amount_recipes = int(console.input("Please enter 1 or higher: "))

    # call method to get results
    recipes, missing, links = get_missing_ingredients(ingredients, amount_recipes)
    print(recipes)
    print(missing)

    # format output
    # unpack results and format into table
    from rich.table import Table

    # initialize table
    table = Table(title='Recipes you can make with ' + ingredients)
    table.add_column("Recipe Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("Missing Ingredients", style="magenta")
    table.add_column("Recipe Link", justify="right", style="green")

    # load data
    for recipe, missing_ingredients, link in zip(recipes, missing, links):
        table.add_row(recipe, missing_ingredients, link)
    # todo make full links and ingrediant list show up

    console.print(table)
    print("Visit my [link=https://www.willmcgugan.com]blog[/link]!")
    # todo figure out links


if __name__ == "__main__":
    main()
