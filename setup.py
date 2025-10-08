"""Setup configuration for the project."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cc_stmt_data_scrubber",
    version="0.1.0",
    author="Belden Schroeder",
    author_email="beldenschroeder@gmail.com",
    description="A tool for scrubbing credit card statement data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/beldenschroeder/cc_stmt_data_scrubber",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "black>=23.7.0",
            "flake8>=6.1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "cc-scrubber=cc_stmt_data_scrubber.main:main",
        ],
    },
)
