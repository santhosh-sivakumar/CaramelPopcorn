class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        OUT = []
        tmp = ''

        for i in words:
            tmp = ''
            for j in i:
                tmp += morse[ord(j) - 97]
            OUT.append(tmp)   

        return len(set(OUT))