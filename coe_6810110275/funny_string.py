def funnyString(s: str) -> str:
    diffs = []
    
    for i in range(1, len(s)):
        diff = abs(ord(s[i]) - ord(s[i-1]))
        diffs.append(diff)
        
    if diffs == diffs[::-1]:
        return "Funny"
    else:
        return "Not Funny"
