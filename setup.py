from setuptools import setup, find_packages


repositories = [
    'cqrs',
    'entropy',
    'images',
    'rea',
    'rea-serializers'
]

setup(
    name='economica',
    version='0.0.3',
    description='Economica for Django',
    author='Daryl Antony',
    author_email='daryl@commoncode.com.au',
    url='https://github.com/commoncode/economica',
    keywords=['django', 'ecommerce'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    dependency_links=[
        'http://github.com/commoncode/{0}/tarball/master#egg={0}'.format(
            repository
        ) for repository in repositories
    ],
    setup_requires=['pip'],
    install_requires=['Django>=1.7'] + repositories
)
