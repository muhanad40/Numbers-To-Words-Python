from unittest import TestCase
from lib import NumbersToWords

class NumbersToWordsTest(TestCase):

	def test_1_prints_out_One(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(1), "One")

	def test_5_prints_out_Five(self):
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