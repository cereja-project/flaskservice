import setuptools

import flaskservice

with open("README.md", "r") as fh:
    long_description = fh.read()

EXCLUDE_FROM_PACKAGES = ()

setuptools.setup(
        name="flaskservice",
        version=flaskservice.__version__,
        author="Joab Leite",
        author_email="jlsn1@ifal.edu.br",
        description="Quick start web services",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/jlsneto/flaskservice",
        packages=setuptools.find_packages(exclude=EXCLUDE_FROM_PACKAGES),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
)