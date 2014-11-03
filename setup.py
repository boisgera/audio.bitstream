#!/usr/bin/env python
# coding: utf-8

# Python 2.7 Standard Library
pass

# Third-Party Libraries
try:
    import setuptools
except ImportError:
    error = "pip is not installed, refer to <{url}> for instructions."
    raise ImportError(error.format(url="http://pip.readthedocs.org"))


info = dict(
  metadata     = dict(name="audio.bitstream"),
  code         = dict(packages=setuptools.find_packages()),
  data         = {},
  requirements = dict(install_requires="bitstream"),
  scripts      = {},
  commands     = {},
  plugins      = {},
  tests        = {},
)


if __name__ == "__main__":
    kwargs = {k:v for dct in info.values() for (k,v) in dct.items()}
    setuptools.setup(**kwargs)

