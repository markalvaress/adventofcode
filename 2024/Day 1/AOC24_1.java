import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Arrays;
import java.lang.Math;

public class AOC24_1 {
    public static int countlines(File file) {
        int numlines = 0;

        try {
            Scanner myReader = new Scanner(file);

            while (myReader.hasNextLine()) {
                numlines++;
                myReader.nextLine();
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error ocurred.");
            e.printStackTrace();
        }

        return numlines;
    }

    public static void main(String[] args) {
        File input_txt = new File("aoc24_1_input.txt");
        int len_lists = countlines(input_txt);
        int[] list1 = new int[len_lists];
        int[] list2 = new int[len_lists];

        // read lists from file
        try {
            Scanner myReader = new Scanner(input_txt);

            int i = 0;
            while (myReader.hasNextLine()) {
                String line = myReader.nextLine();
                String[] numbers = line.split("   ");
                list1[i] = Integer.parseInt(numbers[0]);
                list2[i] = Integer.parseInt(numbers[1]);
                i++;
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error ocurred.");
            e.printStackTrace();
        }

        Arrays.sort(list1);
        Arrays.sort(list2);

        int total_distance = 0;
        int i;
        for (i = 0; i < len_lists; i++) {
            total_distance += Math.abs(list2[i] - list1[i]);
        }

        System.out.println(total_distance);
    }
}
