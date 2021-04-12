
num_words = 4

if ARGV.length > 0
    if ARGV.length > 1
        print "Too many arguments"
        exit
    end
    # from https://stackoverflow.com/questions/1235863/how-to-test-if-a-string-is-basically-an-integer-in-quotes-using-ruby
    if /\A[-+]?\d+\z/ === ARGV[0]
        if ARGV[0].to_i < 1
            print "Argument must be greater than or equal to 1"
            exit
        else
            num_words = ARGV[0].to_i
        end
    else
        print "Argument is not a integer"
        exit
    end
end


words = [$words]
upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

password = ""

i = 0
loop do
    if i == num_words
        break
    end
    password += words.sample
    password += "."

    i+=1

end

password += upper_letters.sample
password += digits.sample

print password