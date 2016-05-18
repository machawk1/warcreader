# WarcReader

WarcReader is as Python library for reading HTTP responses from [Web ARChive 
(WARC) files](https://en.wikipedia.org/wiki/Web_ARChive).

Its main goal is to be as fast as possible, not to provide advanced functions
to work with WARC files.

## Authors

Milos Svana (milos.svana(at)gmail.com)

This library was created as a part of my Bachelor's thesis at the
[Knowledge Technology Research Group](http://knot.fit.vutbr.cz/), 
Faculty of Information technology, Brno University of Technology.

### Example

```python
from warcreader import WarcFile
from gzip import GzipFile

warc_gzip = GzipFile('/path/to/warc/file')
warc_file = WarcFile(warc_gzip)
for webpage in warc_file:
	print(webpage.uri)
```

## TODO

- add more detailed documentation to this README
- add comparison to other solutions to this README
- publish on pip
