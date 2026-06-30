#Question no 1:-
def analyze_string(s):
    if s=="":
        print("Empty string is entered")
        return
    
    print("string length=",len(s))
    print("Reverse a string using slicing=",s[::-1])
     
    count=0
    for ch in s:
        if ch in "aeiou":
            count+=1
    print("Number of vowels=",count)
    i=0
    for i in range(len(s)):
        print("character:",s[i],":","positive index=",i,":","Negative index=",i-len(s))
string=input("Enter any string:")
analyze_string(string)       
