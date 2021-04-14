class Passgen
{
    static let words = [$words]
    static let upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    static let digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    static func gen_pass(_ num_words: Int = 3) -> String
    {
        var password = ""
        for _ in 0..<num_words
        {
            password += Passgen.words.randomElement()!
            password += "."
        }
        password = String(password.dropLast(1))
        password += Passgen.upper_letters.randomElement()!
        password += Passgen.digits.randomElement()!
        return password
    }
}

print(Passgen.gen_pass(4))