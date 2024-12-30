{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPIgQQ/lOYy4B3cuRrFBXM2",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/igoracmorais/IBGE/blob/main/setup.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "9OkHv3nGY8PF"
      },
      "outputs": [],
      "source": [
        "# Arquivo de configuração para transformar o projeto em um pacote instalável.\n",
        "\n",
        "from setuptools import setup, find_packages\n",
        "\n",
        "setup(\n",
        "    name=\"pnadcibge\",\n",
        "    version=\"0.1.0\",\n",
        "    description=\"Ferramentas para manipulação de dados da PNAD Contínua no Python\",\n",
        "    author=\"Seu Nome\",\n",
        "    author_email=\"seuemail@exemplo.com\",\n",
        "    packages=find_packages(),\n",
        "    install_requires=[\n",
        "        \"pandas\",\n",
        "        \"requests\",\n",
        "    ],\n",
        "    classifiers=[\n",
        "        \"Programming Language :: Python :: 3\",\n",
        "        \"License :: OSI Approved :: MIT License\",\n",
        "        \"Operating System :: OS Independent\",\n",
        "    ],\n",
        "    python_requires='>=3.6',\n",
        ")"
      ]
    }
  ]
}