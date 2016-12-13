#!/usr/bin/env python
# -*- coding: utf-8 -*-

import versiontools_support
from setuptools import setup, find_packages

setup(
    name = 'taiga-contrib-mailjet-subscription',
    version = ':versiontools:taiga_contrib_mailjet_subscription:',
    description = 'Plugin to subscribe and unsubscribe users to the newsletter in Mailjet.',
    long_description = 'Plugin to subscribe and unsubscribe users to the newsletter in Mailjet.',
    keywords = 'taiga, mailjet, integration',
    author = 'Taiga Agile LLC',
    author_email = 'taiga@taiga.io',
    url = 'https://github.com/taigaio/taiga-contrib-mailjet-subscription',
    license = 'AGPL',
    include_package_data = True,
    packages = find_packages(),
    install_requires=[
        "mailjet_rest == 1.2.2"
    ],
    setup_requires = [
        'versiontools >= 1.9',
    ],
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
