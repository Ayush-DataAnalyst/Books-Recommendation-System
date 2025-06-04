
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Books-Recommendation-System"
AUTHOR_USER_NAME = "Ayush-DataAnalyst"
SRC_REPO = "books_recommendation_system"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Ayush-DataAnalyst",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ayush-DataAnalyst/Books-Recommendation-System",
    author_email="ayushshimpi02@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.10",
    install_requires=LIST_OF_REQUIREMENTS
)
