package interview.interview.java.sorting;

import java.util.ArrayList;
import java.util.Arrays;

public class counting_sort {

    public static void main(String[] args) {
        int[] input = {1, 4, 1, 2, 7, 5, 2};
        int[] ouput = counting_sort(input);

        System.out.println(Arrays.toString(ouput));
    }

    public static int[] counting_sort(int[] input) {

        int[] count = new int[10];

        for(int i = 0; i < input.length; i++) {
            count[input[i]]++;
        }

        for(int i = 1; i < count.length; i++) {
            count[i] += count[i - 1];
        }

        int[] output = new int[input.length];
        Arrays.fill(output, 0);

        for(int i = 0; i < input.length; i++) {
            int index = count[input[i]];
            output[index - 1] = input[i];
            count[input[i]]--;
        }

        return output;
    }
}
