Numbers to Words (Python)
=========================
A personal Python challenge I wanted to take on. This script takes a numerical input and outputs the words in English. This was coded using Test/Behaviour Driven Development (PyUnit).

# NOTE
I wrote this script in JavaScript and Ruby

# Examples
```python
from lib import NumbersToWords
numbers_to_words = NumbersToWords.NumbersToWords()
print numbers_to_words.convert(123) #=> "One Hundred and Twenty Three"

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
