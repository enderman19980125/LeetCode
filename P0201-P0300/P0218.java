import java.util.*;

class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        Map<Integer, List<Integer>> sky = new TreeMap<>();
        for (int[] building : buildings) {
            int l = building[0], r = building[1], h = building[2];
            if (!sky.containsKey(l)) sky.put(l, new LinkedList<>());
            if (!sky.containsKey(r)) sky.put(r, new LinkedList<>());
            sky.get(l).add(1);
            sky.get(l).add(h);
            sky.get(r).add(-1);
            sky.get(r).add(h);
        }

        int previousHeight = 0;
        List<List<Integer>> ans = new LinkedList<>();
        TreeMap<Integer, Integer> heightMap = new TreeMap<>();
        heightMap.put(0, 1);
        for (Map.Entry<Integer, List<Integer>> e : sky.entrySet()) {
            int x = e.getKey();
            List<Integer> hx = e.getValue();
            for (int i = 0; i < hx.size(); i += 2) {
                int type = hx.get(i);
                int height = hx.get(i + 1);
                if (type == 1) {
                    if (!heightMap.containsKey(height)) heightMap.put(height, 0);
                    heightMap.put(height, heightMap.get(height) + 1);
                } else {
                    heightMap.put(height, heightMap.get(height) - 1);
                    if (heightMap.get(height) == 0) heightMap.remove(height);
                }
            }
            int currentHeight = heightMap.lastKey();
            if (previousHeight != currentHeight) {
                List<Integer> currentPosition = new ArrayList<>(Arrays.asList(x, currentHeight));
                ans.add(currentPosition);
                previousHeight = currentHeight;
            }
        }

        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] buildings;
        List<List<Integer>> answer, stdAnswer;

        buildings = new int[][]{{2, 9, 10}, {3, 7, 15}, {5, 12, 12}, {15, 20, 10}, {19, 24, 8}};
        stdAnswer = new LinkedList<>();
        stdAnswer.add(new LinkedList<>(Arrays.asList(2, 10)));
        stdAnswer.add(new LinkedList<>(Arrays.asList(3, 15)));
        stdAnswer.add(new LinkedList<>(Arrays.asList(7, 12)));
        stdAnswer.add(new LinkedList<>(Arrays.asList(12, 0)));
        stdAnswer.add(new LinkedList<>(Arrays.asList(15, 10)));
        stdAnswer.add(new LinkedList<>(Arrays.asList(20, 8)));
        stdAnswer.add(new LinkedList<>(Arrays.asList(24, 0)));
        answer = solution.getSkyline(buildings);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        buildings = new int[][]{{0, 2, 3}, {2, 5, 3}};
        stdAnswer = new LinkedList<>();
        stdAnswer.add(new LinkedList<>(Arrays.asList(0, 3)));
        stdAnswer.add(new LinkedList<>(Arrays.asList(5, 0)));
        answer = solution.getSkyline(buildings);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        buildings = new int[][]{{0, 2, 3}, {1, 3, 3}, {2, 4, 3}};
        stdAnswer = new LinkedList<>();
        stdAnswer.add(new LinkedList<>(Arrays.asList(0, 3)));
        stdAnswer.add(new LinkedList<>(Arrays.asList(4, 0)));
        answer = solution.getSkyline(buildings);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        buildings = new int[][]{{0, 2, 3}, {1, 3, 4}, {2, 4, 5}};
        stdAnswer = new LinkedList<>();
        stdAnswer.add(new LinkedList<>(Arrays.asList(0, 3)));
        stdAnswer.add(new LinkedList<>(Arrays.asList(1, 4)));
        stdAnswer.add(new LinkedList<>(Arrays.asList(2, 5)));
        stdAnswer.add(new LinkedList<>(Arrays.asList(4, 0)));
        answer = solution.getSkyline(buildings);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        buildings = new int[][]{{0, 2147483647, 1}};
        stdAnswer = new LinkedList<>();
        stdAnswer.add(new LinkedList<>(Arrays.asList(0, 1)));
        stdAnswer.add(new LinkedList<>(Arrays.asList(2147483647, 0)));
        answer = solution.getSkyline(buildings);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);
    }
}