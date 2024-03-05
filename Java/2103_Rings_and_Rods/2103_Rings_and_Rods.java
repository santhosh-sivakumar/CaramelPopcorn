class Solution {
    public int countPoints(String rings) {
        int len = rings.length();
        int n = len / 2;
        int arr[][] = new int[10][3]; // Increase array size to accommodate indices 0-9

        for (int i = 0; i < len; i = i + 2) {
            char color = rings.charAt(i);
            int index = (int)rings.charAt(i + 1) - '0';

            if (color == 'R')
                arr[index][0]++;
            else if (color == 'G')
                arr[index][1]++;
            else if (color == 'B')
                arr[index][2]++;
        }

        int count = 0;
        for (int i = 0; i < 10; i++) { // Update loop limit to match array size
            if (arr[i][0] != 0 && arr[i][1] != 0 && arr[i][2] != 0)
                count++;
        }

        return count;
    }
}