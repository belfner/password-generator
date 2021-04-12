words=($words)

upper=(A B C D E F G H I J K L M N O P Q R S T U V W X Y Z)
digits=(0 1 2 3 4 5 6 7 8 9)

if [ $# -eq 0 ]; then
  declare -i num_words=4
else
  if [[ $1 != ?(-)+([0-9]) ]]; then
    echo "Argument is not a integer"
    exit
  fi
  declare -i num_words=$1
  if [[ "$num_words" -lt 1 ]]; then
    echo "Argument must be greater than or equal to 1"
    exit
  fi
fi

password=""
for i in $(seq 1 $((num_words))); do
  password+="${words[RANDOM % ${#words[@]}]}"
  password+="."
done

password+="${upper[RANDOM % ${#upper[@]}]}"
password+="${digits[RANDOM % ${#digits[@]}]}"
echo $password
