package interview.interview.java.linked_lists;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

public class LinkedListNode {
    public LinkedListNode next = null;
    public int data;


    public LinkedListNode(int d) {
        data = d;
    }

    public LinkedListNode(int[] arr) {
        data = arr[0];
        next = new LinkedListNode(arr[1]);

        LinkedListNode runner = next;

        for(int i = 2; i < arr.length; i++){
            LinkedListNode node = new LinkedListNode(arr[i]);
            runner.next = node;
            runner = runner.next;
        }
    }

    public void printList() {
        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(data);
        LinkedListNode runner = next;

        while (runner != null) {
            arr.add(runner.data);
            runner = runner.next;
        }

        System.out.println(Arrays.toString(arr.toArray()));

    }

}

