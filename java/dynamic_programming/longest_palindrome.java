/**
 Given a string S, find the longest palindromic substring in S.

 Substring of string S:

 S[i...j] where 0 <= i <= j < len(S)

 Palindrome string:

 A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

 Incase of conflict, return the substring which occurs first ( with the least starting index ).

 Example :

 Input : "aaaabaaa"
 Output : "aaabaaa"
 */


package interview.interview.java.dynamic_programming;

public class longest_palindrome {

    public static void main(String[] args) {
        String input = "aaaabaaa";
        String exp_output = "aaabaaa";

        String result = longestPalindrome(input);
        assert result.equals(exp_output);
        System.out.println("Success!");
    }

    public static String longestPalindrome(String str) {
        int n = str.length();

        boolean[][] dp = new boolean[n][n];
        //Arrays.fill(dp, false);
        int longestBegin = 0;
        int maxLen = 1;

        for(int i = 0; i < n; i++) {
            dp[i][i] = true;
        }

        for(int i = 1; i < n; i++) {
            if(str.charAt(i) == str.charAt(i-1)) {
                dp[i-1][i] = true;
                longestBegin = i - 1;
                maxLen = 2;
            }

        }

        for(int len = 3; len <= n; len++) {
            for(int i = 0; i < n - len + 1; i++) {
                int j = i + len - 1;
                if(str.charAt(i) == str.charAt(j) && dp[i+1][j-1]) {
                    dp[i][j] = true;
                    if (len > maxLen) {
                        maxLen = len;
                        longestBegin = i;
                     }
                }
            }
        }

        return str.substring(longestBegin, longestBegin + maxLen);
    }
}

