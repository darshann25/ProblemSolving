package interview.interview.java.dynamic_programming;

public class max_product_subarray {

    public void main(String[] args) {
        final int[] arr = {2, 3 , -2, 4};
        int result = maxProduct(arr);
        assert result == 6;
        System.out.println("Success!");
    }

    // DO NOT MODIFY THE ARGUMENTS WITH "final" PREFIX. IT IS READ ONLY
    public static int maxProduct(final int[] A) {
        /*
        int[] optProd = new int[A.length + 1];
        Arrays.fill(optProd, 0);

        int maxProd = Integer.MIN_VALUE;

        for(int i = 1; i <= A.length; i++) {
            optProd[i] = Math.max(A[i-1], optProd[i-1] * A[i - 1]);
            //if(i > 1 && optProd[i - 1] == 0) optProd[i] = Math.max(A[i-1], A[i-2] * A[i - 1]);
            maxProd = Math.max(maxProd, optProd[i]);
        }

        return maxProd;
        */

        int maxEndHere = 0;
        int minEndHere = 0;
        int maxSoFar = 0;

        if(A.length == 0) return 0;

        for(int i = 0; i < A.length; i++) {
            int num = A[i];

            if(num > 0) {
                if(maxEndHere != 0) maxEndHere *= num;
                else maxEndHere = 1 * num;

                if(minEndHere != 0) minEndHere = Math.min(minEndHere * num, 1);
                else minEndHere = Math.min(minEndHere * num, 0);

            } else if (num == 0) {
                maxEndHere = 0;
                minEndHere = 0;
            } else {
                int temp = (maxEndHere == 0 ? 1 : maxEndHere);

                if (maxEndHere != 0) maxEndHere = Math.max(minEndHere * num, 1);
                else maxEndHere = Math.max(minEndHere * num, 0);

                minEndHere = temp * num;
            }

            //System.out.println(i + " || " + maxEndHere + " || " + minEndHere + " || " + maxSoFar);
            maxSoFar = Math.max(maxSoFar, maxEndHere);
        }

        return maxSoFar;

    }
}
