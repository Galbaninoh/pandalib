from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='pandalib',
    version='0.2.1',
    packages=['pandalib'],
    url='https://github.com/Galbaninoh/pandalib',
    author='galbaninoh',
    author_email='galbaninoh@galbaninoh.space',
    description='A python module to interact with the api of the popular agent pandabuy',
    long_description=long_description,
    long_description_content_type='text/markdown'
)