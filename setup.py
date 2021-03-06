import os
import sys

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

version = '0.2.6'

requires = [
    'pymongo >= 3.6',
    'eduid_am>=0.4.9',
]

testing_extras = [
    'nose==1.2.1',
    'nosexcover==1.0.8',
    'coverage==3.6',
]


setup(
    name='eduid_api_amp',
    version=version,
    description='eduID Sign Up Attribute Manager Plugin',
    long_description=README + '\n\n' + CHANGES,
    # TODO: add classifiers
    classifiers=[
        # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='identity federation saml',
    author='NORDUnet A/S',
    url='https://github.com/SUNET/eduid-api-amp',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    extras_require={
        'testing': testing_extras,
    },
    test_suite='eduid_api_amp',
    entry_points="""\
    [eduid_am.attribute_fetcher]
    eduid_api = eduid_api_amp:attribute_fetcher
    """,
)
