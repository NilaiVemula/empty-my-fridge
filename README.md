# Empty My Fridge

Given a list of ingredients, Empty My Fridge will provide a list of recipes that you can make with what is already in 
 your fridge! Using the [Spoonacular API](https://spoonacular.com/food-api) and the python requests library, this 
 tool aims to eliminate food waste by providing the user with recipes that can be made with ingredients they already have. 

## Accessing the API
In order to use the Spoonacular API, you must create an account and request an API key. For this project, my API key
 is kept in a file titled `config.py`. This file contains only one line:
 
 ```python
API_KEY = '[insert key here]'
```

This file is not included in the git repository to protect my key, but it is essential for running the script. In my
 `main.py` script, I import the API key as `config.API_KEY`.
 
## Requirements
This project requires Python 3.

## Getting Started
The easiest way to run this script is to clone the repository and then run the `main.py` script using the command
 line after making a `config.py` file as described above.
 
```bash
git clone https://github.com/NilaiVemula/empty-my-fridge.git
python main.py
```

## Examples

TODO: add screenshots using https://github.com/mixn/carbon-now-cli
