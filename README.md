# WarcReader

WarcReader is as Python library for reading HTTP responses from [Web ARChive 
(WARC) files](https://en.wikipedia.org/wiki/Web_ARChive).

It's main goal is to be as fast as possible, not to provide advanced functions
to work with warc files.

## Authors

Milos Svana (milos.svana(at)gmail.com)

This library was created as a part of my Bachelor's thesis at the
[Knowledge Technology Research Group](http://knot.fit.vutbr.cz/), 
Faculty of Information technology, Brno University of Technology.

### Example

```python
from warcreader import WarcReader

warc_reader = WarcReader("/path/to/warc/file")
for webpage in warc_reader.iterate():
	print(webpage.title)
```

## TODO

- make title extraction optional
- add requirements
- add more detailed documentation to this README
- add comparison to other solutions to this README
- publish on pip
