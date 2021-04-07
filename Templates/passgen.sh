words=($words)

upper=(A B C D E F G H I J K L M N O P Q R S T U V W X Y Z)
digits=(0 1 2 3 4 5 6 7 8 9)

if [ $# -eq 0 ]
then
  declare -i num_words=4
else
  declare -i num_words=$1
fi
password=""
for i in $(seq 1 $num_words);do
  password+="${words[RANDOM%${#words[@]}]}";
  password+=".";
done

password=${password::-1}

password+="${upper[RANDOM%${#upper[@]}]}"
password+="${digits[RANDOM%${#digits[@]}]}"
echo $password
