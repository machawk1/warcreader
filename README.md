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

## Benchmarks

### Testing setup

Tested on Intel(R) Xeon(R) CPU E5-2630 0 @ 2.30GHz only using one core. Data were are stored on a disk array containing 12 4TB hard drives in RAID 6 and SSD cache. 

### Test script 

```python
from warcreader import WarcFile
from gzip import GzipFile
from sys import argv

if __name__ == '__main__':
    with GzipFile(argv[1], mode='rb') as gzip_file:
        warc_file = WarcFile(gzip_file)
        for webpage in warc_file:
            print(webpage.uri)
```

### Commoncrawl (CC-2015-48)

| File name                                     | File size    | Time Python 2.7  | Time Python 3 |
|-----------------------------------------------|--------------|------------------|---------------|
| 1448398444047.40_20151124205404-00010-warc.gz | 861MB        | 2m2.715s         | 3m43.404s     |
| 1448398444047.40_20151124205404-00021-warc.gz | 873MB        | 2m8.732s         | 3m59.925s     |
| 1448398444047.40_20151124205404-00032-warc.gz | 880MB        | 2m7.905s         | 4m26.469s     | 
| 1448398444047.40_20151124205404-00043-warc.gz | 880MB        | 2m3.966s         | 3m50.878s     |
| 1448398444047.40_20151124205404-00054-warc.gz | 870MB        | 2m13.064s        | 4m10.171s     |


### Clueweb9

| File name                                     | File size    | Time Python 2.7  | Time Python 3 |
|-----------------------------------------------|--------------|------------------|---------------|
| cw_en0035_27.warc.gz                          | 161MB        | 0m37.090s        | 0m43.223s     |
| cw_en0035_32.warc.gz                          | 151MB        | 0m27.869s        | 0m31.620s     |
| cw_en0035_37.warc.gz                          | 153MB        | 0m30.470s        | 0m33.357s     | 
| cw_en0035_42.warc.gz                          | 155MB        | 0m32.795s        | 0m35.594s     |
| cw_en0035_47.warc.gz                          | 138MB        | 0m29.109s        | 0m32.739s     |
