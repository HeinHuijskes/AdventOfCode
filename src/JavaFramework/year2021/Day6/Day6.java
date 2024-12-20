package year2021.Day6;

import JavaFramework.Day;

import java.io.IOException;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.List;

public class Day6 extends Day {
    public Day6() throws IOException {
        super(false);
    }

    public static void main(String[] args) throws IOException {
        new Day6();
    }

    @Override
    public String part1(List<String> input) {
        int[] fish = new int[9];
        Arrays.fill(fish, 0);
        String[] allFish = input.get(0).split(",");
        for (String entry : allFish) {
            int parsed = Integer.parseInt(entry);
            fish[parsed]++;
        }
        int days = 80;
        for (int i = 0; i < days; i++) {
            int fish0 = fish[0];
            fish[0] = 0;
            for (int j = 1; j < fish.length; j++) {
                fish[j-1] += fish[j];
                fish[j] = 0;
            }
            fish[6] += fish0;
            fish[8] += fish0;
        }
        int total = 0;
        for (int f : fish) {
            total += f;
        }
        return Integer.toString(total);
    }

    @Override
    public String part2(List<String> input) {
        BigInteger[] fish = new BigInteger[9];
        for (int i = 0; i < fish.length; i++) {
            fish[i] = new BigInteger("0");
        }
        String[] allFish = input.get(0).split(",");
        for (String entry : allFish) {
            int parsed = Integer.parseInt(entry);
            fish[parsed] = fish[parsed].add(BigInteger.valueOf(1));
        }
        int days = 256;
        for (int i = 0; i < days; i++) {
            BigInteger fish0 = new BigInteger(fish[0].toString());
            fish[0] = new BigInteger("0");
            for (int j = 1; j < fish.length; j++) {
                fish[j-1] = fish[j];
                fish[j] = new BigInteger("0");
            }
            fish[6] = fish[6].add(fish0);
            fish[8] = fish0;
        }
        BigInteger total = new BigInteger("0");
        for (BigInteger f : fish) {
            total = total.add(f);
        }
        return total.toString();
    }
}
