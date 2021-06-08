#Remove vowels

#Write a function that will remove all vowels from a given string. The function should return a string.
#Example:
#Input: ‘Joel’
#Output: ‘Jl’

def rem_vowel(str):
    newStr = ""
    vowel = ("a,e,i,o,u,A,E,I,O,U")
    for x in str:
        if x not in vowel:
            newStr += x
    return newStr

print(rem_vowel('Joel'))
            
    

        
