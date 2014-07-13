from unittest import TestCase
from lib import NumbersToWords

class NumbersToWordsTest(TestCase):

	def test_1_prints_One(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(1), "One")

	def test_5_prints_Five(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(5), "Five")

	def test_12_prints_Twelve(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(12), "Twelve")

	def test_20_prints_Twenty(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(20), "Twenty")

	def test_21_prints_Twenty_One(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(21), "Twenty One")

	def test_55_prints_Fifty_Five(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(55), "Fifty Five")

	def test_99_prints_Ninty_Nine(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(99), "Ninty Nine")

	def test_100_prints_One_Hundred(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(100), "One Hundred")

	def test_101_prints_One_Hundred_and_One(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(101), "One Hundred and One")

	def test_109_prints_One_Hundred_and_Nine(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(109), "One Hundred and Nine")

	def test_115_prints_One_Hundred_and_Fifteen(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(115), "One Hundred and Fifteen")

	def test_138_prints_One_Hundred_and_Thirty_Eight(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(138), "One Hundred and Thirty Eight")

	def test_581_prints_Five_Hundred_and_Eighty_One(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(581), "Five Hundred and Eighty One")

	def test_999_prints_Nine_Hundred_and_Ninty_Nine(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(999), "Nine Hundred and Ninty Nine")

class NumbersToWordsEdgeCaseTests(TestCase):

	def test_000_prints_nothing(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(000), "")

class NumbersToWordsLargeNumberTests(TestCase):

	def test_split_numbers_into_segments_of_3s(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.make_segments(1234), ["1", "234"])

	def test_1000_prints_One_Thousand(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(1000), "One Thousand")

	def test_1001_prints_One_Thousand_One(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(1001), "One Thousand, One")

	def test_1011_prints_One_Thousand_Eleven(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(1011), "One Thousand, Eleven")

	def test_1020_prints_One_Thousand_Twenty(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(1020), "One Thousand, Twenty")

	def test_1058_prints_One_Thousand_Fifty_Eight(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(1058), "One Thousand, Fifty Eight")

	def test_1100_prints_One_Thousand_One_Hundred(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(1100), "One Thousand, One Hundred")

	def test_1553_prints_One_Thousand_Five_Hundred_and_Fifty_Three(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(1553), "One Thousand, Five Hundred and Fifty Three")

	def test_4835_prints_Four_Thousand_Eight_Hundred_and_Thirty_Five(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(4835), "Four Thousand, Eight Hundred and Thirty Five")

	def test_9999_prints_Nine_Thousand_Nine_Hundred_and_Ninty_Nine(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(9999), "Nine Thousand, Nine Hundred and Ninty Nine")

	def test_10000_prints_Ten_Thousand(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(10000), "Ten Thousand")

	def test_10001_prints_Ten_Thousand_One(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(10001), "Ten Thousand, One")

	def test_10015_prints_Ten_Thousand_Fifteen(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(10015), "Ten Thousand, Fifteen")

	def test_10100_prints_Ten_Thousand_One_Hundred(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(10100), "Ten Thousand, One Hundred")

	def test_10999_prints_Ten_Thousand_Nine_Hundred_and_Ninty_Nine(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(10999), "Ten Thousand, Nine Hundred and Ninty Nine")

	def test_15351_prints_Fifteen_Thousand_Three_Hundred_and_Fifty_One(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(15351), "Fifteen Thousand, Three Hundred and Fifty One")

	def test_99351_prints_Ninty_Nine_Thousand_Three_Hundred_and_Fifty_One(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(99351), "Ninty Nine Thousand, Three Hundred and Fifty One")

	def test_199351_prints_One_Hundred_and_Ninty_Nine_Thousand_Three_Hundred_and_Fifty_One(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(199351), "One Hundred and Ninty Nine Thousand, Three Hundred and Fifty One")

	def test_199999_prints_One_Hundred_and_Ninty_Nine_Thousand_Nine_Hundred_and_Ninty_Nine(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(199999), "One Hundred and Ninty Nine Thousand, Nine Hundred and Ninty Nine")

	def test_1199999_prints_One_Million_One_Hundred_and_Ninty_Nine_Thousand_Nine_Hundred_and_Ninty_Nine(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(1199999), "One Million, One Hundred and Ninty Nine Thousand, Nine Hundred and Ninty Nine")

	def test_451199999_prints_Four_Hundred_and_Fifty_One_Million_One_Hundred_and_Ninty_Nine_Thousand_Nine_Hundred_and_Ninty_Nine(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(451199999), "Four Hundred and Fifty One Million, One Hundred and Ninty Nine Thousand, Nine Hundred and Ninty Nine")

	def test_1451199999_prints_One_Billion_Four_Hundred_and_Fifty_One_Million_One_Hundred_and_Ninty_Nine_Thousand_Nine_Hundred_and_Ninty_Nine(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(1451199999), "One Billion, Four Hundred and Fifty One Million, One Hundred and Ninty Nine Thousand, Nine Hundred and Ninty Nine")

	def test_211451199999_prints_Two_Hundred_and_Eleven_Trillion_Four_Hundred_and_Fifty_One_Million_One_Hundred_and_Ninty_Nine_Thousand_Nine_Hundred_and_Ninty_Nine(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(211451199999), "Two Hundred and Eleven Billion, Four Hundred and Fifty One Million, One Hundred and Ninty Nine Thousand, Nine Hundred and Ninty Nine")

	def test_1211451199999_prints_One_Trillion_Two_Hundred_and_Eleven_Trillion_Four_Hundred_and_Fifty_One_Million_One_Hundred_and_Ninty_Nine_Thousand_Nine_Hundred_and_Ninty_Nine(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(1211451199999), "One Trillion, Two Hundred and Eleven Billion, Four Hundred and Fifty One Million, One Hundred and Ninty Nine Thousand, Nine Hundred and Ninty Nine")
