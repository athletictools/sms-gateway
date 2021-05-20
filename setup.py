import os

from setuptools import find_packages, setup


setup(
    name='sms',
    version='0.1.0',
    author='Athletic tools',
    description='SMS sms service',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'sms=sms.cli:cli',
        ],
    },
)
