# GIVEPASS

GIVEPASS is a Python script for storing dummy accounts credentials. The script can be executed from the command line. Credentials are stored in an external file(passwd.txt.aes) encrypted with AES256 with [pyAesCrypt](https://pypi.org/project/pyAesCrypt/)

**DON'T USE THIS TO STORE REAL CREDENTIALS! THIS SCRIPT IS NOT A SECURE WAY TO STORE YOUR CREDENTIALS!**

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```
