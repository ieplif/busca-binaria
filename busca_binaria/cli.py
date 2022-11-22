from busca_binaria import busca_binaria
from busca_binaria import busca_binaria
from argparse import ArgumentParser

parser = ArgumentParser(prog='Busca Binária',
                        usage='Busca Binária [arg]',
                        description="""
                        Insira uma lista e o item a ser procurado""",
                        epilog='A eficiência do algoritmo é O(log2n)',
                        fromfile_prefix_chars='@')


parser.print_help()

parser.add_argument('lista', help='Lista da busca', type=int)
parser.add_argument('i', help='Item procurado', type=int)


args = parser.parse_args()



    