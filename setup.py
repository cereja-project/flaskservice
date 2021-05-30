import sys

import setuptools
import subprocess

cmd_ = " ".join(
        [f"{sys.executable}", "-m", "pip", "install", 'cereja']
)

subprocess.run(cmd_, shell=True, stdout=subprocess.PIPE).check_returncode()

from flaskservice import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fr:
    REQUIRED_PACKAGES = fr.read().splitlines()

EXCLUDE_FROM_PACKAGES = ('flaskservice.tests',)

setuptools.setup(
        name="flaskservice",
        version=__version__,
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
        install_requires=REQUIRED_PACKAGES
)
