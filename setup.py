from setuptools import setup, find_packages

setup(
    name='birb_flask_auth0',
    version='0.7',
    py_modules=['birb_flask_auth0'],
    packages=find_packages(),
    install_requires=[
        'Flask==1.1.2'
    ]
)