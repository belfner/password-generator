from string import Template
import argparse
import os

parser = argparse.ArgumentParser(description="Passgen builder")
parser.add_argument('language', type=str, choices=['python', 'bash', 'c', 'swift', 'dart', 'java', 'powershell', 'php', 'ruby'], help="number of words in the password")
args = parser.parse_args()

try:
    os.mkdir('build')
except FileExistsError:
    pass

try:
    os.mkdir('temp')
except FileExistsError:
    pass


def create_python_script(words):
    d = {'words': "'" + "', '".join(words) + "'"}

    with open('templates/passgen.py') as infile:
        src = Template(infile.read())

    with open('build/passgen.py', 'w') as outfile:
        outfile.write(src.safe_substitute(d))


def create_bash_script(words):
    d = {'words': " ".join(words)}

    with open('templates/passgen.sh') as infile:
        src = Template(infile.read())

    with open('build/passgen.sh', 'w', newline='\n') as outfile:
        outfile.write(src.safe_substitute(d))


def create_c_script(words):
    max_len = max([len(word) for word in words]) + 1
    d = {'words': '"' + '", "'.join(words) + '"', 'num_words': len(words), 'max_len': max_len}

    with open('templates/passgen.c') as infile:
        src = Template(infile.read())

    with open('temp/passgen.c', 'w') as outfile:
        outfile.write(src.safe_substitute(d))


def create_swift_script(words):
    d = {'words': '"' + '", "'.join(words) + '"'}

    with open('templates/passgen.swift') as infile:
        src = Template(infile.read())

    with open('build/passgen.swift', 'w') as outfile:
        outfile.write(src.safe_substitute(d))


def create_dart_script(words):
    d = {'words': "'" + "', '".join(words) + "'"}

    with open('templates/passgen.dart') as infile:
        src = Template(infile.read())

    with open('build/passgen.dart', 'w') as outfile:
        outfile.write(src.safe_substitute(d))


def create_java_script(words):
    d = {'words': '"' + '", "'.join(words) + '"'}

    with open('templates/Passgen.java') as infile:
        src = Template(infile.read())

    with open('temp/Passgen.java', 'w') as outfile:
        outfile.write(src.safe_substitute(d))


def create_powershell_script(words):
    d = {'words': "'" + "', '".join(words) + "'"}

    with open('templates/passgen.ps1') as infile:
        src = Template(infile.read())

    with open('build/passgen.ps1', 'w') as outfile:
        outfile.write(src.safe_substitute(d))


def create_php_script(words):
    d = {'words': '"' + '", "'.join(words) + '"'}

    with open('templates/passgen.php') as infile:
        src = Template(infile.read())

    with open('build/passgen.php', 'w') as outfile:
        outfile.write(src.safe_substitute(d))


def create_ruby_script(words):
    d = {'words': '"' + '", "'.join(words) + '"'}

    with open('templates/passgen.rb') as infile:
        src = Template(infile.read())

    with open('build/passgen.rb', 'w') as outfile:
        outfile.write(src.safe_substitute(d))


creators = {'python': create_python_script,
            'bash': create_bash_script,
            'c': create_c_script,
            'swift': create_swift_script,
            'dart': create_dart_script,
            'java': create_java_script,
            'powershell': create_powershell_script,
            'php': create_php_script,
            'ruby': create_ruby_script}
with open('words.txt') as infile:
    words = infile.read().split('\n')

creators[args.language](words)
