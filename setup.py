#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import os

version='0.2.0'
package = 'cropper'

path = os.path.join(os.path.dirname(__file__), 'cropper')
setuptools.setup(
    name = 'django-image-cropper',
    version = version,
    author  = 'marazmiki',
    author_email = 'marazmiki@gmail.com',
    url = 'https://github.com/Jyggafey/django-image-cropper/',
    download_url = 'https://github.com/Jyggafey/django-image-cropper/archive/master.zip',

    description = 'This app allows upload and crop images',
    long_description = open('README.rst').read(),
    license = 'MIT license',
    install_requires = ['django>=1.3.1', 'Pillow'],
    packages = setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
