# -*- coding: utf8 -*-

from setuptools import setup

version = '1.0.0'

setup(
    name = 'django-gitana',
    version = version,
    author = 'Sven Aßmann',
    author_email='sven.assmann@lubico.biz',
    description = "Git repository management app for django",
    keywords = 'git django vcs repository-management git-web git-ssh',
    url='http://lubico.biz',
    license='LICENSE.txt',
    packages = ['django_gitana'],
    long_description = open('README.txt').read(),
    install_requires=[
        "Django >= 1.4.1",
    ],
)
