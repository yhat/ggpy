import os
from setuptools import find_packages, setup


def get_package_data():
    ''' Find all additional package data to distribute with code. '''

    baseline_images = ['tests/baseline_images/%s/*' % x
                       for x in os.listdir('ggplot/tests/baseline_images')]

    return {'ggplot': baseline_images + ["exampledata/*.csv", "geoms/*.png"]}


def get_readme():
    ''' Retrieve README.rst's content in a safe way. '''
    with open('README.rst') as f:
        return f.read()


setup(name="ggplot",
      version="0.3.0",
      author="Greg Lamp",
      author_email="greg@yhathq.com",
      url="https://github.com/yhat/ggplot/",
      license="BSD",
      packages=find_packages(),
      package_dir={"ggplot": "ggplot"},
      package_data=get_package_data(),
      description="ggplot for python",
      long_description=get_readme(),
      install_requires=["pandas", "matplotlib", "scipy", "statsmodels",
                        "patsy"],
      classifiers=['Intended Audience :: Science/Research',
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
                   'Programming Language :: Python :: 3.3'],
      zip_safe=False)
