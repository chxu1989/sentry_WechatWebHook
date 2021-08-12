#!/usr/bin/env python
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sentry_WechatWebHook",
    version='0.0.4',
    author='ansheng',
    author_email='ianshengme@gmail.com',
    url='https://github.com/chxu1989/sentry_WechatWebHook',
    description='A Sentry extension which send errors stats to WechatWebHook',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords='sentry WechatWebHook',
    include_package_data=True,
    zip_safe=False,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'sentry>=9.0.0',
        'requests',
    ],
    entry_points={
        'sentry.plugins': [
            'sentry_WechatWebHook = sentry_WebHook.plugin:WechatWebHookPlugin'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
        "License :: OSI Approved :: MIT License",
    ]
)
