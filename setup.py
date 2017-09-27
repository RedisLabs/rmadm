from setuptools import setup, find_packages

setup(
    name='rmadm',
    version='0.1.2',
    description='Command-line control tool for redis modules Redis Labs Enterprise Cluster',
    author='RedisLabs',
    url='https://github.com/redislabs/rmadm',
    scripts=['rmadm/rmadm'],
    license='BSD 2-clause',
    packages=find_packages(),
    install_requires=['click', 'requests>=2.4.2', 'colorama']
)
