# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import GovtjobApp


setup(
    name='GovtJobApp',
    version=app.__version__,
    description='',
    author='Jakub Janoszek',
    author_email='kuba.janoszek@gmail.com',
    include_package_data=True,
    url='https://github.com/theshivamrathore/django-cms/tree/ver-%s' % app.__version__,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)

# Usage of setup.py:
# $> python setup.py register             # registering package on PYPI
# $> python setup.py build sdist upload   # build, make source dist and upload to PYPI
