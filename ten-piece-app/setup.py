# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="ten_piece",
    version="1.0.0", 
    description="A sample Python project",
    long_description=long_description, 
    long_description_content_type="text/markdown",
    url="https://github.com/catie/ten-piece", 
    author="Catie Donnelly",
    package_dir={"": "src"}, 
    packages=find_packages(where="src"),
    python_requires=">=3.9, <4",
    install_requires=[
        "requests",
        "boto3",
        "pydantic",
        "aws_lambda_powertools"
    ], 
    extras_require={
        "dev": ["check-manifest"],
        "test": ["coverage", "moto"],
    }
)
