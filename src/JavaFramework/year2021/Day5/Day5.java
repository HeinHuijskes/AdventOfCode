package year2021.Day5;

import JavaFramework.Day;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Day5 extends Day {
    public Day5() throws IOException {
        super(false);
    }

    public static void main(String[] args) throws IOException {
        new Day5();
    }

    @Override
    public String part1(List<String> input) {
        int[][] array = new int[1000][1000];
        for (int i = 0; i < 1000; i++) {
            for (int j = 0; j < 1000; j++) {
                array[i][j] = 0;
            }
        }
        List<String> copy = new ArrayList<>(input);

        int[] x = new int[2];
        int[] y = new int[2];
        while (copy.size() > 0) {
            String[] values = copy.get(0).split(" -> ");
            x[0] = Integer.parseInt(values[0].split(",")[0]);
            x[1] = Integer.parseInt(values[1].split(",")[0]);
            y[0] = Integer.parseInt(values[0].split(",")[1]);
            y[1] = Integer.parseInt(values[1].split(",")[1]);

            if (x[0] == x[1]) {
                for (int i = Math.min(y[0], y[1]); i <= Math.max(y[0], y[1]); i++) {
                    array[x[0]][i] += 1;
                }
            } else if (y[0] == y[1]) {
                for (int i = Math.min(x[0], x[1]); i <= Math.max(x[0], x[1]); i++) {
                    array[i][y[0]] += 1;
                }
            }
            copy.remove(0);
        }

        int counter = 0;
        for (int[] col : array) {
            for (int row : col) {
                if (row >= 2) {
                    counter++;
                }
            }
        }
        return Integer.toString(counter);
    }

    @Override
    public String part2(List<String> input) {
        int[][] array = new int[1000][1000];
        for (int i = 0; i < 1000; i++) {
            for (int j = 0; j < 1000; j++) {
                array[i][j] = 0;
            }
        }
        List<String> copy = new ArrayList<>(input);

        int[] x = new int[2];
        int[] y = new int[2];
        while (copy.size() > 0) {
            String[] values = copy.get(0).split(" -> ");
            x[0] = Integer.parseInt(values[0].split(",")[0]);
            x[1] = Integer.parseInt(values[1].split(",")[0]);
            y[0] = Integer.parseInt(values[0].split(",")[1]);
            y[1] = Integer.parseInt(values[1].split(",")[1]);

            if (x[0] == x[1]) {
                for (int i = Math.min(y[0], y[1]); i <= Math.max(y[0], y[1]); i++) {
                    array[x[0]][i] += 1;
                }
            } else if (y[0] == y[1]) {
                for (int i = Math.min(x[0], x[1]); i <= Math.max(x[0], x[1]); i++) {
                    array[i][y[0]] += 1;
                }
            } else {
                int dy;
                int xStart = Math.min(x[0], x[1]);
                int yStart;
                if (x[0] < x[1]) {
                    yStart = y[0];
                    if (y[0] < y[1]) {
                        dy = 1;
                    } else {
                        dy = -1;
                    }
                } else {
                    yStart = y[1];
                    if (y[0] < y[1]) {
                        dy = -1;
                    } else {
                        dy = 1;
                    }
                }
                for (int i = 0; i <= Math.abs(x[0] - x[1]); i++) {
                    array[xStart+i][yStart+dy*i] += 1;
                }
            }
            copy.remove(0);
        }

        int counter = 0;
        for (int[] col : array) {
            for (int row : col) {
                if (row >= 2) {
                    counter++;
                }
            }
        }
        return Integer.toString(counter);
    }
}
