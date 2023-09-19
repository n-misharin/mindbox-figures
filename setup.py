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
    url="https://github.com/n-misharin/mindbox-figures",
    long_description=readme(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requirements=[],
    classifiers=[
        "Programming Language :: Python :: 3.9.5",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    project_urls={
        "GitHub": "https://github.com/n-misharin/mindbox-figures"
    },
    python_requires='>=3.6'
)
