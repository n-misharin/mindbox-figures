from setuptools import setup, find_packages


def readme() -> str:
    with open("readme.md", "r") as file:
        return file.read()


setup(
    name="mindbox-figures",
    version="0.0.1",
    author="misharin.nd",
    author_email="misharinnikita@gmail.com",
    description="Тестовое задание",
    long_description=readme(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requirements=[],
    classifiers=[
        "Programming Language :: Python :: 3.9.5",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6'
)
