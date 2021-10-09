from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="temperature-reporter",
    version="1.0.1",
    description="A Python package to get temperature of any location.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/narayanasvenkat/temperature-reporter",
    author="Venkat Narayana",
    author_email="narayana.svenkat.cse17@itbhu.ac.in",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["temperature_reporter"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "temperature-reporter=temperature_reporter.cli:main",
        ]
    },
)