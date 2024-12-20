package year2021.Day1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class d1 {
    public static void main(String[] args) {
        System.out.println(part1());
        System.out.println(part2());
    }

    private static int part1() {
        int count = 0;
        try {
            File file = new File("src/Advent_of_code/d1_data");
            Scanner reader = new Scanner(file);
            int previous = Integer.MAX_VALUE;
            do {
                String number = reader.nextLine();
                int parsed = Integer.parseInt(number);
                if (parsed > previous) count++;
                previous = parsed;
            } while (reader.hasNextLine());
        } catch (FileNotFoundException ignored) {}
        return count;
    }

    private static int part2() {
        int[] windows = new int[]{0,0,0};
        int count = 0;
        int pointer = 0;
        try {
            File file = new File("src/Advent_of_code/d1_data");
            Scanner reader = new Scanner(file);
            int previous = Integer.MAX_VALUE;
            int number = Integer.parseInt(reader.nextLine());
            windows[0] += number;
            number = Integer.parseInt(reader.nextLine());
            windows[0] += number;
            windows[1] += number;
            do {
                number = Integer.parseInt(reader.nextLine());
                windows[0] += number;
                windows[1] += number;
                windows[2] += number;
                if (windows[pointer] > previous) count++;
                previous = windows[pointer];
                windows[pointer] = 0;
                pointer++;
                pointer = (pointer > 2) ? 0 : pointer;
            } while (reader.hasNextLine());
        } catch (FileNotFoundException ignored) {}
        return count;
    }
}
