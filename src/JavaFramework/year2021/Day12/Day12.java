package year2021.Day12;

import JavaFramework.Day;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Day12 extends Day {

    public static HashMap<String, Cave> pathMap;
    public static ArrayList<ArrayList<String>> paths;

    public Day12() throws IOException {
        super(true);
    }

    public static void main(String[] args) throws IOException {
        new Day12();
    }

    public class Cave {
        boolean isSmall;
        String name;
        Cave[] connections = null;

        public Cave(String name, boolean isSmall) {
            this.name = name;
            this.isSmall = isSmall;
        }

        public void addConnection(Cave connection) {
            if (connections == null) {
                connections = new Cave[]{connection};
            } else {
                Cave[] newConnectionsList = new Cave[connections.length+1];
                int i = 0;
                for (; i < connections.length; i++) {
                    newConnectionsList[i] = connections[i];
                }
                newConnectionsList[i+1] = connection;
                connections = newConnectionsList;
            }
        }

    }

    @Override
    public String part1(List<String> input) {
        ArrayList<String> caves = new ArrayList<>();
        for (String connection : input) {
            String[] cave = connection.split("-");
            if (!caves.contains(cave[0])) {
                caves.add(cave[0]);
            }
            if (!caves.contains(cave[1])) {
                caves.add(cave[1]);
            }
        }

        pathMap = new HashMap<>();
        for (String name : caves) {
            boolean smallCave = Character.isLowerCase(name.charAt(0));
            Cave cave = new Cave(name, smallCave);
            pathMap.put(name, cave);
        }

        for (String connection : input) {
            String[] caverns = connection.split("-");
            String src = caverns[0];
            String dest = caverns[1];
            pathMap.get(src).addConnection(pathMap.get(dest));
        }

        // now recursively go through the caves starting at the start and ending at the end
        // make sure to not visit small caves more than once
        // return number of unique routes

        ArrayList<String> path = new ArrayList<>();
        path.add("start");
        return Integer.toString(getPaths(path).size());
    }

    private ArrayList<String> getPaths(ArrayList<String> path) {
        for (Cave node : pathMap.get(path.get(path.size()-1)).connections) {
            if (node.isSmall && path.contains(node.name)) { // also include start
                paths.add(path);
            } else {

            }
        }
        return null;
    }

    @Override
    public String part2(List<String> input) {
        return null;
    }
}
