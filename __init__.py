{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOD2+xO6SCsLq5aK4OMsOV8",
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
        "<a href=\"https://colab.research.google.com/github/igoracmorais/IBGE/blob/main/__init__.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "rvoCvutGWFxz"
      },
      "outputs": [],
      "source": [
        "\"\"\"PNADcIBGE: Ferramentas para manipular dados da PNAD Contínua no Python.\"\"\"\n",
        "from .download import download_pnadc, extract_zip\n",
        "from .read import load_pnadc_txt\n",
        "from .process import label_variables, calculate_unemployment_rate\n",
        "\n",
        "__all__ = [\"download_pnadc\", \"extract_zip\", \"load_pnadc_txt\", \"label_variables\", \"calculate_unemployment_rate\"]"
      ]
    }
  ]
}