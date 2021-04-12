import java.util.Random;

public class Passgen {

    static String[] words = {$words};
    static String upper = "ABCDEFGHIJKLMNPQRSTUVWXYZ";
    static String digits = "0123456789";
    static Random rand = new Random();
    public static void main(String[] args)
    {
        int num_words = 4;
        if(args.length > 1)
        {
            System.out.println("Too many arguments");
            return;
        }
        if(args.length == 1)
        {
            try
            {
                num_words = Integer.parseInt(args[0]);
            }
            catch (NumberFormatException e)
            {
                System.out.println("Argument is not a integer");
                return;
            }
            if (num_words<1)
            {
                System.out.println("Argument must be greater than or equal to 1");
                return;
            }
        }

        String password = "";

        for(int x = 0; x< num_words;x++)
        {
            password += words[Passgen.rand.nextInt(words.length)];
            password += ".";

        }
        password += Character.toString(Passgen.upper.charAt(Passgen.rand.nextInt(Passgen.upper.length())));
        password += Character.toString(Passgen.digits.charAt(Passgen.rand.nextInt(Passgen.digits.length())));
        System.out.println(password);

    }
}
