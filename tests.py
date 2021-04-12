import unittest
import re
import subprocess
import os


class PassgenTest(unittest.TestCase):
    name = ''
    file = ''
    basic_command = []

    @staticmethod
    def count_words(output):
        r = re.findall('([a-z]+\.)', output)
        return len(r)

    @staticmethod
    def check_structure(output):
        match = re.search(r'((?:[a-z]+\.)+[A-Z][0-9])$', output)
        return True if match else False

    def custom_setup(self):
        pass

    def setUp(self) -> None:
        try:
            os.remove(self.file)
        except FileNotFoundError:
            pass
        subprocess.run(['make', self.name], stdout=subprocess.PIPE)
        self.custom_setup()

    def custom_teardown(self):
        pass

    def tearDown(self):
        self.custom_teardown()

    def check_build(self):
        assert os.path.isfile(self.file)

    def basic(self):
        result = subprocess.Popen(self.basic_command, stdout=subprocess.PIPE)
        result.wait()
        result_text, err = result.communicate()
        result_text = result_text.decode().strip()
        print(result_text)
        # result_text = result.stdout.decode().strip()
        # print(result_text)
        assert self.check_structure(result_text)

    def variable_length(self):
        num_words = 10

        result = subprocess.Popen(self.basic_command + [str(num_words)], stdout=subprocess.PIPE)
        result.wait()
        result_text, err = result.communicate()
        result_text = result_text.decode().strip()
        word_count = PassgenTest.count_words(result_text)
        assert num_words == word_count

        num_words = 1
        result = subprocess.Popen(self.basic_command + [str(num_words)], stdout=subprocess.PIPE)
        result.wait()
        result_text, err = result.communicate()
        result_text = result_text.decode().strip()
        word_count = PassgenTest.count_words(result_text)
        assert num_words == word_count

    def negative_length(self):
        num_words = -1
        result = subprocess.Popen(self.basic_command + [str(num_words)], stdout=subprocess.PIPE)
        result.wait()
        result_text, err = result.communicate()
        result_text = result_text.decode().strip()

        assert result_text == 'Argument must be greater than or equal to 1'

    def invalid_argument(self):
        invalid = 's'
        result = subprocess.Popen(self.basic_command + [invalid], stdout=subprocess.PIPE)
        result.wait()
        result_text, err = result.communicate()
        result_text = result_text.decode().strip()
        assert not PassgenTest.check_structure(result_text)


class Python(PassgenTest):
    name = 'python'
    file = 'build/passgen.py'
    basic_command = ['python', file]

    def test_check_build(self):
        self.check_build()

    def test_basic(self):
        self.basic()

    def test_variable_length(self):
        self.variable_length()

    def test_negative_length(self):
        self.negative_length()

    def test_invalid_argument(self):
        self.invalid_argument()


class Java(PassgenTest):
    name = 'java'
    file = 'Passgen.class'
    basic_command = ['java', 'Passgen']

    def test_check_build(self):
        self.check_build()
    
    def custom_setup(self):
        os.chdir('build')

    def custom_teardown(self):
        os.chdir('..')

    def test_check_build(self):
        self.check_build()

    def test_basic(self):
        self.basic()

    def test_variable_length(self):
        self.variable_length()

    def test_negative_length(self):
        self.negative_length()

    def test_invalid_argument(self):
        self.invalid_argument()


class Powershell(PassgenTest):
    name = 'powershell'
    file = 'build/passgen.ps1'
    basic_command = ['powershell', file]

    def test_check_build(self):
        self.check_build()

    def test_basic(self):
        self.basic()

    def test_variable_length(self):
        self.variable_length()

    def test_negative_length(self):
        self.negative_length()

    def test_invalid_argument(self):
        self.invalid_argument()


class Dart(PassgenTest):
    name = 'dart'
    file = 'build/passgen.dart'
    basic_command = ['dart', file]

    def test_check_build(self):
        self.check_build()

    def test_basic(self):
        self.basic()

    def test_variable_length(self):
        self.variable_length()

    def test_negative_length(self):
        self.negative_length()

    def test_invalid_argument(self):
        self.invalid_argument()


class Php(PassgenTest):
    name = 'php'
    file = 'build/passgen.php'
    basic_command = ['php', file]

    def test_check_build(self):
        self.check_build()

    def test_basic(self):
        self.basic()

    def test_variable_length(self):
        self.variable_length()

    def test_negative_length(self):
        self.negative_length()

    def test_invalid_argument(self):
        self.invalid_argument()

class Ruby(PassgenTest):
    name = 'ruby'
    file = 'build/passgen.rb'
    basic_command = ['ruby', file]

    def test_check_build(self):
        self.check_build()

    def test_basic(self):
        self.basic()

    def test_variable_length(self):
        self.variable_length()

    def test_negative_length(self):
        self.negative_length()

    def test_invalid_argument(self):
        self.invalid_argument()

if __name__ == '__main__':
    unittest.main()
