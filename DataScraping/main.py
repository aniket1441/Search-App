# FINDING KEYWORD FROM QUESTIONS
import json
from posixpath import split
import time
from cmath import log
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from ctypes import sizeof
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gettext import find
from itertools import count
from nltk import tokenize
from operator import itemgetter
import math
import re
from scipy import spatial
import nltk
from keybert import KeyBERT

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


cred = credentials.Certificate('')
firebase_admin.initialize_app(cred)
db = firestore.client()


# with open('quetion.txt') as f:
#     lines = f.readlines()

# find another way to find keyword its not woring very well
kw_model = KeyBERT()

# extrcating all keyword finding length and storing in set
# for line in lines:


# def getKeywords(line):
#     line = re.sub('[^A-Za-z0-9]+', ' ', line)
#     words = kw_model.extract_keywords(line)
#     for each_word in words:
#         my_set.add(each_word[0])


# count = 1
# for i in range(1, 101):
#     data = db.collection('questions').document(str(count)).get()
#     time.sleep(1)
#     x = data.to_dict()
#     getKeywords(x['dataVector'])
#     count = count+1


# key_words_length = len(my_set)
# print(key_words_length)
# print(my_set)

my_set = {'sumclosed', 'clocktime', 'computation', 'array', 'substringinputeach', 'permutationinputthe', 'xoutputfor', 'pmodq', 'arraythe', 'java', 'walktime', 'zeroinputthe', 'forest', 'treesthere', 'locks', 'palindromewe', 'shufflingtime', 'outputcopyyesnonotetest', 'polycarps', 'stones', 'palindromic', 'creepinessinputthe', 'operationsin', 'constraintstime', 'colors', 'trainstime', 'smallestpermutation', 'cell', 'robottime', 'linguisticstime', 'stringfind', 'operationsinputthe', 'permutationtime', 'integer', 'integershere', 'gambling', 'pointer', 'treesmisha', 'distances', 'swapping', 'arrangementinputthe', 'decreasing', 'queries', 'ijx', 'distance', 'bitwise', 'vertex', 'permutationinputthere', 'clockoutputfor', 'participants', 'weightinputthe', 'pipes', 'permutation', 'reduce', 'trains', 'vertices', 'map', 'abc', 'trapsexampleinputcopy', 'path', 'clock', 'minimizes', 'difftime', 'lexicographically', 'remainder', 'bipartite', 'noexampleinputcopycabcabababbabcbbaacbbcaabababccbbababaacbaaboutputcopyyesnoyesyesno', 'weights', 'maximized', 'multiset', 'store', 'universe', 'sequences', 'multisetit', 'shuffled', 'substringstime', 'digits', 'trees', 'sum', 'subrectangle', 'carriages', 'sumclosedin', 'swappingtime', 'testcase', 'grid', 'arrayinputthe', 'traps', 'tree', 'xor', 'trapsinputthe', 'shift', 'gensokyorecall', 'taskinputthe', 'puzzles', 'sequence', 'cellsexampleinputcopy', 'infectedthe', 'patchouli', 'segment', 'brackets', 'moves', 'problemtime', 'paths', 'adaptiveinputthe', 'arrangements', 'operations', 'stripe', 'nodesthe', 'treeoutputprint', 'bracketsthe', 'rounds', 'sequenceit', 'coins', 'orz', 'casexmodymodymodzmodzmodxmod', 'palindrome', 'bracket', 'groupstime', 'solutions', 'graphs', 'treethe', 'producttime', 'railways', 'concatenating', 'operationsexampleinputcopy', 'purchaseexampleinputcopy', 'cells', 'pedestals', 'shortest', 'speeds', 'secondsmemory', 'bishop', 'packing', 'token', 'inputoutputstandard', 'consecutive', 'enchanted', 'circular', 'segmentstime', 'constraintsinputthe', 'distinct',
          'orztime', 'treestime', 'platform', 'evenexampleinputcopy', 'rows', 'mushroomsit', 'optimallyinputthe', 'reverse', 'mushroom', 'substrings', 'board', 'casino', 'goods', 'operationsinputeach', 'aij', 'subtree', 'minimizationtime', 'nodes', 'permutationoutputoutput', 'compute', 'minimaxtime', 'minimal', 'coloringtime', 'determine', 'arrayoutputfor', 'tokens', 'pairsthe', 'subarrays', 'testcasesthe', 'trap', 'bishopinputthe', 'integersthe', 'arrangement', 'sandtime', 'euclid', 'rearrangement', 'rounding', 'dominoestime', 'answerexampleinputcopy', 'bishoptime', 'creeptime', 'carriage', 'city', 'row', 'energy', 'subarray', 'matrixtime', 'knipipiinputthere', 'segmentsexampleinputcopy', 'subarraystime', 'lockstime', 'test', 'binary', 'vvlcmb', 'mushrooms', 'concatenation', 'graph', 'marathontime', 'exceed', 'subsequence', 'pilesit', 'treetime', 'permutationthe', 'permutations', 'indices', 'marathon', 'optimal', 'domino', 'constraints', 'pedestal', 'integers', 'algorithm', 'constraint', 'decrement', 'permutationforces', 'digit', 'color', 'tokensthe', 'treeit', 'megabytesinputstandard', 'gamblingtime', 'sumclosedinputthe', 'queue', 'pilesoutputfor', 'maximizationtime', 'segments', 'mathematics', 'eveninputeach', 'purchases', 'walking', 'pathtime', 'tasks', 'operation', 'shuffledyou', 'treeyou', 'integerlets', 'chessboard', 'abbcacn', 'sitting', 'systems', 'cities', 'universetime', 'swap', 'palindromein', 'swaps', 'palindromes', 'matrix', 'platforms', 'maximum', 'robot', 'taskstime', 'railway', 'reversaltime', 'zeroes', 'shuffling', 'substring', 'ai', 'sumtime', 'treeeach', 'blocks', 'smallest', 'conditions', 'good', 'lock', 'jm', 'infected', 'balanced', 'concatenate', 'strings', 'pairs', 'minimize', 'segmentits', 'pipe', 'keshi', 'trapstime', 'walk', 'ij', 'roads', 'treethen', 'alphabet', 'shuffle', 'dividing', 'task', 'guessingtime', 'numberstest', 'sort', 'permuting', 'arraytime', 'stringtime', 'groups', 'arrayit', 'shoes', 'string', 'piles', 'pile', 'columns', 'mushroomstest', 'arrays', 'dominoes', 'sand'}
key_words_length = len(my_set)
# # myMap store index of each keyword
myMap = dict()
count = 0
for x in my_set:
    myMap[x] = count
    count = count+1

# finalVector = []

# # # for each question calculating tf
# count = 1
# for i in range(1,4):
#     data = db.collection('questions').document(str(count)).get()
#     time.sleep(1)
#     x = data.to_dict()
#     words = x['dataVector']
#     words = words.split()
#     print(words)
#     total = 0
#     v1 = [0] * (key_words_length)
#     for each_word in words:
#         if each_word in my_set:
#             index = myMap[each_word]
#             v1[index] = v1[index]+1
#             total = total + 1
#     v1 = [a/total for a in v1]
#     count = count+1
#     finalVector.append(v1)


# idfVector = [0]*(key_words_length)


# # calculating idf for each key word
# for vector in finalVector:
#     for index in range(key_words_length):
#         idfVector[index] = idfVector[index] + (vector[index] > 0)

# for index in range(key_words_length):
#     if(idfVector[index] == 0):
#         idfVector[index] = math.log(1)
#     else:
#         idfVector[index] = math.log(100/idfVector[index])

# count = 1
# # created final vectors storing importance of each keyword in question
# for vector in finalVector:
#     for index in range(key_words_length):
#         vector[index] = (vector[index] * (idfVector[index]))
#     db.collection('questions').document(str(count)).update({'vector': vector})
#     time.sleep(1)
#     count = count+1
#     print("done")
#     print(count)
#     print(vector)


# print(idfVector)
s = "array is maximum "

idfVector = [0.0, 4.605170185988092, 1.7147984280919266, 0.0, 0.0, 0.0, 0.0, 4.605170185988092, 0.0, 3.2188758248682006, 0.0, 0.0, 0.0, 4.605170185988092, 0.6733445532637655, 0.0, 0.0, 0.0, 3.506557897319982, 4.605170185988092, 1.9661128563728327, 4.605170185988092, 1.7719568419318754, 0.0, 4.605170185988092, 0.0, 0.0, 0.0, 0.0, 0.0, 2.5257286443082556, 0.0, 0.0, 2.302585092994046, 0.0, 0.0, 0.0, 3.912023005428146, 0.0, 4.605170185988092, 3.506557897319982, 3.912023005428146, 3.912023005428146, 4.605170185988092, 0.0, 4.605170185988092, 0.0, 0.0, 4.605170185988092, 0.0, 4.605170185988092, 3.912023005428146, 0.0, 4.605170185988092, 4.605170185988092, 3.912023005428146, 0.0, 0.9942522733438669, 4.605170185988092, 4.605170185988092, 4.605170185988092, 0.0, 0.0, 3.2188758248682006, 2.407945608651872, 4.605170185988092, 0.0, 4.605170185988092, 0.5276327420823719, 0.0, 4.605170185988092, 0.0, 3.912023005428146, 0.0, 4.605170185988092, 4.605170185988092, 4.605170185988092, 4.605170185988092, 4.605170185988092, 4.605170185988092, 4.605170185988092, 0.0, 1.5606477482646683, 2.407945608651872, 0.0, 2.5257286443082556, 0.0, 0.0, 2.659260036932778, 2.995732273553991, 4.605170185988092, 3.912023005428146, 0.0, 3.912023005428146, 0.0, 0.0, 4.605170185988092, 2.407945608651872, 3.2188758248682006, 4.605170185988092, 4.605170185988092, 0.0, 0.0, 0.0, 0.0, 3.912023005428146, 0.0, 3.912023005428146, 0.0, 0.0, 2.407945608651872, 0.0, 1.7719568419318754, 3.912023005428146, 0.0, 3.506557897319982, 2.302585092994046, 4.605170185988092, 2.207274913189721, 4.605170185988092, 4.605170185988092, 4.605170185988092, 4.605170185988092, 3.912023005428146, 0.0, 3.506557897319982, 2.302585092994046, 4.605170185988092, 4.605170185988092, 4.605170185988092, 3.506557897319982, 2.0402208285265546, 0.0, 2.5257286443082556, 0.0, 4.605170185988092, 4.605170185988092, 3.912023005428146, 3.912023005428146, 3.912023005428146, 4.605170185988092, 0.0, 0.0, 0.0, 0.0, 0.0, 4.605170185988092, 0.0, 3.506557897319982, 4.605170185988092, 0.47803580094299974,
             2.0402208285265546, 4.605170185988092, 3.912023005428146, 4.605170185988092, 0.0, 0.0, 4.605170185988092, 0.0, 1.3093333199837622, 3.912023005428146, 4.605170185988092, 4.605170185988092, 4.605170185988092, 3.912023005428146, 0.0, 0.0, 4.605170185988092, 0.083381608939051, 0.0, 0.0, 4.605170185988092, 4.605170185988092, 0.0, 0.0, 0.0, 4.605170185988092, 2.659260036932778, 0.0, 4.605170185988092, 3.912023005428146, 3.912023005428146, 0.0, 3.912023005428146, 4.605170185988092, 4.605170185988092, 4.605170185988092, 0.0, 0.0, 3.2188758248682006, 2.659260036932778, 0.0, 3.2188758248682006, 0.0, 4.605170185988092, 0.0, 0.0, 0.0, 0.0, 3.912023005428146, 0.0, 0.0, 0.0, 4.605170185988092, 4.605170185988092, 2.659260036932778, 2.995732273553991, 0.07257069283483537, 0.0, 3.2188758248682006, 3.912023005428146, 0.0, 2.659260036932778, 1.2039728043259361, 4.605170185988092, 4.605170185988092, 2.995732273553991, 4.605170185988092, 0.0, 0.0, 0.0, 3.912023005428146, 0.0, 4.605170185988092, 2.302585092994046, 0.0, 3.912023005428146, 0.0, 0.0, 4.605170185988092, 3.506557897319982, 0.0, 0.0, 0.0, 4.605170185988092, 0.0, 3.506557897319982, 0.0, 4.605170185988092, 4.605170185988092, 0.0, 0.0, 3.912023005428146, 2.120263536200091, 0.0, 2.5257286443082556, 2.5257286443082556, 2.302585092994046, 0.0, 0.0, 2.8134107167600364, 2.8134107167600364, 1.171182981502945, 4.605170185988092, 2.5257286443082556, 4.605170185988092, 0.0, 4.605170185988092, 2.995732273553991, 2.302585092994046, 0.0, 0.0, 0.0, 0.0, 0.0, 4.605170185988092, 2.8134107167600364, 0.0, 4.605170185988092, 3.912023005428146, 0.0, 4.605170185988092, 0.0, 4.605170185988092, 0.0, 0.0, 0.0, 4.605170185988092, 3.912023005428146, 0.0, 0.0, 0.0, 4.605170185988092, 3.506557897319982, 3.506557897319982, 4.605170185988092, 4.605170185988092, 4.605170185988092, 0.0, 0.0, 0.0, 4.605170185988092, 3.506557897319982, 2.207274913189721, 3.2188758248682006, 2.995732273553991, 4.605170185988092, 3.2188758248682006, 2.995732273553991, 4.605170185988092, 4.605170185988092]


s = re.sub('[^A-Za-z0-9]+', ' ', s)
words = s.split()
total = 0
v1 = [0] * (key_words_length)
for each_word in words:
    if each_word in my_set:
        index = myMap[each_word]
        print(each_word, index)
        v1[index] = v1[index]+1
        total = total + 1
v1 = [a/total for a in v1]

print(s)
print(v1)

for i in range(key_words_length):
    v1[i] = v1[i]*idfVector[i]

simVector = []

count = 1

for i in range(1, 101):
    data = db.collection('questions').document(str(count)).get()
    data = data.to_dict()
    print(data['vector'])
    # time.sleep(0.5)
    result = 1 - spatial.distance.cosine(v1, data['vector'])
    if result > 0:
        simVector.append((result, count))
    count = count+1

print(simVector)
