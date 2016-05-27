import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='ShipEasy, built using flask-adminLTE',
    version='2.0.6',
    url='http://github.com/shipEZ/flask-admin',
    license='BSD',
    author='sachinbhat.as@gmail.com',
    author_email='sachinbhat.as@gmail.com',
    description='An extension that includes AdminLTE in the project.',
    long_description=read('README.rst'),
    packages=['flask_adminlte'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.8',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
