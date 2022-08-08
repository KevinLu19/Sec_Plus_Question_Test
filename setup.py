from setuptools import setup

# install Package via "pip install ."
# python setup.py install

setup(
    name="Sec Plus Question Prompt",
    version="",
    description="Prompts questions for the test.",
    author="Kevin Lu",
    packages=["src"],
    install_requires=["pymongo", "PyPDF2"]
)