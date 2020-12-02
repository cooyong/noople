import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="noople-cherdt", # Replace with your own username
    version="0.0.1",
    author="Chris Herdt",
    author_email="cherdt@gmail.com",
    description="The worst search engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cherdt/noople",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.8',
)
