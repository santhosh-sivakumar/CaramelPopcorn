class Solution {
    public boolean isPalindrome(int x) {
        int tmp = x, y = 0;

        if(tmp < 0)
            return false;
        else
        {
                    while(tmp != 0)
            {
                y = (y*10)+(tmp%10);
                tmp /= 10;
            }

            if(x == y)
                return true;
            return false;
        }
    }
}