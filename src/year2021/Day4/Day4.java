package year2021.Day4;

import JavaFramework.Day;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Day4 extends Day {

    public Day4() throws IOException {
        super(false);
    }

    public static void main(String[] args) throws IOException {
        new Day4();
    }

    private void fillBingoCards(List<String> copy, int[][][] bingoCards) {
        String[] line = null;
        int index = 0;
        do { // generate the bingo cards
            for (int i = 0; i < 5; i++) {
                line = copy.get(0).replace("  ", " ").split(" ");
                if (line.length > 5) {
                    String[] resize = new String[5];
                    System.arraycopy(line, 1, resize, 0, 5);
                    line = resize;
                }
//                System.out.println(Arrays.toString(Arrays.stream(line).toArray()));
                for (int j = 0; j < 5; j++) {
                    bingoCards[index][i][j] = Integer.parseInt(line[j]);
                }
                copy.remove(0);
            }
            if (copy.size() > 0) {
                index++;
                copy.remove(0);
            }
        } while (copy.size() > 0);
    }



    @Override
    public String part1(List<String> input) {
        List<String> copy = new ArrayList<>(input);
        String[] numbers = copy.get(0).split(",");
        copy.remove(0);
        copy.remove(0);
        boolean[][][] bingoCheck = new boolean[copy.size()/6 + 1][5][5];
        fill(bingoCheck, false);
        int[][][] bingoCards = new int[copy.size()/6 + 1][5][5];
        fillBingoCards(copy, bingoCards);

//        displayCard(bingoCards[0]);
//        System.out.println();
//        displayCard(bingoCards[bingoCards.length - 1]);

        int num = 0;
        int[][] bingo = null;
        int i = 0;
        int j = 0;
        int k = 0;
        for (String number : numbers) { // cross out bingo numbers
            num = Integer.parseInt(number);
//            System.out.print(num + ",");
            for (i = 0; i < bingoCards.length; i++) {
                for (j = 0; j < bingoCards[0].length; j++) {
                    for (k = 0; k < bingoCards[0][0].length; k++) {
                        if (bingoCards[i][j][k] == num) {
                            bingoCheck[i][j][k] = true;
                            if (checkBingo(bingoCheck[i], j, k)) {
                                bingo = bingoCards[i];
//                                System.out.println();
//                                displayCard(bingo);
//                                System.out.println(j + ", " + k + ", num: " + num);
                                break;
                            }
                        }
                    }
                    if (bingo != null) break;
                }
                if (bingo != null) break;
            }
            if (bingo != null) break;
        }

        int sum = 0;
        for (k = 0; k < bingo.length; k++) {
            for (j = 0; j < bingo[0].length; j++) {
                if (!bingoCheck[i][j][k]) {
                    sum += bingo[j][k];
                }
            }
        }

        return Integer.toString((sum * num));
    }

    private void displayCard(int[][] bingoCard) {
        for (int[] test : bingoCard) {
            System.out.println(Arrays.toString(Arrays.stream(test).toArray()));
        }
    }

    private boolean checkBingo(boolean[][] bingoCard, int j, int k) {
        boolean horizontalBingo = true;
        boolean verticalBingo = true;
        for (int i = 0; i < bingoCard.length; i++) {
            if (!bingoCard[j][i]) {
                horizontalBingo = false;
            }
            if (!bingoCard[i][k]) {
                verticalBingo = false;
            }
        }
        return horizontalBingo || verticalBingo;
    }

    private void fill(boolean[][][] array, boolean value) {
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[0].length; j++) {
                for (int k = 0; k < array[0][0].length; k++) {
                    array[i][j][k] = value;
                }
            }
        }
    }

    @Override
    public String part2(List<String> input) {
        List<String> copy = new ArrayList<>(input);
        String[] numbers = copy.get(0).split(",");
        copy.remove(0);
        copy.remove(0);
        boolean[][][] bingoCheck = new boolean[copy.size()/6 + 1][5][5];
        fill(bingoCheck, false);
        int[][][] bingoCards = new int[copy.size()/6 + 1][5][5];
        fillBingoCards(copy, bingoCards);

        ArrayList<Integer> tracker = new ArrayList<>();
        for (int i = 0; i < bingoCards.length; i++) {
            tracker.add(i);
        }

        int num = 0;
        int[][] bingo = null;
        int i = 0;
        int j = 0;
        int k = 0;
        for (String number : numbers) { // cross out bingo numbers
            num = Integer.parseInt(number);
//            System.out.print(num + ",");
            int[] indices = makeIntArray(tracker);
            for (int index : indices) {
                for (j = 0; j < bingoCards[0].length; j++) {
                    for (k = 0; k < bingoCards[0][0].length; k++) {
                        if (bingoCards[index][j][k] == num) {
                            bingoCheck[index][j][k] = true;
                            if (checkBingo(bingoCheck[index], j, k)) {
                                if (indices.length == 1) {
                                    i = index;
                                    bingo = bingoCards[index];
                                    break;
                                } else {
                                    removeFromArrayList(tracker, index);
                                }
//                                System.out.println();
//                                displayCard(bingo);
//                                System.out.println(j + ", " + k + ", num: " + num);
                            }
                        }
                    }
                    if (bingo != null) break;
                }
                if (bingo != null) break;
            }
            if (bingo != null) break;
        }

        int sum = 0;
        for (k = 0; k < bingo.length; k++) {
            for (j = 0; j < bingo[0].length; j++) {
                if (!bingoCheck[i][j][k]) {
                    sum += bingo[j][k];
                }
            }
        }

        return Integer.toString((sum * num));
    }

    private int[] makeIntArray(ArrayList<Integer> input) {
        int[] result = new int[input.size()];

        for (int i = 0; i < input.size(); i++) {
            result[i] = input.get(i);
        }

        return result;
    }

    private static void removeFromArrayList(ArrayList<Integer> list, int tbr) {
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) == tbr) {
                list.remove(i);
                break;
            }
        }
    }
}
