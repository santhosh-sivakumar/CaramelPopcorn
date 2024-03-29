import java.util.*;

class Solution {
    char arr[] = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
    
    public int romanToInt(String s) {
        int val = 0;
        for(int i = 0; i < s.length(); i++)
        {
            char curr = s.charAt(i), next;
            if(i == s.length() - 1)
                next = ' ';
            else
                next = s.charAt(i+1);
            
            if(curr == 'I')
            {
                if(next != 'V' && next != 'X')
                    val += 1;
                else
                    val -= 1;
            }
            else if(curr == 'V')
            {
                val += 5;
            }
            else if(curr == 'X')
            {
                if(next != 'L' && next != 'C')
                    val += 10;
                else
                    val -= 10;
            }
            else if(curr == 'L')
            {
                val += 50;
            }
            else if(curr == 'C')
            {
                if(next != 'D' && next != 'M')
                    val += 100;
                else
                    val -= 100;
            }
            else if(curr == 'D')
            {
                val += 500;
            }
            else if(curr == 'M')
            {
                val += 1000;
            }
        }
        return val;
    }
}