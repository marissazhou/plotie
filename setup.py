"""
.. module:: setup
   :synopsis: Installation information for plotie
.. moduleauthor:: Marissa Zhou
"""
# Standard
import re
import os

try:
    from herodotus.describe.egg import version
except ImportError:
    def version():
        pkg_info_version_re = re.compile("\nVersion: ([^\s]*)\n")
        caller_path = os.path.dirname(__file__)
        with open(os.path.join(caller_path, 'PKG-INFO')) as fd:
            match = pkg_info_version_re.search(fd.read())
            if match:
                return match.groups()[0]

from setuptools import setup, find_packages


TESTS_REQUIRE = []
INSTALL_REQUIRES = [
    "plotly",
]


setup(
    name="plotie",
    version=version(),
    packages=find_packages('src'),
    package_dir={"": "src"},
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    entry_points={
        'console_scripts': [
            'mcc = plotie.scripts.plot:main'
        ]
    },
)
