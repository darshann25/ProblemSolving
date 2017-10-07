/*
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
*/

package interview.interview.java.linked_lists;
import java.util.Arrays;
import java.util.HashMap;

public class remove_duplicates_completely {
    public static void main(String[] args){
        int[] list = {1, 1, 2, 3, 3, 4, 4, 5};
        int[] exp_result = {2, 5};
        LinkedListNode listNode = new LinkedListNode(list);

        System.out.println("Before Removing Duplicates:");
        listNode.printList();

        System.out.println("\nAfter Removing Duplicates:");
        listNode = remove_duplicates_completely_linkedlist(listNode);
        listNode.printList();

        System.out.println("\nExpected Result:");
        System.out.println(Arrays.toString(exp_result));

    }

    public static LinkedListNode remove_duplicates_completely_linkedlist(LinkedListNode head) {
        HashMap<Integer, Integer> map = new HashMap<>();
        LinkedListNode node = head;

        while(node != null) {
            if(map.containsKey(node.data)) {
                int val = map.get(node.data);
                map.put(node.data, ++val);
            } else {
                map.put(node.data, 1);
            }
            node = node.next;
        }

        node = head;
        LinkedListNode prev = null;

        while(node.next != null) {
            if(map.get(node.data) > 1) {
                if(prev != null) {
                    prev.next = node.next;
                }
            } else if (map.get(node.data) == 1) {
                if(prev == null) {
                    prev = node;
                    head = prev;
                } else {
                    prev.next = node;
                    prev = prev.next;
                }
            }
            node = node.next;
        }

        if(prev == null) head = prev;
        return head;
    }
}
