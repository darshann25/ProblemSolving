/*
Implement an algorithm to determine if a string has all unique characters
*/
package interview.java.arrays;

public class unique_string {
    public static void main(String[] args) {
        String text = "abcdea";
        if (is_string_unique(text)) System.out.println("Yes, " + text + " is unque!");
        else System.out.println("Bummer! " + text + " is not unique!");
    }

    public static boolean is_string_unique(String str) {
        int[] char_freq = new int[256];

        for (int i = 0; i < str.length(); i++) {
            char char_letter = str.charAt(i);
            int int_letter = Character.getNumericValue(char_letter);
            int base = Character.getNumericValue('a');

            if (char_freq[int_letter - base] != 0) return false;
            else char_freq[int_letter - base] = 1;
        }

        return true;
    }
}
