#!/usr/bin/env python

from distutils.core import setup

VERSION = '1.0.0'
DESCRIPTION = "Django persistent database connection for Postgresql (psycopg2)"
LONG_DESCRIPTION = """
Small custom psycopg2 backend that implements persistent connection using global variable (threadsafe)

http://stackoverflow.com/questions/1125504/django-persistent-database-connection/1351213#1351213
"""

CLASSIFIERS = filter(None, map(str.strip,
"""                 
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Topic :: Database :: Front-Ends
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines()))


setup(
    name="pytimeago",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    author="HardQuestions@Stackoverflow",
    url="http://stackoverflow.com/questions/1125504/django-persistent-database-connection/1351213#1351213",
    license="GPL",
    packages=['postgresql_psycopg2_persistent'],
    platforms=['any'],
)


