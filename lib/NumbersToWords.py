class NumbersToWords(object):
	def __init__(self):
		self.ONES_TENS = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split(" ")
		self.MULTIPLES_OF_TEN = "ten twenty thirty fourty fifty sixty seventy eighty ninty hundred".split(" ")
		self.WORDS = "hundred thousand million billion trillion gazillion".split(" ")

	def convert_segment(self, number):
		output = ""
		number = int(number)
		if number <= 0:
			output = ""
		else:
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

	def convert(self, number):
		segment_output = ""
		number_segments = self.make_segments(number)
		number_segments = number_segments[::-1]
		for i, segment in enumerate(number_segments):
			if int(segment) > 0:
				segment_output += self.convert_segment(int(segment))
				segment_output += " " + self.WORDS[i].capitalize()
		return segment_output

	def make_segments(self, number):
		# reverse the order of numbers
		number = str(number)[::-1]
		output = []
		# split numbers into segments of 3s
		for num in range(0, len(number), 3):
			output.append(number[num:num+3])
		# reverse each segment back to normal
		for i,v in enumerate(output):
			output[i] = output[i][::-1]
		# reverse the order of segments
		return output[::-1]