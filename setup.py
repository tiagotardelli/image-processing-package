from setuptools import setup, find_packages

with open("READNE.md", "r") as file:
    page_description = file.read()

with open("requeriments.txt") as file:
    requeriments = fiel.read().splitlines()

setup(
    name="image_processing_tt",
    version="0.0.1",
    author="Tiago Tardelli",
    author_email="tiagob.tardelli@gmail.com",
    description="Pacote teste para aprendizado",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=requeriments,
    python_requires='>=3.12',
)