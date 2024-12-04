import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Arrays;
import java.lang.Math;
import java.util.Objects;

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

    public static int count_occurences(int[] list, int number) {
        /* Count number of occurences of `number` in `list`. */
        int i;
        int occurences = 0;

        for (i = 0; i < list.length; i++) {
            if (list[i] == number) {
                occurences++;
            }
        }

        return occurences;
    }

    public static void print_total_difference(int[] list1, int[] list2) {
        /** For pt 1 of the problem */
        Arrays.sort(list1);
        Arrays.sort(list2);

        int total_distance = 0;
        int i;
        for (i = 0; i < list1.length; i++) {
            total_distance += Math.abs(list2[i] - list1[i]);
        }

        System.out.println(total_distance);
    }

    public static void print_sim_score(int[] list1, int[] list2) {
        /** For pt 2 of the problem */
        int i;
        int similarity_score = 0;

        for (i = 0; i < list1.length; i++) {
            similarity_score += list1[i] * count_occurences(list2, list1[i]);
        }

        System.out.println(String.format("Similarity score: %d", similarity_score));
    }

    public static void main(String[] args) {
        /**
         * Takes an arguments '1' or '2', whether to run part 1 or part 2 of the problem.
         */
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

        if (Objects.equals(args[0], "1")) {
            print_total_difference(list1, list2);
        } else if (Objects.equals(args[0], "2")) {
            print_sim_score(list1, list2);
        } else {
            System.out.println(String.format("Invalid argument: %s", args[0]));
        }
    }
}
