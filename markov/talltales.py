import os.path 
import random 

HEREDIR = os.path.abspath(os.path.dirname(__file__)) 
walt= os.path.join(HEREDIR, '1322.txt') 

def weavetale(filename, startword, sentence_count): 
    f=open(filename, 'r').readlines() 
    d={}
    
    #create this dictionary by reading through the document d:{word}-->[list of words that follow it]
    for line in f: 
        if not line: 
            pass 
        else: 
            k=line.split() 
            for index in range(len(k)-1): 
                if not k[index] in d: 
                    d[k[index]]=[k[index+1]]
                else: 
                    d.get(k[index]).append(k[index+1])
    
    #print d.items()
                
    #start telling the story 
    count = 0
    tale = startword 
    while count < sentence_count: 
        if not d.get(startword):
            startword='this'
            tale + '\n' + startword     
        #randomly chose a following word to tack on 
        randno=random.randrange(0,len(d.get(startword)))
        tale = tale + ' '+ d.get(startword)[randno]
        #newline for punctuation 
        for punct in ['.', '?', '!']: 
            if d.get(startword)[randno].endswith(punct):
                tale = tale +'\n'
        #newline if too long
        if count %10 ==0: 
            tale = tale + '\n'
        #get ready for next iteration
        startword =d.get(startword)[randno]
        count +=1 
        
    print tale +'.'

 

weavetale(walt, 'this', 100)
    
    
    
