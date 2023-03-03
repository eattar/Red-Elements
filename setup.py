from setuptools import setup
from setuptools import find_packages

setup(
    name='red-elements',
    version='1.0.0',
    description='This package scrapes red underlined elements from a specific URL.',
    author='Ehsan Attar',
    author_email='ehsanattar@gmail.com',
    packages=find_packages(exclude='test'),
    install_requires=[
        'requests~=2.27.1',
        'lxml~=4.8.0'],
    entry_points={
        'console_scripts': [
            'red-elements-cli=elements_scraper.main:main']
    }
)
