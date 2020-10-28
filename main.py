#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import sys
import json


def main(book):
	print(book)
	with open('bookInfo.json') as jsonFile:
		bookInfo = json.load(jsonFile)

	code = bookInfo[book]['code']
	nChapters = bookInfo[book]['length']

	f = open('markdownBooks/{}.md'.format(book), 'w')

	f.write('# {}\n\n'.format(book))

	for ch in range(nChapters):

		f.write('## Ch {}.\n\n'.format(ch+1))

		r = requests.get('https://esv.literalword.com/?q={}+{}'.format(book, ch+1))

		soup = BeautifulSoup(r.text, 'html.parser')
		verses = soup.find_all('span', {'class': 'bV'})

		for i, verse in enumerate(verses):
			verseText = verse.text.strip()
			if i == 0:
				f.write('{} {} ^{}-{}\n\n'.format(code, verseText, ch+1, i+1))
			else:
				f.write('{} {}:{} ^{}-{}\n\n'.format(code, ch+1, verseText, ch+1, i+1))

		f.write('\n')


if __name__ == '__main__':
	book = sys.argv[1]
	main(book)