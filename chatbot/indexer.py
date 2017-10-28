#  Example code in python programming language demonstrating some of the features of an inverted index.
#  In this example, we scan a directory containing the corpus of files. (In this case the documents are reports on articles
#  and authors submitted to the Journal "Communications of the Association for Computing Machinery"
#
#  In this example we see each file being read, tokenized (each word or term is extracted) combined into a sorted
#  list of unique terms.
#
#  We also see the creation of a documents dictionary containing each document in sorted form with an index assigned to it.
#  Each unique term is written out into a terms dictionary in sorted order with an index number assigned for each term.
#  From our readings we know that to complete teh inverted index all that we need to do is create a third file that will
#  coorelate each term with the list of documents that it was extracted from.  We will do that in a later assignment.
##
#  We can further develop this example by keeping a reference for each term of the documents that it came from and by
#  developing a list of the documents thus creating the term and document dictionaries.
#
#  As you work with this example, think about how you might enhance it to assign a unique index number to each term and to
#  each document and how you might create a data structure that links the term index with the document index.


import sys,os,re
import time
import sqlite3
import nltk
# from nltk.corpus import stopwords

# Data Model
# The database is a simple dictionary
database = {}

# We will create a term object for each unique instance of a term
#
class Docs():
    terms = {}

class Term():
    termid = 0
    termfreq = 0
    docs = 0
    docids = {}

# split on any chars
def splitchars(line) :
    return chars.split(line)

# this small routine is used to accumulate query idf values
def elenQ(elen, a):
    return(float(math.pow(a.idf,2))+float(elen))

# this small routine is used to accumulate document tfidf values
def elenD(elen, a):
    valor = float(math.pow(a.tfidf,2))+float(elen)
    return(valor)


# split on an

# download stop words
nltk.download('stopwords')

# define global variables used as counters
tokens     = 0
documents  = 0
terms      = 0
termindex  = 0
docindex   = 0

# initialize list variable
#
alltokens = []
alldocs = []


# Capture the start time of the routine so that we can determine the total running
# time required to process the corpus
#
t2 = time.localtime()


# set the name of the directory for the corpus
#
dirname = "/Users/pulso8/Desktop/Data/_Desarrollo/of_v0.9.8_osx_release/apps/laboratorioAppsCulturales/chatbot/corpus"

# For each document in the directory read the document into a string
#
all = [f for f in os.listdir(dirname)]
for f in all:
    documents+=1
    with open(dirname+'/'+f, 'r') as myfile:
        alldocs.append(f)
        data=myfile.read().replace('\n', '')
        for token in data.split():
            alltokens.append(token)
            tokens += 1


# Open for write a file for the document dictionary
#
documentfile = open(dirname+'/'+'documents.txt', 'w')
alldocs.sort()

for f in alldocs:
  docindex += 1
  documentfile.write(f+','+str(docindex)+os.linesep)
documentfile.close()

#
# Sort the tokens in the list
alltokens.sort()

#
# Define a g list for the unique terms, s for stemmed terms
g=[]
s=[]
#
# Identify unique terms in the corpus
for i in alltokens:
    if i not in g:
       g.append(i)
       terms+=1
print("Raw terms: %i" % terms)

# Remove stopwords using nltk
filtered_g = [word for word in g if word not in nltk.corpus.stopwords.words('spanish')]
dif_g      = len(g) - len(filtered_g)
g          = filtered_g
terms      = len(g)
print("Terms without stopwords:  %i" % terms)

# Remove words not beginning with a number
filtered_g = [word for word in g if word[0].isalpha()]
dif_g2     = len(g) - len(filtered_g)
g          = filtered_g
terms      = len(g)
print("Terms without those those beginning with a number:  %i" % terms)

# Remove words with trailing not alphanumeric characters
filtered_g = []
pattern    = re.compile('\W')
for i in g:
    filtered_g.append(re.sub(pattern, '', i))
g          = filtered_g
terms      = len(g)
print("Terms without numeric terms:  %i" % terms)

# Sort and remove duplicates
sorted_g   = sorted(set(g))
g          = sorted_g
terms      = len(g)
print("Final number of unique terms filtered and sorted:  %i" % terms)


# Stem the terms using nltk
sno = nltk.stem.SnowballStemmer('spanish')
for i in g:
    s.append(sno.stem(i))


# wordfreq = []
# for w in alltokens:
#     wordfreq.append(alltokens.count(w))
#     print w + "," + str(alltokens.count(w))



# Output Index to disk file. As part of this process we assign an 'index' number to each unique term.
#
indexfile = open(dirname+'/'+'index.txt', 'w')

for i in g:
  termindex += 1
  indexfile.write(i+','+s[termindex-1]+','+str(alltokens.count(i))+','+str(termindex)+os.linesep)
indexfile.close()


# Print metrics on corpus
#
print("Processing Start Time: %.2d:%.2d" % (t2.tm_hour, t2.tm_min))
print("Documents %i" % documents)
print("Tokens %i" % tokens)
print("Terms %i" % terms)
print("Total number of stop words: %i" % dif_g)
print("Removed words with leading non alpha characters: %i" % dif_g2)

t2 = time.localtime()
print("Processing End Time: %.2d:%.2d" % (t2.tm_hour, t2.tm_min))
