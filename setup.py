#! /usr/bin/env python
from setuptools import setup

setup(
    name='markdown-lightbox',
    version='1.0.0',
    author='Alicia Schep',
    author_email='aschep@gmail.com',
    description='Markdown extension which turns images into lightbox',
    url='https://github.com/AliciaSchep/markdown-lightbox',
    py_modules=['mdlightbox'],
    install_requires=['Markdown>=3.0'],
    classifiers=[
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
