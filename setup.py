from setuptools import setup
from pkg_resources import parse_requirements

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r',  encoding='utf-8') as f:
    requirements = [x for x in parse_requirements(f.read())]

setup(
    name='py3-utility',
    version='1.0',
    description='A useful module',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='rdgl',
    author_email='',
    license="MIT",
    install_requires=requirements
)
