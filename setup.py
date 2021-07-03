from setuptools import setup, find_packages

setup(
    name='flask_auth0',
    version='0.4',
    py_modules=['flask_auth0'],
    packages=find_packages(),
    install_requires=[
        'Flask==1.1.2'
    ]
)