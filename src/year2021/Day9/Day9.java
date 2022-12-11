package year2021.Day9;

import JavaFramework.Day;

import java.io.IOException;
import java.util.List;

import static year2021.Utils.*;

public class Day9 extends Day {

    public static boolean[][] searched;
    public static int[][] heightMap2;

    public Day9() throws IOException {
        super(false);
    }

    public static void main(String[] args) throws IOException {
        new Day9();
    }

    @Override
    public String part1(List<String> input) {
        int[][] heightMap = new int[input.size()][input.get(0).length()];
//        boolean[][] searched = new boolean[input.get(0).length()][input.size()];
        for (int i = 0; i < heightMap.length; i++) {
            for (int j = 0; j < heightMap[0].length; j++) {
//                searched[i][j] = false;
                heightMap[i][j] = Integer.parseInt(input.get(i).substring(j, j+1));
//                System.out.print(heightMap[i][j]);
            }
//            System.out.println();
        }

        int totalRiskLevel = 0;
        for (int i = 0; i < heightMap.length; i++) {
            for (int j = 0; j < heightMap[0].length; j++) {
                if (isLowPoint(heightMap, i, j)) {
//                    System.out.println(heightMap[i][j] + " at (" + i + "," + j + ") is a low point");
                    totalRiskLevel += heightMap[i][j]+1;
                }
            }
        }

        return Integer.toString(totalRiskLevel);
    }

    private static boolean isLowPoint(int[][] heightMap, int i, int j) {
        int current = heightMap[i][j];
        if (current == 9) return false;
        if (i > 0 && heightMap[i-1][j] < current) {
            return false;
        }
        if (i < heightMap.length-1 && heightMap[i+1][j] < current) {
            return false;
        }
        if (j > 0 && heightMap[i][j-1] < current) {
            return false;
        }
        if (j < heightMap[0].length - 1 && heightMap[i][j+1] < current) {
            return false;
        }
        return true;
    }

    @Override
    public String part2(List<String> input) {
        heightMap2 = new int[input.size()][input.get(0).length()];
        searched = new boolean[input.size()][input.get(0).length()];
        for (int i = 0; i < heightMap2.length; i++) {
            for (int j = 0; j < heightMap2[0].length; j++) {
                searched[i][j] = false;
                heightMap2[i][j] = Integer.parseInt(input.get(i).substring(j, j+1));
            }
        }

        int[] largestBasins = new int[]{1,1,1};
        int basinsFound = 0;
        int basinSize;
        for (int i = 0; i < heightMap2.length; i++) {
            for (int j = 0; j < heightMap2[0].length; j++) {
                if (isLowPoint(heightMap2, i, j)) {
                    basinsFound++;
                    basinSize = getBasinSize(i, j);
                    System.out.println("Basin at (" + i + "," + j + "), size: " + basinSize);
                    for (int k = 0; k < 3; k++) {
                        if (basinSize > largestBasins[k]) {
                            int temp = largestBasins[k];
                            largestBasins[k] = basinSize;
                            basinSize = temp;
                        }
                    }
                }
            }
        }

        printInColour(heightMap2, true);
        System.out.println("Found " + basinsFound + " basins total");
        System.out.println("Largest basin sizes: " + largestBasins[0] + ", " + largestBasins[1] + ", " + largestBasins[2] + "\n");
        return Integer.toString(largestBasins[0] * largestBasins[1] * largestBasins[2]);
    }

    private int getBasinSize(int i, int j) {
        if (heightMap2[i][j] == 9) return 0;
        int size = 1;
        searched[i][j] = true;
        if (i > 0 && !searched[i-1][j]) {
            size += getBasinSize(i-1, j);
        }
        if (i < heightMap2.length-1 && !searched[i+1][j]) {
            size += getBasinSize(i+1, j);
        }
        if (j > 0 && !searched[i][j-1]) {
            size += getBasinSize(i, j-1);
        }
        if (j < heightMap2[0].length-1 && !searched[i][j+1]) {
            size += getBasinSize(i, j+1);
        }
        return size;
    }

    public static void printInColour(int[][] map, boolean raw) {
        String[] printLns = new String[map.length];
        for (int i = 0; i < map.length; i++) {
            String ln = "";
            for (int j = 0; j < map[0].length; j++) {
                int value = map[i][j];
                String output = raw ? Integer.toString(value) : "▓";
                if (value == 9) {
                    ln += TEXT_RED + output + TEXT_RESET;
                } else if (isLowPoint(map, i, j)) {
                    ln += raw ? output : "▒"; // output or "░", "▓", "▓", "█"
                } else if (value > 5){
                    ln += TEXT_YELLOW + output + TEXT_RESET;
                } else {
                    ln += TEXT_GREEN + output + TEXT_RESET;
                }
            }
            printLns[i] = ln;
        }
        System.out.println();
        for (String ln : printLns) {
            System.out.println(ln);
        }
        System.out.println();
    }
}
