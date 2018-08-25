from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='fizzbuzz',
      version='0.1',
      description='A simple implementation of the FizzBuzz excercise',
      url='http://github.com/morrieinmaas/fizzbuzz',
      author='Moritz Schlichting',
      author_email='2718281@protonmail.ch',
      license='GPLv3',
      install_requires=['argparse'],
      packages=find_packages(exclude=['tests*']),
      entry_points = {
        'console_scripts': ['fizzbuzz = fizzbuzz.fizzbuzz:main'],
    },
      zip_safe=False)
