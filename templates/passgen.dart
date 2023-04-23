import 'dart:math';

class Passgen {
  static final _random = new Random();
  static List<String> words = [$words];
  static List<String> upperLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
  static List<String> digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

  static String genPass(int numWords) {
    String password = '';
    for (var i = 0; i < numWords - 1; i++) {
      password += Passgen.words[Passgen._random.nextInt(Passgen.words.length)];
      password += '.';
    }
    password += Passgen.words[Passgen._random.nextInt(Passgen.words.length)];
    password += Passgen.upperLetters[Passgen._random.nextInt(Passgen.upperLetters.length)];
    password += Passgen.digits[Passgen._random.nextInt(Passgen.digits.length)];
    return password;
  }
}


void main(List<String> arguments) {
  int numWords = 4;

  if (arguments.length > 1) {
    print('Too many arguments');
    return;
  }
  if (arguments.length == 1) {
    if (int.tryParse(arguments[0]) == null) {
      print('Argument is not a integer');
      return;
    }
    int numWords = int.parse(arguments[0]);
    if (numWords < 1) {
      print('Argument must be greater than or equal to 1');
      return;
    }
    else {
      print(Passgen.genPass(numWords));
      return;
    }
  }
  print(Passgen.genPass(numWords));
}