[![Build Status](https://travis-ci.org/DavidMStraub/pylha.svg?branch=master)](https://travis-ci.org/DavidMStraub/pylha) [![Coverage Status](https://coveralls.io/repos/github/DavidMStraub/pylha/badge.svg?branch=master)](https://coveralls.io/github/DavidMStraub/pylha?branch=master)

# pylha

A Python package to convert data files in SLHA and similar formats to Python objects, JSON, or YAML.


## Motivation

In particle physics phenomenology, structured data like model parameters are frequently exchanged in a file format inspired by the [SUSY Les Houches Accord](https://arxiv.org/abs/0801.0045), for instance

```
Block MODSEL		     # Select model
    1    1		     # sugra
Block MINPAR		     # Input parameters
    1   1.000000000e+02	     # m0
    2   2.500000000e+02	     # m12
    3   1.000000000e+01	     # tanb
    4   1.000000000e+00	     # sign(mu)
    5  -1.000000000e+02	     # A0
```

Other examples include the [FLHA](https://arxiv.org/abs/1008.0762) ("Flavour Les Houches Accord") and the input and outputs files formats of [DSixTools](https://dsixtools.github.io/) and [Rosetta](https://rosetta.hepforge.org/).

While [several well-tested parsers](http://skands.physics.monash.edu/slha/) exist for the original SLHA format, most of these are not robust enough to treat the generalized formats. The purpose of pylha is to provide a simple low-level Python package that allows to import any file in a "LHA-like" format into a Python data structure and export it back to industry-standard exchange formats like JSON or YAML (or back to LHA format).

## Usage

At the moment, pylha can only be used as a Python module (command line scripts might be added later). To install it, use

```
pip3 install pylha
```

The above example string can be converted to a JSON string using

```python
import pylha
d = pylha.load(example_string)
pylha.dump(d, 'json')
```

Which will return

```json
{
  "BLOCK": {
    "MODSEL": {
      "values": [[1, 1]]
    },
    "MINPAR": {
      "values": [[1, 100.0], [2, 250.0], [3, 10.0], [4, 1.0], [5, -100.0]]
    }
  }
}
```
