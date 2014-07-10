class NumbersToWords(object):
	def __init__(self):
		self.ONES_TENS = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split(" ")
		self.MULTIPLES_OF_TEN = "ten twenty thirty fourty fifty sixty seventy eighty ninty hundred".split(" ")

	def convert_segment(self, number):
		output = ""
		if number <= 20:
			output += self.ONES_TENS[number-1].capitalize()
		elif number <= 99:
			output += self.MULTIPLES_OF_TEN[number/10-1].capitalize()
			if number%10 != 0:
				output += " " + self.ONES_TENS[number%10-1].capitalize()
		return output
