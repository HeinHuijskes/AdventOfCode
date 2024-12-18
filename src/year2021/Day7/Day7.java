package year2021.Day7;

import JavaFramework.Day;

import java.io.IOException;
import java.util.List;

public class Day7 extends Day {
    public Day7() throws IOException {
        super(false);
    }

    public static void main(String[] args) throws IOException {
        new Day7();
    }

    @Override
    public String part1(List<String> input) {
        String[] inputArray = input.get(0).split(",");
        int[] positions = new int[inputArray.length];
        int maxPosition = 0;
        for (int i = 0; i < inputArray.length; i++) {
            positions[i] = Integer.parseInt(inputArray[i]);
            if (positions[i] > maxPosition) maxPosition = positions[i];
        }

        long lowestFuelConsumption = Integer.MAX_VALUE; // lowest fuel consumption overall
        long currentFuelConsumption; // temporary value storing the fuel consumption in the current loop
        long newPosition = 0; // position the crabs should move to
        long bestPosition = 0;
        for (; newPosition <= maxPosition; newPosition++) {
            currentFuelConsumption = 0;
            for (int position : positions) {
                currentFuelConsumption += Math.abs(position - newPosition);
            }
            if (currentFuelConsumption < lowestFuelConsumption) {
                lowestFuelConsumption = currentFuelConsumption;
                bestPosition = newPosition;
            }
        }

        return Long.toString(lowestFuelConsumption);
    }

    @Override
    public String part2(List<String> input) {
        String[] inputArray = input.get(0).split(",");
        int[] positions = new int[inputArray.length];
        int maxPosition = 0;
        for (int i = 0; i < inputArray.length; i++) {
            positions[i] = Integer.parseInt(inputArray[i]);
            if (positions[i] > maxPosition) maxPosition = positions[i];
        }

        int lowestFuelConsumption = Integer.MAX_VALUE; // lowest fuel consumption overall
        int currentFuelConsumption; // temporary value storing the fuel consumption in the current loop
        for (int newPosition = 0; newPosition <= maxPosition; newPosition++) {
            currentFuelConsumption = 0;
            for (int position : positions) {
                currentFuelConsumption += getFuelConsumption(Math.abs(position - newPosition));
            }
            if (currentFuelConsumption < lowestFuelConsumption) {
                lowestFuelConsumption = currentFuelConsumption;
            }
        }

        return Long.toString(lowestFuelConsumption);
    }

    public static int getFuelConsumption(int amount) {
        int result = 0;
        while (amount > 0) {
            result += amount;
            amount--;
        }
        return result;
    }
}
