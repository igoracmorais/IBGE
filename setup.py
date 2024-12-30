from setuptools import setup, find_packages

setup(
    name="pnadcibge",
    version="0.1.0",
    description="Ferramentas para manipulação de dados da PNAD Contínua no Python",
    author="Seu Nome",
    author_email="seuemail@exemplo.com",
    url="https://github.com/igoracmorais/IBGE",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "requests",
        "pyreadstat",  # Necessário para ler os arquivos do IBGE
        "zipfile36",   # Caso esteja lidando com arquivos zip
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
