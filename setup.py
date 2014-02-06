from setuptools import setup, find_packages

setup( name='economica',
    version = '0.0.1',
    description = 'Economica for Django',
    author = 'Daryl Antony',
    author_email = 'daryl@commoncode.com.au',
    url = 'https://github.com/commoncode/economica',
    keywords = ['django',],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    dependency_links = [
        'http://github.com/commoncode/entropy/tarball/master#egg=django-entropy',
        'http://github.com/commoncode/rea/tarball/master#egg=rea',
    ],
    setup_requires = [
        'pip',
    ],
    install_requires = [
        'django-entropy',
        'rea',
    ],
)