import sys
sys.path.append("..")

from flask import render_template, request
from app import app
from lib import NumbersToWords

@app.route('/', methods=['GET'])
def index():
	number = request.args.get('numbers') if request.args.get('numbers')!=None else ''
	context = request.args.get('context') if request.args.get('context')!=None else ''
	if request.method == 'GET' and number != '':
		numbers_to_words = NumbersToWords.NumbersToWords(context)
		numbers_output = numbers_to_words.convert(number)
	else:
		numbers_output = ''
	return render_template('index.html', numbers_output=numbers_output, number=number, context=context)
