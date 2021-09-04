from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'URL Shortener from python'
LONG_DESCRIPTION = 'URL Shortener which shortens url directly from your python code. An api for lnk.gdn which is also made by me! All made via requests.'

setup(
    name="pyshortener",
    version=VERSION,
    author="JustAnotherCoder",
    author_email="<alexthegreatmatei@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'requests', 'url shortener', 'url', 'website', 'shortener', 'short', 'request', 'api', 'flask'],
    classifiers=[
        "Development Status :: 1 - Releasing",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)