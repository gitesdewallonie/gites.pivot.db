from setuptools import setup, find_packages

version = '0.1'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(
    name='gites.pivot.db',
    version=version,
    description="Pivot db connexion for GDW",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
    ],
    keywords='Plone SQLAlchemy',
    author='Affinitic',
    author_email='support@lists.affinitic.be',
    url='https://github.com/gitesdewallonie/',
    license='GPL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['gites', 'gites.pivot'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'beautifulsoup4',
        'gites.db',
        'mysql-python',
        'paramiko',
        'setuptools',
    ],
    extras_require={
        'test': [
            'affinitic.testing',
            'gocept.testdb',
            'plone.app.testing',
        ],
    },
    entry_points={
        'console_scripts': [
            'create_views = gites.pivot.db.scripts.create_views:main',
            'get_archive = gites.pivot.db.scripts.archive:main',
        ]}
)
