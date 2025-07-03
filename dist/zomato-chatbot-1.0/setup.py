from setuptools import setup, find_packages

setup(
    name="zomato-chatbot",
    version="1.0",
    author='Aydie',
    author_email='business@aydie.in',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)