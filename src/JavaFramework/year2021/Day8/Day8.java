package year2021.Day8;

import JavaFramework.Day;

import java.io.IOException;
import java.util.List;

public class Day8 extends Day {
    public Day8() throws IOException {
        super(false);
    }

    public static void main(String[] args) throws IOException {
        new Day8();
    }

    @Override
    public String part1(List<String> input) {
        String[] lines = new String[input.size()];
        for (int i = 0; i < input.size(); i++) {
            lines[i] = input.get(i).split("\\|")[1];
        }

        int counter = 0;
        String[] outputs;
        int length;
        for (int i = 0; i < lines.length; i++) {
            outputs = lines[i].split(" ");
            for (String output : outputs) {
                length = output.length();
                if (length == 2 || length == 3 || length == 4 || length == 7) {
                    counter++;
                }
            }
        }

        return Integer.toString(counter);
    }

    @Override
    public String part2(List<String> input) {
        return null;
    }
}
