package year2021.Day3;

import JavaFramework.Day;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Day3 extends Day {

    public static void main(String[] args) throws IOException {
        new Day3();
    }

    public Day3() throws IOException {
        super(false);
    }

    @Override
    public String part1(List<String> input) {
        int[] counters = new int[12];
        Arrays.fill(counters, 0);
        int num = 0;
        int i;
        for (String entry : input) {
            num = Integer.parseInt(entry, 2);
            for (i = 0; i < 12; i++) {
                if ((num & 1) == 1) {
                    counters[11-i]++;
                } else {
                    counters[11-i]--;
                }
                num = num >> 1;
            }
        }

        int gamma = 0;
        int epsilon = 0;
        int addResult = 0b100000000000; // 12 bits

        for (i = 0; i < 12; i++) {
            if (counters[i] > 0) {
                gamma += addResult;
            } else {
                epsilon += addResult;
            }
            addResult = addResult >> 1;
        }
        return "" + (gamma * epsilon);
    }

    @Override
    public String part2(List<String> input) {
        ArrayList<Integer> ogrList = new ArrayList<>();
        ArrayList<Integer> csrList = new ArrayList<>();
        ArrayList<Integer> new1List = new ArrayList<>();
        ArrayList<Integer> new0List = new ArrayList<>();

        int number;
        for (String entry : input) {
            number = Integer.parseInt(entry, 2);
            ogrList.add(number);
            csrList.add(number);
        }

        int ogrLevel = countLists(ogrList, new1List, new0List, false);
        int csrLevel = countLists(csrList, new1List, new0List, true);

        return "" + (ogrLevel * csrLevel);
    }

    private static int countLists(ArrayList<Integer> countList, ArrayList<Integer> new1List, ArrayList<Integer> new0List, boolean csr) {
        int counter;
        new1List.clear();
        new0List.clear();
        while (countList.size() > 1) {
            int addResult = 0b100000000000;
            for (int i = 0; i < 12; i++) {
                counter = 0;
                for (int integer : countList) {
                    if ((integer & addResult) > 0) {
                        counter++;
                        new1List.add(integer);
                    } else {
                        counter--;
                        new0List.add(integer);
                    }
                }
                addResult = addResult >> 1;
                if (!csr) {
                    countList = counter >= 0 ? (ArrayList<Integer>) new1List.clone() : (ArrayList<Integer>) new0List.clone();
                } else {
                    countList = counter >= 0 ? (ArrayList<Integer>) new0List.clone() : (ArrayList<Integer>) new1List.clone();
                }
                new1List.clear();
                new0List.clear();
                if (countList.size() == 1) break;
            }
        }
        return countList.get(0);
    }
}
