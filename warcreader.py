# Copyright 2016 Milos Svana
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from gzip import GzipFile
import re

class Webpage(object):
	'''
	Represents one webpage (or HTTP response) from WARC file. You can access:
	- webpage payload
	- uri 
	- title if present
	- is_html - a boolean which tells if the payload is a HTML webpage
	'''

	title_re = re.compile(
		'<head>.*?<title>(.*?)</title>.*?</head>', 
		re.IGNORECASE | re.DOTALL)

	def __init__(self, uri, payload, is_html):
		''' Called by WarcReader '''
		self.uri = uri
		self.payload = payload
		self.is_html = is_html
		self.title = self.extract_title()

	def extract_title(self):
		'''
		Extracts webpage title from html <title /> element in the payload using
		a regular expression. Returns None if no title is found.
		'''
		matches = self.title_re.search(self.payload[:20000])
		if matches:
			return matches.group(1)
		else:
			return None

class WarcReader(object):
	'''
	Reads the web achive (WARC) files. 
	Can iterate through HTTP responses inside using a simple state machine.
	'''

	http_response_re = re.compile(b'^HTTP\/1\.[01] 200')
	h_letter = b'H'

	def __init__(self, filename):
		'''
		Opens the WARC file for reading and sets the initial state of the 
		state machine. Supports raw or Gzip compressed (file must have '.gz'
		extension) WARC files. 
		'''
		self.open(filename)
		self.in_warc_response = False
		self.in_http_response = False
		self.in_payload = False

	def iterate(self):
		'''
		Generator that provides HTTP responses from the WARC file as instances 
		of Webpage class one at the time. Can be used in the for loop:

		warc_reader = new WarcReader("some-warc.gz")
		for webpage in warc_reader.iterate():
			print(webpage.title)
		'''
		payload = ''
		is_html = False
		for line in self.file_obj:
			if not self.in_warc_response:
				if line == b'WARC-Type: response\r\n':
					self.in_warc_response = True
				continue
			if not self.in_http_response:
				if line[:11] == b'WARC-Target':
					target_uri = line[17:-2]
				elif line[0:1] == self.h_letter and self.http_response_re.match(line):
					self.in_http_response = True
				continue
			if not self.in_payload:
				if line[:23] == b'Content-Type: text/html':
					is_html = True
				elif line == b'\r\n':
					self.in_payload = True
				continue
			if line == b'WARC/1.0\r\n':
				yield Webpage(target_uri, payload, is_html)
				self.in_payload = self.in_http_response = self.in_warc_response = is_html = False
				payload = ''
				continue
			payload += str(line)

	def open(self, filename):
		'''
		Opens the WARC file in standard Python way or as a GzipFile if the
		filename ends with .gz. Both object provide same interface for reading
		so it's not required to differentiate between them anywhere else
		'''
		file_handle = open(filename, 'rb')
		if filename[-3:] =='.gz':
			self.file_obj = GzipFile(mode='r', fileobj=file_handle)
		else:
			self.file_obj = file_handle
		return self.file_obj
