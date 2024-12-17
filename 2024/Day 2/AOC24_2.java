import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.lang.Math;

public class AOC24_2 {
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
    
    public static boolean is_safe(int[] report) {
        int i;
        int difference;
        boolean increasing = (report[1] > report[0]);
        for (i = 0; i < report.length - 1; i++) {
            difference = report[i+1] - report[i];

            // first two check if the sequence stays monotonic, third checks size of difference
            if (increasing && (difference < 0)) {
                return false;
            } else if (!increasing && (difference > 0)) {
                return false;
            } else if ((Math.abs(difference) < 1) || (Math.abs(difference) > 3)) {
                return false;
            }
        }

        return true;
    } 

    public static boolean is_safe_with_removal(int[] report) {
        // Checks if the report is safe as a whole or with one of its levels removed
        if (is_safe(report)) {
            return true;
        } else {
            int[] report_with_removal = new int[report.length - 1];
            int i;
            int j;
            int k;

            // each iter tests the report with the i'th level removed
            for (i = 0; i < report.length; i++) {
                j = 0;
                k = 0;

                // this skips over the i'th element of report
                while (j < report.length - 1) {
                    if (k != i) {
                        report_with_removal[j] = report[k];
                        j++;
                    }
                    k++;
                }

                if (is_safe(report_with_removal)) return true;
            }

            // we have tried all reports with one removal and none are safe
            return false;
        }        
    } 


    public static void main(String[] args) {
        File input_txt = new File("input.txt");
        int num_reports = countlines(input_txt);
        int[][] reports = new int[num_reports][];

        // read in the input file into `reports` (an array of arrays)
        try {
            Scanner myReader = new Scanner(input_txt);

            int i = 0;
            int j;
            String line;
            String[] numbers;

            // loop through each report and parse the numbers
            while (myReader.hasNextLine()) {
                line = myReader.nextLine();
                numbers = line.split(" ");
                reports[i] = new int[numbers.length];
                for (j = 0; j < numbers.length; j++) {
                    reports[i][j] = Integer.parseInt(numbers[j]);
                }
                i++;
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error ocurred.");
            e.printStackTrace();
        }

        // count the number of reports that are safe
        int num_safe = 0;
        int j;
        for (j = 0; j < num_reports; j++) {
            if (is_safe_with_removal(reports[j])) num_safe += 1;
        }

        System.out.println(String.format("Number of safe reports: %d", num_safe));
    }
}
