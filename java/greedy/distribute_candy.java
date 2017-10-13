package interview.interview.java.greedy;

public class distribute_candy {

    public void main(String[] args) {
        int[] ratings = {1, 3, 4, 2};
        int result = candy(ratings);
        assert result == 7;
        System.out.println("Success!");
    }

    public static int candy(int[] ratings) {
        if(ratings == null || ratings.length == 0) return 0;

        int[] candies = new int[ratings.length];
        candies[0] = 1;

        // ascending
        for(int i = 1; i < ratings.length; i++) {
            if(ratings[i] > ratings[i - 1]){
                candies[i] = candies[i - 1] + 1;
            } else {
                candies[i] = 1;
            }
        }

        int result = candies[ratings.length - 1];

        // descending
        for(int i = ratings.length - 2; i >= 0; i--) {
            int curr = 1;
            if(ratings[i] > ratings[i + 1]) {
                curr = candies[i+1] + 1;
            }

            result += Math.max(curr, candies[i]);
            candies[i] = curr;
        }

        return result;
    }
}
