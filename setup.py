#encoding:utf-8
from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='mdzz',
      version=version,
      description="终端英译汉工具",
      classifiers=[], 
      keywords='python mdzz dictionary terminal',
      author='NewBee',
      author_email='liu392285478@gmail.com',
      url='https://github.com/newbee-7/mdzz',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'termcolor',
      ],
      entry_points={
        'console_scripts':[
            'mdzz = mdzz.mdzz:main'
        ]
      },
)
