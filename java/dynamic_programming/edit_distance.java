/**
Given two words A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example :
edit distance between
"Anshuman" and "Antihuman" is 2.

Operation 1: Replace s with t.
Operation 2: Insert i.
*/


package interview.interview.java.dynamic_programming;

public class edit_distance {

    public static void main(String[] args) {
        String a = "sunday";
        String b = "saturday";

        assert (minDistance(a, b) == 3);

        String c = "Anshuman";
        String d = "Antihuman";

        assert (minDistance(c, d) == 2);

        System.out.println("Success!");
    }

    public static int minDistance(String a, String b) {
        int m = a.length();
        int n = b.length();
        int[][] memo = new int[m+1][n+1];

        for(int i = 0; i <= m; i++) {
            for(int j = 0; j <= n; j++) {

                // if first string is empty, distance is len of second string
                if (i == 0) {
                    memo[i][j] = j;
                    continue;
                }

                // if second string is empty, distance is len of first string
                if (j == 0) {
                    memo[i][j] = i;
                    continue;
                }

                // if the characters match, do not increment distance
                if (a.charAt(i-1) == b.charAt(j-1)) {
                    memo[i][j] = memo[i-1][j-1];
                    continue;
                }

                // otherwise increment one to the min dist of three operations
                memo[i][j] = 1 + Math.min(memo[i][j-1], Math.min(memo[i-1][j], memo[i-1][j-1])); // Delete

            }
        }

        return memo[m][n];
    }
}
