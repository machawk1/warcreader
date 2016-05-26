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

This library is released under Apache 2.0 licence

## Documentation

### Installation

You can use `pip` or `pip3` utility to install the library:

```
pip install warcreader
```

or you can just download the repository contents and copy the `warcreader` directory
to your project

### WarcFile

`WarcFile` class represents a WARC archieve to be read.

Accepts one parameter on initialization. Its value should be an opened file
containing the WARC archieve. It can be an instance of `file` type created by 
`open()` function or any other file-like object like `gzip.GzipFile` or 
`lzma.LZMAFile` instance.

**The file has to be opened in binary mode** 
(letter 'b' has to be added to the `mode` parameter string)

`WarcFile` instances are iterable. They return next HTTP response as `Webpage` 
instance on each iteration. 

### Webpage

`Webpage` class represents one HTTP respone from WARC archieve. Does not
provide any methods, only the following attributes:

- `uri` - absolute URI of the HTTP response
- `content_type` - value of `Content-Type` field of HTTP header. `None` if this field is not found
- `payload` - contents of the HTTP response like HTML source core of the the web page

### Example

```python
from warcreader import WarcFile
from gzip import GzipFile

warc_gzip = GzipFile('/path/to/warc/file', 'rb')
warc_file = WarcFile(warc_gzip)
for webpage in warc_file:
	print(webpage.uri)
```

## TODO

- make benchmarks
- test on other WARC file sources, not only CommonCrawl
