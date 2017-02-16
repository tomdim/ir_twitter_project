import numpy as np
import xlrd
from scipy import spatial
import codecs

#---------------------------------------
#tweets of week 1 or 2
week = 1
#---------------------------------------

def parseLex(f):
    lex = []
    workbook = xlrd.open_workbook(f, 'utf-8')
    worksheet = workbook.sheet_by_index(0)
    for i in range(1, worksheet.nrows):
        lex.append(worksheet.cell(i,2).value)
        
    return lex

def checkNearestTerms(terms, minIndexes, _sentiment, lex):
    numOfPositives = 0
    numOfNegatives = 0
    newPos = []
    newNeg = []
    if (_sentiment == 'positive'):
        for i in range(0, len(minIndexes)):
            if terms[minIndexes[i]] in lex:
                numOfPositives += 1
            else:
                newPos.append(terms[minIndexes[i]])
        print 'Average number of positive nearest terms is: ', numOfPositives/float(len(minIndexes))
        print '*** New Positive terms ***'
        for i in range(0, len(newPos)):
            print newPos[i]
    elif (_sentiment == 'negative'):
        for i in range(0, len(minIndexes)):
            if terms[minIndexes[i]] in lex:
                numOfNegatives += 1
            else:
                newNeg.append(terms[minIndexes[i]])
        print 'Average number of negative nearest terms is: ', numOfNegatives/float(len(minIndexes))
        print '*** New Negative terms ***'
        for i in range(0, len(newNeg)):
            print newNeg[i]       
                
def saveNearestTerms(p, terms, term, minIndexes, pos_lex, neg_lex):
    if term in pos_lex:
        f = codecs.open("ext%s/%s/ExtPos(%s).txt" % (week, p, term), "w+", "utf-8")
        print 'Term is Positive!'
        checkNearestTerms(terms, minIndexes, 'positive', pos_lex)
    else:
        f = codecs.open("ext%s/%s/ExtNeg(%s).txt" % (week, p, term), "w+", "utf-8")
        print 'Term is Negative!'
        checkNearestTerms(terms, minIndexes, 'negative', neg_lex)
        
    for i in range(0, len(minIndexes)):
        f.write(terms[minIndexes[i]] + '\n')
    f.close()
    
def minValues(v, p, term, terms):
    if p == 1:
        _min = v[0]
        _minInd = 0
        for j in range(1, len(v)):
            if _min == 0:
                _min = v[j]
                _minInd = j
            if v[j] < _min and term <> terms[_minInd]:
                _min = v[j]
                _minInd = j
        
        return _minInd
    else:
        minIndexes = []
        tmp = v
        tmp = np.sort(tmp)
        minVals = tmp[:p+1,]  
        _threshold = p          
        for i in range(0, v.shape[0]):
            if(_threshold == 0):
                break
            if v[i] in minVals and term <> terms[i]:
                _threshold -= 1
                minIndexes.append(i)
        
        return minIndexes
    
def p_nearest_terms(distances, terms, p, pos_lex, neg_lex):
    print '\n\n****************************************** %s-nearest terms ******************************************' % p
    for i in range(0, distances.shape[0]):
        minIndexes = []
        minIndex = -1
        if((terms[i] not in pos_lex) and (terms[i] not in neg_lex)):
            continue
        print '***************************************************'                
        if p == 1:    
            minIndex = minValues(distances[i, :], p, terms[i], terms)
            print 'nearest term of', terms[i], 'is : ', terms[minIndex]
            minIndexes.append(minIndex)
        else:
            minIndexes = minValues(distances[i, :], p, terms[i], terms)
            print 'nearest terms of', terms[i], 'are : '
            for j in range(0, len(minIndexes)):
                print terms[minIndexes[j]]
        
        saveNearestTerms(p, terms, terms[i], minIndexes, pos_lex, neg_lex)
        
        print '***************************************************'
'''
*********************************************************************************
'''
terms = []    
documents = []

#Parse tweets and store in documents and terms vectors
path = 'results_week%s/tweets_week%s.txt' % (week, week)
with codecs.open(path,'r',encoding='utf8') as f:
    documents = f.readlines()
    tmp = []
    for i in range(0, len(documents)):
        tmp = documents[i].split()
        for j in range(0, len(tmp)):
            if tmp[j] not in terms:
                terms.append(tmp[j].strip())  

pos_lex = parseLex('PosLex.xls')
print 'pos_lex:', len(pos_lex)
neg_lex = parseLex('NegLex.xls')
print 'neg_lex:', len(neg_lex)
X = np.zeros((len(terms), len(documents)))

#array term in document
for i in range(0, len(terms)):
    t = terms[i]
    for j in range(0, len(documents)):
        tmp = documents[j].split()
        for k in range(0, len(tmp)):
            if t == tmp[k]:
                X[i][j] = 1

print X
print 'X size: ', X.shape, '\n'

c = 0
tmp = []
for i in range(0, len(terms)):
    s = 0
    for j in range(0, len(documents)):
        s += X[i][j]
    if s > 1:
        c += 1
        tmp.append(terms[i])

terms = None
terms = tmp        
tmp = None

print "terms found in more than one documents: ", c 
print 'terms size', len(terms)

bad_rows = np.nonzero(np.sum(X,axis=1) < 2)

X = np.delete(X, bad_rows, axis=0)
print X
print 'X size: ', X.shape, '\n'

print '\n******SVD ANALYSIS******\n\n'
U, S, V = np.linalg.svd(X, full_matrices=True)   
print '\n****** U ******\n'
print U
print 'U size: ', U.shape
print '\n****** S ******\n'
print S
print 'S size: ', S.shape
print '\n****** V ******\n'
print V
print 'V size: ', V.shape

print '\n******Uk (k =100)******\n\n'
Uk = np.empty([len(terms),100])
Uk = U[:,:100]
print Uk
print 'Uk shape: ', Uk.shape

print '\n******EUCLIDEAN DISTANCE******\n\n'
distances = np.zeros((len(terms), len(terms)))
print distances
print 'distances: ', distances.shape

print 'Uk shape[0]', Uk.shape[0]
for i in range(0, Uk.shape[0]):
    for j in range(0, Uk.shape[0]):
        distances[i][j] = spatial.distance.euclidean(Uk[i, :100], Uk[j, :100])

print '\n******DISTANCES ARRAY******\n\n'
print distances
print 'distances: ', distances.shape

p = [1, 2, 4, 5, 10]
for i in range(0, len(p)):
    p_nearest_terms(distances, terms, p[i], pos_lex, neg_lex)
