import 'dart:math';
final _random = new Random();

class Passgen
{
  static List<String> words = [$words];
  static List<String> upperLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
  static List<String> digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
  
  static String genPass({int numWords: 3})
  {
    String password = '';
    for( var i = 0 ; i < numWords; i++ ) 
    { 
      password += Passgen.words[_random.nextInt(Passgen.words.length)];
      password += '.';
    } 
    password = password.substring(0,password.length-1);
    password += Passgen.upperLetters[_random.nextInt(Passgen.upperLetters.length)];
    password += Passgen.digits[_random.nextInt(Passgen.digits.length)];
    return password;
  }
}



void main() {
  print(Passgen.genPass());
}