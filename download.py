{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMRg4Eg3GmWnq00wugcfpZ1",
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
        "<a href=\"https://colab.research.google.com/github/igoracmorais/IBGE/blob/main/download.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "coLfJwVFX1So"
      },
      "outputs": [],
      "source": [
        "import os\n",
        "import requests\n",
        "import zipfile\n",
        "\n",
        "def download_pnadc(year, quarter, download_dir=\"data\"):\n",
        "    \"\"\"Baixa os microdados da PNAD Contínua para um ano e trimestre especificados.\"\"\"\n",
        "    base_url = f'https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Trimestral/Microdados/{year}/'\n",
        "    file_name = f\"PNADC_0{quarter}{year}.zip\"\n",
        "    url = base_url + file_name\n",
        "    os.makedirs(download_dir, exist_ok=True)\n",
        "    output_path = os.path.join(download_dir, file_name)\n",
        "\n",
        "    response = requests.get(url)\n",
        "    if response.status_code == 200:\n",
        "        with open(output_path, \"wb\") as file:\n",
        "            file.write(response.content)\n",
        "        return output_path\n",
        "    else:\n",
        "        raise Exception(f\"Erro ao baixar {file_name}. HTTP Status: {response.status_code}\")\n",
        "\n",
        "def extract_zip(zip_path, extract_dir):\n",
        "    \"\"\"Extrai um arquivo ZIP para um diretório especificado.\"\"\"\n",
        "    with zipfile.ZipFile(zip_path, 'r') as zip_ref:\n",
        "        zip_ref.extractall(extract_dir)\n",
        "    return extract_dir"
      ]
    }
  ]
}