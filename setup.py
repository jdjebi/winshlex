import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="winshlex", # Replace with your own username
    version="0.0.1",
    author="Dje Bi Mointi",
    author_email="tidev.99@gmail.com",
    description="Alternative to python shlex package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jdjebi/winshlex",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.3',
)