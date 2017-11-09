package interview.interview.java.sorting;

import java.util.Arrays;

public class bitwise_sort {

    public static void main(String[] args) {
        int[] bits = {1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1};
        bits = sort(bits);

        System.out.println(Arrays.toString(bits));
    }

    public static int[] sort(int[] arr) {
        int start = 0;
        int end = arr.length - 1;
        int index = 0;

        while(start < end) {
            if(arr[index] == 0 && index > start) {
                arr[index] = arr[start];
                arr[start] = 0;
                start++;
            } else if(arr[index] == 1 && index < end) {
                arr[index] = arr[end];
                arr[end] = 1;
                end--;
            } else {
                index++;
            }

        }

        return arr;
    }
}
