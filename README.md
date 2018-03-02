pythonwhois
===========

A WHOIS retrieval and parsing library for Python.

FORK of https://github.com/joepie91/python-whois (re-licensed: WTFPL -> MIT)

## Dependencies

None! All you need is the Python standard library.

## Instructions

From command line with `pwhois example.com` or within your Python app with `pythonwhois.get_whois('example.com')`

## Important update notes

*2.5.0 and up*: Fixed parsing of .ca, .io, .kr, .nz WHOIS responses. APIs support for `timeout` argument to specify a timeout in seconds (float). Several other fixes - see commit log.

*older*: See https://github.com/joepie91/python-whois
