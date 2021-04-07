from string import Template
import argparse

parser = argparse.ArgumentParser(description="Passgen builder")
parser.add_argument('language', type=str, choices=['python', 'bash', 'c', 'swift', 'dart'], help="number of words in the password")
args = parser.parse_args()


def create_python_script(words):
    d = {'words': "'" + "', '".join(words) + "'"}

    with open('Templates/passgen.py') as infile:
        src = Template(infile.read())

    with open('Generators/passgen.py', 'w') as outfile:
        outfile.write(src.safe_substitute(d))


def create_bash_script(words):
    d = {'words': " ".join(words)}

    with open('Templates/passgen.sh') as infile:
        src = Template(infile.read())

    with open('Generators/passgen.sh', 'w', newline='\n') as outfile:
        outfile.write(src.safe_substitute(d))


def create_c_script(words):
    max_len = max([len(word) for word in words])
    d = {'words': '"' + '", "'.join(words) + '"', 'num_words': len(words), 'max_len': max_len}

    with open('Templates/passgen.c') as infile:
        src = Template(infile.read())

    with open('temp/passgen.c', 'w', newline='\n') as outfile:
        outfile.write(src.safe_substitute(d))


def create_swift_script(words):
    d = {'words': '"' + '", "'.join(words) + '"'}

    with open('Templates/passgen.swift') as infile:
        src = Template(infile.read())

    with open('Generators/passgen.swift', 'w') as outfile:
        outfile.write(src.safe_substitute(d))


def create_dart_script(words):
    d = {'words': "'" + "', '".join(words) + "'"}

    with open('Templates/passgen.dart') as infile:
        src = Template(infile.read())

    with open('Generators/passgen.dart', 'w') as outfile:
        outfile.write(src.safe_substitute(d))


creators = {'python': create_python_script, 'bash': create_bash_script, 'c': create_c_script, 'swift': create_swift_script, 'dart': create_dart_script}

with open('words.txt') as infile:
    words = infile.read().split('\n')

creators[args.language](words)
