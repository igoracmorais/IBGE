{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOiwip+n/fYZ+xRVyyDNczK",
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
        "<a href=\"https://colab.research.google.com/github/igoracmorais/IBGE/blob/main/read.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "lSkXULdpYKrG"
      },
      "outputs": [],
      "source": [
        "# Funções para carregar os dados TXT.\n",
        "\n",
        "import pandas as pd\n",
        "\n",
        "def load_pnadc_txt(txt_file_path, dictionary_file_path):\n",
        "    \"\"\"Carrega os dados da PNAD Contínua a partir de um arquivo TXT.\"\"\"\n",
        "    columns = []\n",
        "    widths = []\n",
        "    with open(dictionary_file_path, 'r', encoding='latin1') as dict_file:\n",
        "        for line in dict_file:\n",
        "            parts = line.strip().split()\n",
        "            if len(parts) >= 3:\n",
        "                columns.append(parts[0])\n",
        "                start_pos = int(parts[1])\n",
        "                end_pos = int(parts[2])\n",
        "                widths.append(end_pos - start_pos + 1)\n",
        "    return pd.read_fwf(txt_file_path, widths=widths, names=columns, encoding='latin1')"
      ]
    }
  ]
}