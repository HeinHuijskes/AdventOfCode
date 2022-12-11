package year2021.Day11;

import JavaFramework.Day;

import java.io.IOException;
import java.util.List;
import static year2021.Utils.*;

public class Day11 extends Day {

    public static int[][] octopuses = new int[10][10];
    public static int flashes;
    public static boolean synchronousFlash = false;

    public Day11() throws IOException {
        super(false);
    }

    public static void main(String[] args) throws IOException {
        new Day11();
    }

    @Override
    public String part1(List<String> input) {
        flashes = 0;
        for (int i = 0; i < input.size(); i++) {
            for (int j = 0; j < input.get(0).length(); j++) {
                octopuses[i][j] = Integer.parseInt(input.get(i).substring(j, j+1));
//                System.out.print(octopuses[i][j]);
            }
//            System.out.println();
        }

        for (int i = 1; i <= 100; i++) {
            update();
            updateFlashes();
            if (i < 5) {
                printOctopuses();
            }
        }

        return Integer.toString(flashes);
    }

    public static void update() {
        for (int i = 0; i < octopuses.length; i++) {
            for (int j = 0; j < octopuses[0].length; j++) {
                octopuses[i][j]++;
            }
        }
    }

    public static void updateFlashes() {
        int flashCount;
        do {
            flashCount = 0;
            for (int i = 0; i < octopuses.length; i++) { // y
                for (int j = 0; j < octopuses[0].length; j++) { // x
                    if (octopuses[i][j] > 9) {
                        flashCount++;
                        flash(j, i); // flash(x,y)
                    }
                }
            }
        } while (flashCount != 0);
    }

    public static void flash(int x, int y) {
        flashes++;
        for (int i = x-1; i <= x+1; i++) {
            for (int j = y-1; j <= y+1; j++) {
                add(i, j);
            }
        }
        octopuses[y][x] = 0;
    }

    public static void add(int x, int y) {
        if (x >= 0 && x < octopuses[0].length && y >= 0 && y < octopuses.length) {
            if (octopuses[y][x] != 0) {
                octopuses[y][x]++;
            }
        }
    }

    @Override
    public String part2(List<String> input) {
        flashes = 0;
        for (int i = 0; i < input.size(); i++) {
            for (int j = 0; j < input.get(0).length(); j++) {
                octopuses[i][j] = Integer.parseInt(input.get(i).substring(j, j+1));
            }
        }

        int counter = 0;
        do {
            counter++;
            update();
            updateFlashes();
            synchronousFlash = checkSynchronous();
        } while (!synchronousFlash);

        return Integer.toString(counter);
    }

    private boolean checkSynchronous() {
        for (int i = 0; i < octopuses.length; i++) {
            for (int j = 0; j < octopuses[0].length; j++) {
                if (octopuses[i][j] != 0) return false;
            }
        }
        return true;
    }

    private void printOctopuses() {
        String output = TEXT_WHITE;
        for (int i = 0; i < octopuses.length; i++) {
            for (int j = 0; j < octopuses[0].length; j++) {
                if (octopuses[i][j] != 0) {
                    output += Integer.toString(octopuses[i][j]);
                } else {
                    output += TEXT_RESET + "*" + TEXT_WHITE;
                }
            }
            output += "\n";
        }
        System.out.println(output);
    }
}
