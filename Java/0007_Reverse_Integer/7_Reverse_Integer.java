import java.util.*;
class Solution {
    public int reverse(int x) {
        long rev = 0;
        int tmp = x;

        if(x > 0) 
        {
            while(tmp != 0)
            {
                rev = rev * 10 + tmp % 10;
                tmp = (int) tmp / 10;

                if (rev > Integer.MAX_VALUE || rev < Integer.MIN_VALUE)
                    return 0;
            }

            return (int)rev;
        }
        else if(x == 0)
        {
            return 0;
        }
        else
        {
            tmp = tmp*(-1);

            while(tmp != 0)
            {
                rev = rev * 10 + tmp % 10;
                tmp = tmp / 10;

                if (rev > Integer.MAX_VALUE || rev < Integer.MIN_VALUE)
                    return 0;

            }

            rev = rev * (-1);
            return (int)rev;
        }
    }
}