from secrets import choice
import string
import argparse

parser = argparse.ArgumentParser(description="Password generator")
parser.add_argument('num', type=int, nargs='?', default=4, help="number of words in the password")
args = parser.parse_args()

words = [$words]

if args.num < 1:
    print('Argument must be greater than or equal to 1')
    exit()

password = ''
for x in range(args.num):
    password += choice(words)
    password += '.'
password = password[:-1]
password += choice(string.ascii_uppercase)
password += choice(string.digits)
print(password)
