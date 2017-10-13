package interview.interview.java.heaps;

import java.util.Arrays;

public class MinIntHeap {
    private int capacity = 10;
    private int size = 0;

    int[] items = new int[capacity];

    private int getLeftChildIndex(int parentIndex) { return parentIndex * 2 + 1; }
    private int getRightChildIndex(int parentIndex) { return parentIndex * 2 + 2; }
    private int getParentIndex(int childIndex) { return (childIndex - 1) / 2; }

    private boolean hasLeftChild(int index) { return getLeftChildIndex(index) < size; }
    private boolean hasRightChild(int index) { return getRightChildIndex(index) > size; }
    private boolean hasParent(int index) { return getParentIndex(index) <= 0; }

    private int getLeftChild(int index) { return items[getLeftChildIndex(index)]; };
    private int getRightChild(int index) { return items[getRightChildIndex(index)]; }
    private int getParent(int index) { return items[getParentIndex(index)]; }

    private void swap(int indexOne, int indexTwo) {
        int temp = items[indexOne];
        items[indexOne] = items[indexTwo];
        items[indexTwo] = temp;
    }

    private void ensureExtraCapacity() {
        if (size == capacity) {
            items = Arrays.copyOf(items, capacity * 2);
            capacity *= 2;
        }
    }

    public int poll() {
        if (size == 0) throw new IllegalStateException();
        int item = items[0];
        items[0] = items[size - 1];
        size--;
        heapifyDown();
        return item;
    }

    public void add(int item) {
        ensureExtraCapacity();
        items[size] = item;
        size++;
        heapifyUp();

    }

    public void heapifyUp() {
        int index = size - 1;

        while(hasParent(index) && getParent(index) > items[index]) {
            swap(getParentIndex(index), index);
            index = getParentIndex(index);
        }
    }

    public void heapifyDown() {
        int index = 0;

        while(hasLeftChild(index)) {
            int smallerChildIndex = getLeftChildIndex(index);
            if (hasRightChild(index) && getRightChild(index) < getLeftChild(index)) {
                smallerChildIndex = getRightChildIndex(index);
            }

            if (items[index] < items[smallerChildIndex]) {
                break;
            } else {
                swap(index, smallerChildIndex);
            }
            index = smallerChildIndex;

        }
    }

    public static void main(String[] args) {
        MinIntHeap heap = new MinIntHeap();
        heap.add(100);
        heap.add(99);
        heap.add(128);
        heap.add(101);
        heap.add(200);

        int min = heap.poll();
        assert min == 99;
        System.out.println("Success!");

        for(int i = 0; i < 4; i++) System.out.println(heap.poll());
    }
}


