"""redditcleaner - setup.py"""
import setuptools

LONG_DESC = open('README.md').read()

setuptools.setup(
    name="redditcleaner",
    version="1.1.2",
    author="Lorenz Leitner",
    author_email="lrnz.ltnr@gmail.com",
    description="Clean Reddit Text Data",
    long_description_content_type="text/markdown",
    long_description=LONG_DESC,
    url="https://github.com/lolei/redditcleaner",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
    )
