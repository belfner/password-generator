param ([int] $num_words = 4)
if ($num_words -lt 1)
{
    write-host "Argument must be greater than or equal to 1"
    exit
}
$pwords = $words
$upper_letters = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
$digits = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
$password = ""
for ($i = 1; $i -le $num_words; $i++)
{
    $password += Get-Random -InputObject $pwords
    $password += "."
}

$password += Get-Random -InputObject $upper_letters
$password += Get-Random -InputObject $digits
write-host $password