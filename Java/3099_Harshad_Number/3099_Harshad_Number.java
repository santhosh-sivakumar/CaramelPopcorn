class Solution {
    public int sumOfTheDigitsOfHarshadNumber(int x) {
        int sum = 0, tmp = x;

        while(tmp > 0)
        {
            sum += tmp%10;
            tmp /= 10;
        }

        if(x%sum == 0)
            return sum;
        else
            return -1;

    }
}