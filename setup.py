from setuptools import setup

setup(
   name='snowflake',
   version='1.0',
   description='A useful module',
   author='Siyuan Mei',
   author_email='siyuan.mei@fau.de',
   packages=['snowflake'],  #same as name
   install_requires=['numpy', 'turtles'], #external packages as dependencies
)
