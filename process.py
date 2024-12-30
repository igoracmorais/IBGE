{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNVDbqEIATrnfnKxadA8JQk",
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
        "<a href=\"https://colab.research.google.com/github/igoracmorais/IBGE/blob/main/process.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "CAm5mZuoYqA1"
      },
      "outputs": [],
      "source": [
        "# Funções de processamento de dados.\n",
        "\n",
        "def label_variables(df, label_dict):\n",
        "    \"\"\"Adiciona rótulos legíveis às variáveis no DataFrame.\"\"\"\n",
        "    return df.rename(columns=label_dict)\n",
        "\n",
        "def calculate_unemployment_rate(df, employed_col, unemployed_col):\n",
        "    \"\"\"Calcula a taxa de desemprego a partir de colunas de empregados e desempregados.\"\"\"\n",
        "    df[\"unemployment_rate\"] = df[unemployed_col] / (df[employed_col] + df[unemployed_col]) * 100\n",
        "    return df"
      ]
    }
  ]
}