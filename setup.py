import setuptools

setuptools.setup(
    name='extraction_tutorial',
    version='0.1',
    author='Will Larson',
    author_email='lethain@gmail.com',
    packages=['extraction_tutorial'],
    url='https://github.com/lethain/extraction_tutorial/',
    license='LICENSE.txt',
    description='Tutorial for using extraction library with graphql',
    long_description=open('README.md').read(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
