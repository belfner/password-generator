set words {$words}

set upper_letters {A B C D E F G H I J K L M N O P Q R S T U V W X Y Z}
set digits {0 1 2 3 4 5 6 7 8 9}

set list_len [llength $$words]
set num_words 4
if {$argc>1} {
    puts "Too many arguments"
    exit
} elseif {$argc == 1} {
    set arg [lindex $argv 0]
    if {[scan $arg %d num_words] == 1} {
        if {$num_words < 1} {
            puts "Argument must be greater than or equal to 1"
            exit
        }
    } else {
        puts "Argument is not a integer"
        exit
    }
}
puts $num_words


set password ""
for {set i 0} {$i < $num_words - 1} {incr i} {
    set index [expr {int(rand() * $list_len)}]
    set password $password[lindex $$words $index]
    set password $password\.
}
set index [expr {int(rand() * $list_len)}]
set password $password[lindex $$words $index]

set password $password[lindex $upper_letters [expr {int(rand() * 26)}]]
set password $password[lindex $digits [expr {int(rand() * 10)}]]

puts $password