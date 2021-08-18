##This is a function to reverse string.
def reverseString(self, s: List[str]) -> None:
        if (len(s)==1):
            pass
        else:
            for i in range(0,len(s)//2):
                s[len(s)-i-1],s[i] = s[i],s[len(s)-i-1]
