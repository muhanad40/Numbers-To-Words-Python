class NumbersToWords(object):
	def __init__(self):
		self.ONES_TENS = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split(" ")
		self.MULTIPLES_OF_TEN = "ten twenty thirty fourty fifty sixty seventy eighty ninty hundred".split(" ")
		self.WORDS = "hundred thousand million billion trillion gazillion".split(" ")

	def convert_segment(self, number):
		output = ""
		if number <= 20:
			output = self.ONES_TENS[number-1].capitalize()
		elif number <= 99:
			output = self.MULTIPLES_OF_TEN[number/10-1].capitalize()
			if number%10 != 0:
				output += " " + self.ONES_TENS[number%10-1].capitalize()
		elif number <= 999:
			output = self.ONES_TENS[number/100-1].capitalize()
			output += " " + self.WORDS[0].capitalize()
			if number%100 != 0:
				output += " and " + self.convert_segment(number%100)
		return output
