from setuptools import setup, find_packages

setup(
    name='flask_auth0',
    version='',
    package_dir={'flask_auth0': 'src'},
    packages=find_packages(),
    install_requires=[
        'Flask==1.1.2'
    ]
)