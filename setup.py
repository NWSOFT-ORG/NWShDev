from setuptools import setup
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='NWSh',
    version='0.1.3',
    packages=['NWSh'],
    url='https://www.nwsoft.tk',
    license='GPL',
    author='ZCG-Coder',
    author_email='andy@nwsoft.tk',
    description='A little library for the NWSh development',
    install_requires=[
        'prompt_toolkit',
        'json5rw',
    ],
    data_files=[('NWSh/resources', ['NWSh/resources/settings.json'])],
    include_dirs=['NWSh/resources'],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown'
)
