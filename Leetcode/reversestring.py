def reverse(s):
    j= len(s)-1
    i = 0
    while i<j:
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i+=1
        j-=1
    
    return s












s =["h","e","l","l","o"]
print(reverse(s))