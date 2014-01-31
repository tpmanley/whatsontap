from setuptools import setup
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

long_description = read('README.md')


setup(
    name='whatsontap',
    version=find_version('whatsontap.py'),
    url='http://github.com/tpmanley/whatsontap/',
    license='Apache Software License',
    author='Tom Manley',
    install_requires=['Flask',
                      'Flask-SQLAlchemy',
                      'SQLAlchemy',
                      'Flask-Restless',
                      ],
    author_email='tom.manley@gmail.com',
    description='Find out what is on tap at your favorite brewery or taproom',
    long_description=long_description,
#    packages=['whatsontap'],
#    package_dir={'whatsontap': 'whatsontap'},
#    package_data={'whatsontap': ['templates/*.html']},
    include_package_data=True,
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
)