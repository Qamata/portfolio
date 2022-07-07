#****************** Compulsory Task 1 ******************
import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp('cat')
word2 = nlp('monkey')
word3 = nlp('banana')


print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''
I think it is quite impressive how the model is able to realise
the close relation of 'cat' and 'monkeys' in that they are both animals
in comparison to 'monkey' and 'banana'

'''

tokens = nlp('cat apple monkey banana money human') 
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

'''
I added the strings 'money' and 'human' to the tokens.
I found it odd that 'money' and 'monkey' have a similarity almost equal
that of 'money' and human. I attribute this to the shared latters between
'money' and 'monkey'

I ran the example file on the 'en_core_web_sm' model
The simpler model was less accurate with 'banana' being more similar
to 'cat' than 'monkey' which is absolutely incorrect.
'''

#**************** Compulsory Task 2 ****************

def to_watch(description):
    '''
    This funtion returns a suggests the most similar movie to watch
    next by comparing the descriptions of the recently watched movie
    as input to multiple other movies
    '''
    nlpHulk = nlp(description)
    sentence = nlp(nlpHulk)
    similarities = []

    with open("movies.txt") as options:    # Opening 'movies' text file
        Movie_list = options.read().splitlines()
        for sentences in Movie_list:
            similarity = nlp(sentences).similarity(sentence)
            similarities.append(similarity)
    index = similarities.index(max(similarities)) #Index of movie description
                                                  #with highest similarity
    suggestion = Movie_list[index]   
    print(f'{suggestion[0:7]} is similar to Planet Hulk')
            


planetHulk = ('Will he save their world or destroy it? When the Hulk becomes'
              'too dangerous for the Earth, the Illuminati trick Hulk into a'
              'shuttle and launch him into space to a planet where the Hulk'
              'can live in peace. Unfortunately, Hulk land on the planet Sakaar'
              ' where he is sold into slavery and trained as a gladiator.')
to_watch(planetHulk) # Calling to_watch funtion with Planet Hulk as input


        
        
        


        
            
