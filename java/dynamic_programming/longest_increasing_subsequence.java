/**
 Given a sequence, find the length of the longest increasing subsequence from a given sequence .
 The longest increasing subsequence means to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest
 to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.

 Note: Duplicate numbers are not counted as increasing subsequence.

 For example:
 length of LIS for
 { 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6 and LIS is {10, 22, 33, 50, 60, 80}.



 Input:
 The first line contains an integer T, depicting total number of test cases.
 Then following T lines contains an integer N depicting the size of array and next line followed by the value of array.


 Output:
 Print the Max length of the subsequence in a separate line.


 Constraints:
 1 ≤ T ≤ 100
 1 ≤ N ≤ 1000
 0 ≤ A[i] ≤ 300

 Example:
 Input
 1
 16
 0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15

 Output
 6
 */

package interview.interview.java.dynamic_programming;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.lang.*;

public class longest_increasing_subsequence {
    public static void main (String[] args) throws FileNotFoundException {
        //code

        Scanner sc = new Scanner(new File("./src/interview/interview/java/dynamic_programming/longest_increasing_subsequence.txt"));
        int test_cases = sc.nextInt();

        while(test_cases > 0) {
            int input_len = sc.nextInt();
            ArrayList<Integer> list = new ArrayList<>();

            for(int i = 0; i < input_len; i++) {

                int curr = sc.nextInt();
                list.add(curr);

            }
            System.out.println(low_inc_subseq(list));
            test_cases--;
        }

    }

    public static int low_inc_subseq(ArrayList<Integer> list) {
        if (list.size() == 0) return 0;
        if (list.size() == 1) return 1;

        int[] result = new int[list.size()];
        Arrays.fill(result, 1);
        int max = 1;

        for(int i = 1; i < result.length; i++) {
            for(int j = 0; j < i; j++) {
                if(list.get(i) > list.get(j)) {
                    int res_val = result[j] + 1;
                    if (res_val > result[i]) {
                        result[i] = res_val;
                        if (max < res_val) max = res_val;
                    }
                }
            }
        }
        return max;
    }
}