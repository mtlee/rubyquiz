import os.path 
import random 
import string

HEREDIR = os.path.abspath(os.path.dirname(__file__)) 
heights=os.path.join(HEREDIR, '768.txt') 

def mung(filename): 
    f=open(filename, 'r').readlines() 
    
    for line in f: 
        if not line: 
            pass 
        #call the scramble method to actually scramble each bit of text separated by whitespace, and add a space
        else: 
            k= line.split()
            munged_text=''
            for word in k: 
                munged_text= munged_text + ' '+ scramble(word)
            print munged_text
        

#I feel like this could have been better written, it took me a while to get to work, and there must be a more clever way
def scramble(word):
    #l is going to be my list of not-yet-assigned spots/orders for text
    l=range(len(word))
    #new is a list containing entries (spot, char) which I then use to put toghether the word
    new=[]
    #first take out all of the punctuation and put it in the same spot 
    for index, char in enumerate(list(word)):
        if char.strip(string.punctuation)=='': 
            new.append((index, char))
            #remove the punct so that l now only contains unassigned spots for alpha-numerics 
            l.remove(index)
    
    #now go through again and put the first and last alpha numerics in same place, use a new 'for' loop because now l[0] and l[-1] will be our first and last alpha numerics        
    for index in l: 
        if index ==l[0] or index==l[-1]: 
            new.append((index, list(word)[index]))
            #remove the first and last so that l now only contains unassigned spots for those characters that need to be scrambled
            l.remove(index)
    
    #create a copy of l, shuffle them, create a dict: spot->char
    k=l[:]
    random.shuffle(k)
    spot_to_char=dict(zip(l, k))
    
    for index in l: 
        new.append((index, list(word)[spot_to_char[index]]))
    
    # sort the 'new' list so that the spot numbers are in order  
    new.sort()
    newword=''                    
    #append each char 
    for char in new: 
        newword = newword + char[1]
    return newword

mung('768.txt') 
