from nose.tools import *
from lib import NumbersToWords

def test_1_prints_out_One():
	numbers_to_words = NumbersToWords.NumbersToWords()

	assert_equal(numbers_to_words.convert_segment(1), "One");

def test_5_prints_out_Five():
	numbers_to_words = NumbersToWords.NumbersToWords()

	assert_equal(numbers_to_words.convert_segment(5), "Five");