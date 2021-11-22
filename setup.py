# -*- coding: utf-8 -*-

import setuptools

with open('README.md', 'r',) as f:
    readme = f.read()

setuptools.setup(
    name = 'renderapi',
    packages = ['renderapi'],
    version = '0.9',
    description = 'render.com API wrapper',
    long_description_content_type="text/markdown",
    long_description=readme,
    author = 'bojan',
    author_email = '',
    license='MIT',
    url = 'https://github.com/abrihter/renderapi/releases',
    download_url = 'https://github.com/abrihter/renderapi/archive/v_09.tar.gz',
    keywords = ['RENDER.COM', 'API', 'WRAPPER'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
