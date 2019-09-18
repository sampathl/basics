#Backspace String Compare
"""Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:

    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.
"""

def createString(st:str):
    slist=[]
    for i in st :
        if i == '#':
            if len(slist) >0 :
                slist.pop()
        else :
            slist.append(i)
    
    return ''.join(slist)

def backspaceCompare(S: str, T: str) -> bool:
    s1= createString(S)
    t1= createString(T)
    print(s1, t1 ,sep='\n')
    return s1 == t1 

backspaceCompare("xywrrmp","xywrrmu#p")