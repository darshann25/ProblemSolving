/**
 * You are given a set of coins S. In how many ways can you make sum N assuming you have infinite amount of each coin in the set.

 Note : Coins in set S will be unique. Expected space complexity of this problem is O(N).

 Example :

 Input :
 S = [1, 2, 3]
 N = 4

 Return : 4

 Explanation : The 4 possible ways are
 {1, 1, 1, 1}
 {1, 1, 2}
 {2, 2}
 {1, 3}
 Note that the answer can overflow. So, give us the answer % 1000007
 */

package interview.interview.java.dynamic_programming;

import java.util.Arrays;

public class coin_sum_infinite {

    public void main(String[] args) {
        int[] coins = {1, 2, 3};
        int N = 4;

        int result = coinchange2(coins, N);
        assert result == 4;
        System.out.println("Success!");
    }

    public static int coinchange2(int[] S, int N) {
        int m = S.length;
        int n = N;

        int[] table = new int[n + 1];
        Arrays.fill(table, 0);
        table[0] = 1;

        for(int i = 0; i < m; i++) {
            for(int j = S[i]; j <= n; j++) {
                table[j] += table[j - S[i]];
                table[j] %= 1000007;
            }
        }

        //System.out.println(Arrays.toString(table));
        return table[n] % 1000007;
    }
}

