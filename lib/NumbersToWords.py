class NumbersToWords(object):
	def __init__(self):
		self.ONES = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split(" ")

	def convert_segment(self, number):
		return self.ONES[number-1].capitalize()