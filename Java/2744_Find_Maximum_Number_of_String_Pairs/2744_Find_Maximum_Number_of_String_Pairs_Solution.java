class Solution {
    public int maximumNumberOfStringPairs(String[] words) {
        int pair = 0;

        for (int i = 0; i < words.length; i++) {
            String select = words[i];
            String tmp = "";

            for (int j = 0; j < select.length(); j++) {
                tmp = select.charAt(j) + tmp;
            }

            for (int j = i + 1; j < words.length; j++) {
                if (tmp.equalsIgnoreCase(words[j])) {
                    pair++;
                }
            }
        }

        return pair;
    }
}
