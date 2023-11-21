import re
import sys

from tqdm import tqdm

sys.path.extend(['.', '..'])

from pycparser import c_parser, c_generator
from . import helper


# strip WhiteSpace
def remove_spaces(code):
    return ''.join(code.text.split())


# strip include from code file using RE
def remove_includes(code):
    # match include , replace with space
    return re.sub('#include[ ]*(<.*>|".*")', ' ', code, re.S)


# strip comment from file using RE
def remove_comments(code):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " "
        else:
            return s

    pattern = re.compile(r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"', re.DOTALL | re.MULTILINE)

    return re.sub(pattern, replacer, code)


def filter(code):
    filtered_code = remove_comments(code)
    filtered_code = remove_includes(filtered_code)

    return filtered_code


def filter_code_dict(code_dict):
    filtered_code_dict = {}
    for key, code in code_dict.items():
        filtered_code_dict[key] = filter(code)

    return filtered_code_dict


# @TODO This func need refactor, every time make obj
def regenerate_code(code):
    """
    This function generates c code from c code
    the only purpose is reshape the code
    """
    parser = c_parser.CParser()
    generator = c_generator.CGenerator()

    ast = parser.parse(code, filename='<none>')
    generated_code = generator.visit(ast)

    return generated_code


def reformat_c_code(code):
    # @TODO Code style is bad, and the code must tested
    return regenerate_code(code).replace('&', '& ').replace(';', ' ;').replace(',', ' ,').replace('(', ' ( ').replace(
        ')', ' )').replace('[', ' [ ').replace(']', ' ]').replace('++', ' ++').replace('--', ' --')


def c_code_keyword_list(c_code):
    c_32_keywords_count = {'enum': 0, 'extern': 0, 'float': 0, 'for': 0,
                           'goto': 0, 'if': 0, 'int': 0, 'long': 0, 'register': 0, 'return': 0,
                           'short': 0, 'signed': 0, 'sizeof': 0, 'static': 0, 'struct': 0, 'switch': 0,
                           'typedef': 0, 'union': 0, 'unsigned': 0, 'void': 0, 'volatile': 0, 'while': 0}

    tokens = c_code.split()
    keyword_list = []

    for token in tokens:
        if token in c_32_keywords_count:
            c_32_keywords_count[token] = c_32_keywords_count[token] + 1
            keyword_list.append(token + str(c_32_keywords_count[token]))
    return keyword_list


# @TODO This func need refactor
def jaccard_filter(code_dict):
    jaccard_ready_dict = {}

    # Create a tqdm progress bar with the total number of items
    with tqdm(total=len(code_dict), desc="[+] Applying jaccard filter", unit='file') as pbar:
        for key, code in code_dict.items():
            # @TODO reformat_c_code func is bad
            c_code = reformat_c_code(filter(code))
            jaccard_ready_dict[key] = c_code_keyword_list(c_code)

            # Update the progress bar
            pbar.update(1)

    return jaccard_ready_dict


def generate_abstract_c_code(c_code):
    parser = c_parser.CParser()
    generator = helper.AbstractCGenerator()

    ast = parser.parse(c_code, filename='<none>')
    generated_code = generator.visit(ast)

    return generated_code


def normalize_abstract_c_code(abstract_c_code):
    map = {'ARR': 'A', 'CONST': 'C', 'FUNC': 'F', 'ID': 'I', 'LABLE': 'L', 'STRUCT': 'S',
           'char': 'c', 'const': 'd', 'float': 'f', 'for': 'g', 'int': 'i', 'return': 'r',
           'struct': 's', 'typedef': 't', 'union': 'u', 'void': 'v', 'while': 'w'}

    tokens = abstract_c_code.split()
    maped_tokens = []

    for token in tokens:
        if token in map:
            maped_tokens.append(map[token])
        else:
            maped_tokens.append(token)
    return "".join(maped_tokens)


# @TODO This func need refactor, reformat_c_code() should be in normalize_abstract_c_code()
def lcs_filter(code_dict):
    lcs_ready_dict = {}

    # Create a tqdm progress bar with the total number of items
    with tqdm(total=len(code_dict), desc="[+] Applying lcs filter", unit='file') as pbar:
        for key, code in code_dict.items():
            abstract_c_code = generate_abstract_c_code(filter(code))
            abstract_c_code = reformat_c_code(abstract_c_code)

            lcs_ready_dict[key] = normalize_abstract_c_code(abstract_c_code)

            # Update the progress bar
            pbar.update(1)

    return lcs_ready_dict
