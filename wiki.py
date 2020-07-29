import pkg_resources
import re
import subprocess
import sys
import os
import argparse
import random


def search_wikipedia(arguments):

    import wikipedia
    wikipedia.set_lang("pt")

    try:
        os.system("clear")
        print("\033[35mPesquisando a palavra/frase na Wikipedia...\033[m\n")
        result = wikipedia.summary(arguments.pesquisa)
        print("\n\n"+"\033[33m"+result+"\033[m")

    except wikipedia.exceptions.PageError:
        print("\033[31mNão há pesquisa correspondente na Wikipedia\033[m")

    except wikipedia.exceptions.DisambiguationError:

        os.system("clear")
        pages = wikipedia.search(arguments.pesquisa)

        print(f'{arguments.pesquisa} pode se referir a: ')

        for i, topic in enumerate(pages):
            print(i, topic)

        choice = int(input("Enter a choice: "))
        assert choice in range(len(pages))

        result = wikipedia.summary(pages[choice])
        print("\n\n"+"\033[33m"+result+"\033[m")


def verification_module_wikipedia():

    try:
        pkg_resources.get_distribution("wikipedia")

    except pkg_resources.DistributionNotFound:
        print("\033[31minstalando modulo wikipedia\033[m")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "wikipedia"])

        # reparo temporario ate atualizacao no modulo estar disponivel no Pypl
        os.system(
            "python3 -m pip install --upgrade git+git://github.com/goldsmith/Wikipedia.git")


def configure_agparse():
    parser = argparse.ArgumentParser(
        description="Um programa de pesquisa na Wikipedia pelo terminal")
    parser.add_argument('-s', action='store', dest='pesquisa',
                        required='True', help='O que deseja pesquisar')

    return parser.parse_args()


def main():
    arguments = configure_agparse()
    verification_module_wikipedia()
    search_wikipedia(arguments)


if __name__ == '__main__':
    main()
