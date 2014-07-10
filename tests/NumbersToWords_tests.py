from unittest import TestCase
from lib import NumbersToWords

class NumbersToWordsTest(TestCase):

	def test_1_prints_out_One(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(1), "One");

	def test_5_prints_out_Five(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(5), "Five");

	def test_12_prints_Twelve(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(12), "Twelve");