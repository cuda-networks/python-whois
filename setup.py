from setuptools import setup

setup(name='pythonwhois-bn',
      version='2.5.0',
      description='Module for retrieving and parsing the WHOIS data for a domain. Supports most domains. No dependencies.',
      author='Barracuda Networks',
      url='https://github.com/cuda-networks/python-whois',
      packages=['pythonwhois'],
      package_dir={"pythonwhois":"pythonwhois"},
      package_data={"pythonwhois":["*.dat"]},
      install_requires=['argparse'],
      provides=['pythonwhois'],
      scripts=["pwhois"],
      license="MIT"
     )
