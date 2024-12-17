import java.io.IOException;
import java.nio.file.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class AOC24_3 {
    public static String read_to_string(String filename) {
        try {
            String data = new String(Files.readAllBytes(Paths.get(filename)));
            return data;
        } catch (IOException e) {
            e.printStackTrace();
            return "";
        }
    }

    public static int parse_multiply(String instruction) {
        // parses the two integers in instruction and multiplies them together
        int result = 1;
        Matcher m = Pattern.compile("[0-9]+").matcher(instruction);
        while (m.find()) {
            result *= Integer.parseInt(m.group());
        }

        return result;
    }

    public static void main(String[] args) {
        String input_data = read_to_string("input.txt");
        int total = 0;

        // create matcher that finds all instances of mul(a,b) for a,b integers
        Matcher m = Pattern.compile("mul\\([0-9]+,[0-9]+\\)").matcher(input_data);

        while (m.find()) {
          total += parse_multiply(m.group());
        }

        System.out.println(String.format("Total = %d", total));
    }
}