package interview.java.linked_lists;

import interview.interview.java.linked_lists.LinkedListNode;

import java.util.Arrays;
import java.util.HashSet;


public class remove_duplicates {

    public static void main(String[] args) {
        int[] list = {2, 3, 3, 4, 4, 5, 5};
        LinkedListNode input = new LinkedListNode(list);

        input.printList();

        LinkedListNode output = remove_duplicates_linkedlist(input);
        output.printList();



    }

    public static LinkedListNode remove_duplicates_linkedlist(LinkedListNode head) {
        HashSet<Integer> set = new HashSet<>();

        LinkedListNode node = head;

        while (node != null) {
            if(set.contains(node.data)) {
                if (node.next == null) {
                    node = null;
                } else {
                    LinkedListNode next = node.next;
                    node.data = next.data;
                    node.next = next.next;
                }
            } else {
                set.add(node.data);
                node = node.next;
            }

        }
        return head;
    }
}
