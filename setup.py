import codecs
import os.path
import re
import sys

from setuptools import setup, find_packages


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


requires = []


setup_options = dict(
    name='task_orchestrator',
    version=find_version("task_orchestrator", "__init__.py"),
    description='Task orchestrator API',
    long_description=open('README.md').read(),
    author='Jefferson Stachelski',
    url='',
    packages=find_packages(exclude=['tests*']),
    package_data={'task_orchestrator': []},
    install_requires=requires,
    extras_require={},
    license="MIT",
    classifiers=[],
)


setup(**setup_options)
