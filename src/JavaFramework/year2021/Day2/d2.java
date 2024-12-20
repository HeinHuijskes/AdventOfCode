package year2021.Day2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class d2 {
    public static void main(String[] args) {
        System.out.println(part1());
        System.out.println(part2());
    }

    private static int part1() {
        int depth = 0;
        int pos = 0;
        try {
            Scanner reader = new Scanner(new File("src/Advent_of_code/d2_data"));
            String[] commands = new String[2];
            int amount;
            do {
                commands = reader.nextLine().split(" ");
                amount = Integer.parseInt(commands[1]);
                if (commands[0].equals("forward")) {
                    pos += amount;
                } else if (commands[0].equals("up")) {
                    depth -= amount;
                } else {
                    depth += amount;
                }
            } while (reader.hasNextLine());
        } catch (FileNotFoundException ignored) {}
        return depth*pos;
    }

    private static int part2() {
        int depth = 0;
        int pos = 0;
        int aim = 0;
        try {
            Scanner reader = new Scanner(new File("src/Advent_of_code/d2_data"));
            String[] commands = new String[2];
            int amount;
            do {
                commands = reader.nextLine().split(" ");
                amount = Integer.parseInt(commands[1]);
                if (commands[0].equals("forward")) {
                    pos += amount;
                    depth += aim*amount;
                } else if (commands[0].equals("up")) {
                    aim -= amount;
                } else {
                    aim += amount;
                }
            } while (reader.hasNextLine());
        } catch (FileNotFoundException ignored) {}
        return depth*pos;
    }
}
