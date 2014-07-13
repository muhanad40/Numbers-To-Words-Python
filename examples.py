from lib import NumbersToWords
numbers_to_words = NumbersToWords.NumbersToWords()
print numbers_to_words.convert(123) #=> "One Hundred and Twenty Three"

rabbits = NumbersToWords.NumbersToWords("rabbits")
print rabbits.convert(123) #=> "One Hundred and Twenty Three Rabbits"

pounds = NumbersToWords.NumbersToWords("pounds")
print pounds.convert(123) #=> "One Hundred and Twenty Three Pounds"