#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from pybase64 import standard_b64decode, standard_b64encode

def TestOneInput(data):
    encoded = standard_b64encode(data)
    decoded = standard_b64decode(encoded)

    if decoded != data:
        raise AssertionError("Decoded data doesn't match input data")

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()