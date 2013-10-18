from distutils.core import setup


required = []

setup(
    name="ggplot",
    version="0.2.8",
    author="Greg Lamp",
    author_email="greg@yhathq.com",
    url="https://github.com/yhat/ggplot/",
    license="BSD",
    packages=['ggplot',
              'ggplot.components',
              'ggplot.exampledata',
              'ggplot.geoms',
              'ggplot.scales',
              'ggplot.tests',
              'ggplot.utils',
              ],
    package_data={"ggplot": ["exampledata/*.csv", "geoms/*.png"]},
    description="ggplot for Python",
    # run pandoc --from=markdown --to=rst --output=README.rst README.md
    long_description=open("README.rst").read(),
    install_requires=required,
)

