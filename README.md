Numbers to Words (Python)
=========================
A personal Python challenge I wanted to take on. This script takes a numerical input and outputs the words in English. This was coded using Test/Behaviour Driven Development (PyUnit).

# NOTE
I wrote this script in [JavaScript](https://github.com/muhanad40/Numbers-To-Words-JS) and [Ruby](https://github.com/muhanad40/Numbers-To-Words-Ruby)

# Examples
```python
from lib import NumbersToWords

numbers_to_words = NumbersToWords.NumbersToWords()
print numbers_to_words.convert(123) #=> "One Hundred and Twenty Three"

# Output with a context
rabbits = NumbersToWords.NumbersToWords("rabbits")
print rabbits.convert(123) #=> "One Hundred and Twenty Three Rabbits"

pounds = NumbersToWords.NumbersToWords("pounds")
print pounds.convert(123) #=> "One Hundred and Twenty Three Pounds"
```

# Demo
http://numberstowords-python.heroku.com/

# Technologies
* Flask
* PyUnit
* Heroku
