package interview.interview.java.sorting;

import java.util.Arrays;

public class bitwise_sort {

    public static void main(String[] args) {
        int[] bits = {0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1};
        bits = sort(bits);

        System.out.println(Arrays.toString(bits));
    }

    public static int[] sort(int[] arr) {
        int start = 0;
        int end = arr.length - 1;

        while(start < end) {
            if(arr[start] != 0) {
                arr[start] = arr[end];
                arr[end] = 1;
                end--;
            } else {
                start++;
            }

        }

        return arr;
    }
}
