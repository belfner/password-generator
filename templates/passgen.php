<?php

$num_words = 4;

if ($argc > 1)
{
    if ($argc > 2)
    {
        echo "Too many arguments";
        exit;
    }
    if (!filter_var($argv[1], FILTER_VALIDATE_INT))
    {
        echo "Argument is not a integer";
        exit;
    }
    $num_words = (int)$argv[1];
    if ( $num_words < 1)
    {
        echo "Argument must be greater than or equal to 1";
        exit;
    }
}

$word_list = array($words);
$upper_letters = array("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z");
$digits = array("0", "1", "2", "3", "4", "5", "6", "7", "8", "9");


$password = "";

for ($i=0; $i < $num_words - 1; $i++) {
    $password .= $word_list[array_rand($word_list,1)];
    $password .= ".";
}
$password .= $word_list[array_rand($word_list,1)];
$password .= $upper_letters[array_rand($upper_letters,1)];
$password .= $digits[array_rand($digits,1)];
echo $password;
