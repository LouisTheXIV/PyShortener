from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'URL Shortener from python'
LONG_DESCRIPTION = 'URL Shortener which shortens a url directly from your python code. An api for lnk.gdn which is also made by me! All made via requests.'

setup(
    name="pyshortener",
    version=VERSION,
    author="JustAnotherCoder",
    author_email="<alexthegreatmatei@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'requests', 'url shortener', 'url', 'website', 'shortener', 'short', 'request', 'api', 'flask'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)