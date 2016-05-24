import os
from setuptools import find_packages, setup
from ggplot.__init__ import __version__



setup(
    name="ggplot",
    # Increase the version in ggplot/__init__.py
    version=__version__,
    author="Greg Lamp",
    author_email="greg@yhathq.com",
    url="https://github.com/yhat/ggplot/",
    license="BSD",
    packages=find_packages(),
    package_dir={"ggplot": "ggplot"},
    package_data={"ggplot": ["datasets/*.csv"]},
    description="ggplot for python",
    # run pandoc --from=markdown --to=rst --output=README.rst README.md
    long_description=open("README.rst").read(),
    install_requires=[
        "six",
        "statsmodels",
        "brewer2mpl",
        "matplotlib",
        "scipy",
        "patsy>=0.4",
        "pandas",
        "cycler",
        "numpy"
    ],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3'
    ],
    zip_safe=False
)
