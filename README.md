# PyShortener
WIP! Do not use yet
PyShortener is a python 3 package for shortening a url directly from python

# Installation
`pip install pyshortener` or `python -m pip install pyshortener`

# Usage & Documentation
Documentation is at: https://pyshortener.readthedocs.io/en/latest/

##### Usage:
    ```
    from pyshortener import *

    url_obj = shorten(url="https://youtube.com")

    print(url_obj.link())
    print(url_obj.code())
    print(url_obj.html())
    print(url_obj.status_code)
    ```
