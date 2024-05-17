class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        if( ruleKey == 'type'):
            OUT = list( filter( lambda x : x[0] == ruleValue, items ) )
        elif( ruleKey == 'color'):
            OUT = list( filter( lambda x : x[1] == ruleValue, items ) )
        elif( ruleKey == 'name'):
            OUT = list( filter( lambda x : x[2] == ruleValue, items ) )
        
        return len( OUT )