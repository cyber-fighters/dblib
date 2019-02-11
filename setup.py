import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dblib",
    version="1.0.0",
    author="Andreas Maier",
    author_email="andbotATgmx.de",
    description="Support package to manage interaction with databases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyber-fighters/dblib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests>=2.21.0"
    ],
)
