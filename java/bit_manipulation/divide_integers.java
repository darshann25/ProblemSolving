/**
 *
 Divide two integers without using multiplication, division and mod operator.

 Return the floor of the result of the division.

 Example:

 5 / 2 = 2
 Also, consider if there can be overflow cases. For overflow case, return INT_MAX.
 */

package interview.interview.java.bit_manipulation;

public class divide_integers {

    public static void main(String[] args) {
        int dividend = 100;
        int divisor = -2;

        int result = divide(dividend, divisor);
        assert result == -50;

        System.out.println("Success!");
    }

    public static int divide(int dividend, int divisor) {
        if(divisor == 0) return Integer.MAX_VALUE;
        if(divisor == -1 && dividend == Integer.MIN_VALUE) return Integer.MAX_VALUE;

        int sign = (dividend < 0) ^ (divisor < 0) ? -1 : 1;

        long tDivisor = Math.abs((long) divisor);
        long tDividend = Math.abs((long) dividend);
        int result = 0;

        while (tDividend >= tDivisor) {
            int numShifts = 0;
            while (tDividend >= (tDivisor << numShifts)) {
                numShifts++;
                //System.out.println(tDivisor);
            }
            result += 1 << (numShifts - 1);
            //System.out.println(result);
            tDividend -= (tDivisor << (numShifts - 1));
            //System.out.println(tDividend);
        }

        if (sign < 0) return -result;

        return result;

    }
}
