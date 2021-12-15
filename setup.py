from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'This package helps in creating thumbnail for image in a model'
LONG_DESCRIPTION = '''When a django model contains a image field most of the times we 
would want it to have a thumbnail this package helps in creating thumbnail for image in a model'''

# Setting up
setup(
    # the name must match the folder name 'thumbnailerist'
    name="thumbnailerist",
    version=VERSION,
    author="Nitin",
    author_email="",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'Django==3.2.9',
        'Pillow==8.4.0'
    ],  # add any additional packages that
    keywords=['python', 'thumbnail'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
