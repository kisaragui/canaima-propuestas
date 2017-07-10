#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="canaima-propuestas",
    packages=find_packages(include=['canaima_propuestas']),
    version="1.0.0",
    install_requires=[
        "django == 1.9.9",
        "Pillow == 3.4.2",
        "Pygments == 2.1.3",
        "argparse == 1.2.1",
        "django-registration-redux == 1.4",
        "django-simple-captcha == 0.5.3",
        "djangorestframework == 3.5.3",
        "gunicorn == 19.6.0",
        "six == 1.10.0",
        "wsgiref == 0.1.2"
    ],
    zip_safe=False,
    include_package_data=True,
    license='GPL3 License',
    description='Sistema de postulacion de paquetes.',
    url='http://gitlab.canaima.softwarelibre.gob.ve/canaima-gnu-linux/canaima-propuestas.git',
    author='Noel Alvarez',
    author_email='nalvarez@cnti.gob.ve',
)