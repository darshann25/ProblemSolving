package interview.interview.java.linked_lists;

import interview.interview.java.linked_lists.LinkedListNode;

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
        LinkedListNode previous = null;

        while (node != null) {
            if(set.contains(node.data)){
                previous.next = node.next;
            } else {
                previous = node;
                set.add(node.data);
            }
            node = node.next;
        }

        return head;
    }
}
