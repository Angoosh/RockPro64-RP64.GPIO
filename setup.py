import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RP64.GPIO",
    version="0.0.3",
    author="Angoosh",
    author_email="angoosh3d@gmail.com.com",
    description="RockPro64 GPIO package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Angoosh/RockPro64-RP64.GPIO",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.5+",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
)
