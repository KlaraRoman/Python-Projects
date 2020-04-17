vowels=("a","e","i","o","u")
word=str(input("Please put a word: ")).lower()

new_word=""
 
for l in word:
    if l not in vowels:
        new_word += l
        continue
    
print(new_word)
        
      
    
        
    
        
    
        
