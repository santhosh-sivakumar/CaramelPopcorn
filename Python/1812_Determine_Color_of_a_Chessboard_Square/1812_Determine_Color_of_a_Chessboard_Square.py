class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        chess = {
            "a": [0, 1, 0, 1, 0, 1, 0, 1],
            "b": [1, 0, 1, 0, 1, 0, 1, 0],
            "c": [0, 1, 0, 1, 0, 1, 0, 1],
            "d": [1, 0, 1, 0, 1, 0, 1, 0],
            "e": [0, 1, 0, 1, 0, 1, 0, 1],
            "f": [1, 0, 1, 0, 1, 0, 1, 0],
            "g": [0, 1, 0, 1, 0, 1, 0, 1],
            "h": [1, 0, 1, 0, 1, 0, 1, 0],
        }
        
        A = coordinates[0]
        B = int(coordinates[1])

        return chess[A][B - 1]