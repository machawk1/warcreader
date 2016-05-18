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

'''
Simple test script which prints all HTTP responses' URLs and their total
count from a warc file whose path is passed as command line argument.

Does not support gzipped files.
'''

from warcreader import WarcFile
from sys import argv

def main():
	filename = argv[1]
	with open(filename, 'r') as raw_warc_file:
		warc_file = WarcFile(raw_warc_file)
		count = 0
		for webpage in warc_file:
			count += 1
			print(webpage.uri)
		print('Total count of HTTP responses: %d' % count)

if __name__ == '__main__':
	main()

