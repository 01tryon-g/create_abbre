# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 11:35:44 2022

@author: Tryon
"""
# =============================================================================
# #Run records
# %timeit find('girl')
# 5.13 ms ± 177 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# 
# %timeit finre('girl')
# 6.17 ms ± 338 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# 
# %timeit a('girl')
# 5.36 ms ± 233 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# 
# Don't be fooled by the above, with just %time, re is a lot faster.
# re is also a shorter code to write. if you are are only lookig for where the word occur???? i guess, this will not be so useful, so iterate.
# =============================================================================
import re
import time
from itertools import permutations, chain
from functools import partial, update_wrapper
from collections import defaultdict
from functools import lru_cache
import numpy as np

# from word_finder import Words
from data_bs import my_listnp, re_word_list, my_list
#%%

def finder(words, _input = None, max_=5):
    
    def iter_(a):
        b = [x for x in words if len(x) == lent and set(x).issubset(a)]
        b_inc = [x for x in words if set(x).issubset(a)]
        final_ = b if b else sorted(b_inc, key=len, reverse = True)
        if final_:
            return f'Your results are:\n{final_[:max_]} \n'
        else:
            return 'You have no result: try again' '\n'
        
    if _input is None:
        _input = input('Find the suitable abbreviation for: '.title())
    assert isinstance(_input, str)
        
    lent = len(_input)
    return iter_(_input.lower())


while True:
    try:    
        print(finder(my_list))
    except KeyboardInterrupt:
        print('\n...\nOps:\nSearch Process has been Terminated by user')
        break
    except Exception as err:
        print(f'Some other error has occured, which is: \n{repr(err)}')
        break

a_find = partial(finder, my_list)
# =============================================================================
# THIS CODE HAS BEEN SUCCESSFULLY COMPLETED.
# =============================================================================


#the assertion line is not neccessary cos of duck typing I suppose cs _input is 
# converted to str. However, below is a test for my assertion.   
# =============================================================================
# try:
#     print(finder(Words, 55))        
# except AssertionError:
#     print('Please start with a valid input, not integers.')
# 
# =============================================================================

#Well, obviously, this code may not need to use closures esp for what it is meant for
#but let's just ignore... 
#%% Trying to take advantage of the use of closure in the above def.
x = a_find()


#%%
#Actually, I could make the above a pd or np array object and do a vectorized operation on them.


#%%



def finder(words, _input = None, max_=5):
    
    def iter_(a):
        b = [x for x in words if len(x) == lent and set(x).issubset(a)]
        b_inc = [x for x in words if set(x).issubset(a)]
        final_ = b if b else sorted(b_inc, key=len, reverse = True)
        if final_:
            return f'Your results are:\n{final_[:max_]} \n'
        else:
            return 'You have no result: try again' '\n'
        
    if _input is None:
        _input = input('Find the suitable abbreviation for: '.title())
    
    if not isinstance(_input, str):
        print('Please enter proper inputs that contain alphabets: \n')
        main()
    else:
        lent = len(_input)
        
    # assert isinstance(_input, str)
    
        
    return iter_(_input.lower())


def main_():
    while True:
        try:
            print(finder(my_listnp))
            
        except KeyboardInterrupt:
            print('\n...\nOps:\nSearch Process has been Terminated by user')
            break
    
        except Exception as err:
            print(f'Some other error has occured, which is: \n{repr(err)}')
            break

def run():
    
    try:
        finder(my_listnp, 5)
        
    except AssertionError:
        print('Please enter only strings: Try again \n')
        main()


run()


#%% Here is she best so far.

from functools import partial

def finder(words, _input = None, max_=5):
    
    def iter_(a):
        b = [x for x in words if len(x) == lent and set(x).issubset(a)]
        b_inc = [x for x in words if set(x).issubset(a)]
        final_ = b if b else sorted(b_inc, key=len, reverse = True)
        if final_:
            return f'Your results are:\n{final_[:max_]} \n'
        else:
            return 'You have no result: try again' '\n'
        main()
        
    if _input is None:
        _input = input('Find the suitable abbreviation for: '.title())
    try:
        assert isinstance(_input, str)
    except AssertionError:
        print('Please enter something that conatians letters: Try again', '\n')
        return main()
        
    lent = len(_input)
    return iter_(_input.lower())

b_find = partial(finder, Words) #Now I only have to enter the arg I wanna find. 


def main():
    while True:
        try:    
            print(b_find())
        except KeyboardInterrupt:
            print('\n...\nOps:\nSearch Process has been Terminated by user')
            break
        except Exception as err:
            print(f'Some other error has occured, which is: \n{repr(err)}')
            break


#Need a way to handle nameerror.

#%% Using re

def findre(word, in_=None, max_=5):
    my_l = []
    if in_ is None:
        in_ = input('Write something to match:')
    inn = bytes(in_, 'utf-8')    
    pattern = re.compile(inn)
    for x in word:
        found = pattern.search(bytes(x, 'utf-8'))
        if found:
            my_l.append(x)
    return my_l[:max_]
        
c_find = partial(findre, Words)

print(c_find())

#I can search for multiple things at a time. in essence, re will be the best mordality
# as it gonna allow me to iterate over many stuffs without complexities


#%% Shorter form but not so useful without iteration



def findre(word, in_=None, max_=5):
    if in_ is None:
        in_ = input('Write something to match:')
    pattern = re.compile(in_)
    found = pattern.findall(str(word))
    return found[:max_]
        
d_find = partial(findre, re_word_list)

print(d_find('girl'))

#%% Trying to make re suitable for further processing


def findre(word, in_=None, max_=5):
    if in_ is None:
        in_ = input('Write something to match:')
    pattern = re.compile(in_)
    found = [x for x in word if pattern.search(x)]
    return found[:max_]
        
e_find = partial(findre, re_word_list)

print(e_find('girl'))



#%%

def findre(word, in_=None, max_=5):
    if in_ is None:
        in_ = input('Write something to match:')
    pattern = re.compile( bytes(in_, 'utf-8'))
    found = [x for x in word if pattern.search(bytes(x, 'utf-8'))]
    return found[:max_]
        
f_find = partial(findre, Words)

print(f_find())







#%%

#PERFORMANCE ANALYSIS. 

# =============================================================================
# %timeit a_find('community')
# 7.34 ms ± 1.06 ms per loop (mean ± std. dev. of 7 runs, 100 loops each)
# 
# %timeit b_find('community')
# 6.26 ms ± 343 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# 
# %timeit c_find('community')
# 2.93 ms ± 537 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# 
# %timeit d_find('community')
# 53 µs ± 732 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
# 
# %timeit e_find('community')
# 1.7 ms ± 241 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
# 
# %timeit f_find('community')
# 3.1 ms ± 379 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# =============================================================================


#WITH JUST TIME
# =============================================================================
# %time a_find('community')
# Wall time: 6 ms
# Out[163]: "Your results are:\n['community'] \n"
# 
# %time b_find('community')
# Wall time: 11 ms
# Out[164]: "Your results are:\n['community'] \n"
# 
# %time c_find('community')
# Wall time: 2 ms
# Out[165]: ['community']
# 
# %time d_find('community')
# Wall time: 0 ns
# Out[166]: ['community']
# 
# %time e_find('community')
# Wall time: 2 ms
# Out[167]: ['community']
# 
# %time f_find('community')
# Wall time: 4 ms
# Out[168]: ['community']
# =============================================================================


#SUMMARY
# =============================================================================
# As can be seen, it is best to use re... and perhaps, convert to string, even if
# it is in a list. it will shock you, as per the speed.
# the speed of c and e with same code shows that e, which uses a list comp is better
# d is the fasters, that's cos there is no iteration. but it is still useful, 
# bcos we uses findall, so returns all occurences. so if ur not interested in d word.
# =============================================================================


#%% Improving d_find

# Now this line is better. #but the speed has significantly reduced. and e has 
# way fater than it.

# =============================================================================
# %time g_find('tan')
# Wall time: 13 ms
# Out[222]: ['distance', 'exultant', 'hesitant', 'important', 'outstanding']
# 
# %time a_find('tan')
# Wall time: 7.99 ms
# Out[223]: "Your results are:\n['tan'] \n"
# 
# %time e_find('tan')
# Wall time: 2 ms
# Out[224]: ['distance', 'exultant', 'hesitant', 'important', 'outstanding']
# 
# =============================================================================
from re_list import re_word_list

def findre(word, in_=None, max_=5):
    if in_ is None:
        in_ = input('Write something to match:')
    pattern = re.compile(f'\w*{in_}\w*')
    found = pattern.findall(str(word))
    return found[:max_]
        
g_find = partial(findre, re_word_list)

print(g_find('girl'))


#%% Searching Multiple


def findre(word, in_= None, max_=5):
    my_dict = {}
    if in_ is None:
        in_ = input('Write all you want to match:')
    word_toS = re.compile('[a-zA-Z]+')
    found = word_toS.findall(in_)
        
    for x in found:
        my_dict.setdefault(x, [])
        pattern = re.compile(f'(?i)\w*{x}\w*')
        my_dict[x].append(pattern.findall(str(word)))
    
    return f'For {in_}, matches are: {my_dict}'
        
m_find = partial(findre, re_word_list)

print(m_find())

#%% #control the max output for my dict

def findre(word, in_= None, max_=5):
    my_dict = {}
    if in_ is None:
        in_ = input('Write all to match:')
    word_toS = re.compile('[a-zA-Z]+')
    found = word_toS.findall(in_)
        
    for x in found:
        my_dict.setdefault(x, [])
        pattern = re.compile(f'(?i)\w*{x}\w*')
        my_dict[x].append(pattern.findall(str(word)))
    print()
    if my_dict:
        for x,y in my_dict.items():
            print(f'RESULTS for "{x.upper()}" are: \n{y[0][:max_]} \n')
    else:
        print('You have no results')
    
        
n_find = partial(findre, re_word_list)
update_wrapper(n_find, findre) #Use upddate wrapper if you wanna copy the __doc__ etc, just lke in functools.wraps.
#partialmethod is used to wrap fnc with specific variables within a class. nb, d fnc it wraps is usu outside d class.

def man():
    while True:
        try:    
           n_find()
        except KeyboardInterrupt:
            print('\n...\nOps:\nSearch Process has been Terminated by user')
            break
        except Exception as err:
            print(f'Some other error has occured, which is: \n{repr(err)}')
            break

if __name__ == '__main__':
    man()

n_find('this is /ARE shit the chalenges they FAce')





#%%
# Can I make re give me all possibilities regardless of arrangement??


# print(list(permutations('elrufai')))
# =============================================================================
# for x in permutations('elru'):
#           a = ''.join(x)
#           print(a)
# 
# =============================================================================

# def permut(x):
#     return (''.join(c) for c in permutations(x))
 
def clock(func):
    def clocked(*args): # 
        t0 = time.perf_counter()
        _ = func(*args) #I want it to run the fnc.
        elapsed = time.perf_counter() - t0 #time at the end of the result.
        name = func.__name__ #get the name of the fnc it is decorating.
        print('[%0.8fs] %s' % (elapsed, name))
        return 
    return clocked


permut = lambda x : (''.join(c) for c in permutations(x))

#ok... Now, I have my function... letme use that.
print(list((permut('gsi'))))

# @clock
@lru_cache()
def a(x):
    return (''.join(c) for c in permutations(x))

# for x in a('this'):
#     print(x)
print(a('that'))
    
# @clock
def b(x):
    return (''.join(c) for c in permutations(x))

print(b('math'))

print(chain(a('two'), b('two')))
print(chain.from_iterable((a('two'), b('two'))))

v = chain.from_iterable((a('two'), b('two'))) #only works with one iterable, but i put in 2, in a tuple
y = chain(a('two'), b('two'))
# assert v == y #Assersion error. they are not same.
print(list(v))
print(list(y))
#%%
# lol... really not feasible
# @lru_cache(16)
def findre(word, in_=None, max_=5):
    if in_ is None:
        in_ = input('Write something to match:')
    found = defaultdict(list)    
    for x in permut(in_):
        pattern = re.compile(f'\w*{x}\w*')
        found[x].append(pattern.findall(str(word)))
        
    return found[0][:max_]
        
p_find = partial(findre, re_word_list)

p_find('nio')

# permut('gsi')
@lru_cache(160, True)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)
print(fibonacci(100))

#%% searching multiple with regex.

def findre(word, in_= None, max_=5):
    my_dict = {}
    if in_ is None:
        in_ = input('Write all to match:')
    word_toS = re.compile('[a-zA-Z]+')
    found = word_toS.findall(in_)
        
    for x in found:
        my_dict.setdefault(x, [])
        pattern = re.compile(f'(?i)\w*{x}\w*')
        my_dict[x].append(pattern.findall(str(word)))
    print()
    if my_dict:
        for x,y in my_dict.items():
            print(f'RESULTS for "{x.upper()}" are: \n{y[0][:max_]} \n')
    else:
        print('You have no results')
    
        
rc_find = partial(findre, re_word_list)

def man():
    while True:
        try:    
           rc_find()
        except KeyboardInterrupt:
            print('\n...\nOps:\nSearch Process has been Terminated by user')
            break
        except Exception as err:
            print(f'Some other error has occured, which is: \n{repr(err)}')
            break

if __name__ == '__main__':
    man()


#%% Searching multiple with normal find.


def finder(words, _input = None, max_=5):
    my_dict = defaultdict(list)
    if _input is None:
        _input = input('Find the suitable abbreviation for: '.title())
    assert isinstance(_input, str)
    find = re.compile('[a-zA-Z]+').findall(_input)
    
    def iter_(f_):
        for word in f_:
            lent = len(word)
            a = word.lower()
            b = [x for x in words if len(x) == lent and set(x).issubset(a)]
            b_inc = [x for x in words if set(x).issubset(a) and len(x) < lent]
            my_dict[word].append(b + sorted(b_inc, key=len, reverse = True))
            
        for x, y in my_dict.items():
            print(f'RESULTS for "{x.upper()}" are: \n{y[0][:max_]} \n')
                
    return iter_(find)


def man_():
    while True:
        try:    
            mc_find()
        except KeyboardInterrupt:
            print('\n...\nOps:\nSearch Process has been Terminated by user')
            break
        except Exception as err:
            print(f'Some other error has occured, which is: \n{repr(err)}')
            break

mc_find = partial(finder, my_list)


if __name__ == '__main__':
    man_()
    
    
    
    
#Final verdict. the normal find is a lot faster. #Nb that finding with re gives you an expanded find.

#%% Using a timer to time our fncs.
#so, remember, decorator takes fnc as arg... so implementing it is like saing..
# clock(a) where a is the cnd it is decorating.

def clock(func):
    def clocked(*args): # 
        t0 = time.perf_counter()
        _ = func(*args) #I want it to run the fnc.
        elapsed = time.perf_counter() - t0 #time at the end of the result.
        name = func.__name__ #get the name of the fnc it is decorating.
        print('[%0.8fs] %s' % (elapsed, name))
        return 
    return clocked

@clock
def findre(word, in_= None, max_=5):
    my_dict = {}
    if in_ is None:
        in_ = str(input('Write all to match:'))
        
    word_toS = re.compile('[a-zA-Z]+')
    
    found = word_toS.findall(in_)
    for x in found:
        my_dict.setdefault(x, [])
        pattern = re.compile(f'(?i)\w*{x}\w*')
        my_dict[x].append(pattern.findall(str(word)))
        
    for x,y in my_dict.items():
        return f'RESULTS for "{x.upper()}" are: \n{y[0][:max_]} \n'

@clock
def finder(words, _input = None, max_=5):
    my_dict = defaultdict(list)
    if _input is None:
        _input = input('Find the suitable abbreviation for: '.title())
    assert isinstance(_input, str)
    find = re.compile('[a-zA-Z]+').findall(_input)
    
    def iter_(f_):
        for word in f_:
            lent = len(word)
            a = word.lower()
            b = [x for x in words if len(x) == lent and set(x).issubset(a)]
            b_inc = [x for x in words if set(x).issubset(a) and len(x) < lent]
            my_dict[word].append(b + sorted(b_inc, key=len, reverse = True))
            
        for x,y in my_dict.items():
            return f'RESULTS for "{x.upper()}" are: \n{y[0][:max_]} \n'
        
    return iter_(find)


findre(my_list, 'You have no results7what, eh ahoufdc fucnk you aoindint woi in the village ossn our elsseri')
finder(my_list, 'You have no results7what, eh ahoufdc fucnk you aoindint woi in the village ossn our elsseri')

#well, trust me, the results are:
    # [0.17522470s] findre
    # [0.08153500s] finder #more than 2x faster.

#however, if I'm only matching the right word... as per without the \w* around, then:
    # [0.06379640s] findre #More than 3 x faster
    # [0.19357080s] finder

# Test for a large file. #59040 words.
with open('experiment.txt', encoding='utf8') as f:
    try:
        a = f.read()
    except (UnicodeDecodeError, TypeError): pass
    finally:
        print(len(a))
        # findre(my_list, a)
        # finder(my_list, a)
     
    
 
# Result for large file search 5040 words:
    # [43.24294590s] finder
    # [63.13625100s] findre

# for 179241 words
    # [1349.70006510s] findre
    # [868.60610060s] finder

#the error not subscriptable means that the object impliments the __getitem__ method... ie, it is a container, 
# and can contain different items type, hence, i couldn't use itertools.chain in my my_dict[word] append line.

# AFter doing the change of combining list, here is the result for their time, finder is still faster.

#%%
#want to use multithreading for the above and see teh difference in time.
from concurrent import futures



# =============================================================================
# #wrong implimentation... it has to be able to di it one after d other...
# 
# #lemme set to 20 workers and see what difference it brings.
# @clock
# def f_findre():
#     with futures.ThreadPoolExecutor(20) as executor:
#         result = executor.map(findre, ['this', 'is'])
#     return result
#         
# 
# @clock
# def f_finder():
#     with futures.ThreadPoolExecutor(20) as executor:
#         result = executor.map(finder, ['this', 'is'])
#     return result
# =============================================================================
    
# f_finder()
# f_findre()
# list(map(len, one_word()))

class Abre:
    
    my_dict = defaultdict(list)
    word_toS = re.compile('[a-zA-Z]+')
    
    def __init__(self, words, max_=5):
        self.words = words
        self.max = max_
        
    def __iter_(self, abbr): #1
         lent = len(abbr)
         a = abbr.lower()
         
         b = [x for x in self.words if len(x) == lent and set(x).issubset(a)] #2
         b_inc = [x for x in self.words if set(x).issubset(a) and len(x) < lent]
         
         self.my_dict[abbr].append(b + sorted(b_inc, key=len, reverse = True)) #3
         
    
    def __search_many(self, it, n=None):
        it = self.word_toS.findall(str(it))
        
        if n is None:
            n = min(100, len(it)) #4
        with futures.ProcessPoolExecutor() as executor: #5
            executor.map(self.__iter_, it) #6
        return self.__run()

    def __run(self):
        for x,y in self.my_dict.items():
            print(f'RESULTS for "{x.upper()}" are: \n{y[0][:self.max]} \n')
        self.my_dict.clear() #7
        return 'DONE! \n\n'
        
    def __call__(self, x):
        return self.__search_many(x)
        



# 9
a = Abre(my_list)
print(a('this'))
print(a('cometo'))
print(a(['this', 'is', 'boy']))
#8
# print(a.__search_many('this is a boy'))
# b = Abre(my_list)
# print(b.search_many(['this', 'is', 'boy']))
# b('come')

# 10
# =============================================================================
# %time findre(my_list, 'You have no results7what, eh ahoufdc fucnk you aoindint woi in the village ossn our elsseri')
# [0.12157770s] findre
# Wall time: 132 ms
# 
# 
# c = Abre(my_list)
# %time c('You have no results7what, eh ahoufdc fucnk you aoindint woi in the village ossn our elsseri')
# Wall time: 69 ms
# Out[73]: 'DONE! \n\n'
#

# For or 179241 words gotten from the one_word function
# a = list(one_word())
# %time c(a)

# =============================================================================


# =============================================================================
# Explanations:
# 1. this method returns nothing, so calling it will return None.
# 2. get matching values
# 3. put results in the dict
# 4. used the least needed processor for n so you don't produce wasteful cores.
# 5. instantiation with a future object.
# 6. Run every thing in the iterable
# 7. Clear the dict to give room for another call.
# 8. protected methods...
# 9. Code testing.
# 10. Code timing.
# =============================================================================


 #if we wanna execute many, use this to extract the words
 #so that it can be added to download meany one at a time.
 #this was a static method in the class before. I just decided to seperate.
def one_word(x=None):
    word_toS = re.compile('[a-zA-Z]+')
    if x:
        found = word_toS.findall(str(x))
    else:
        x = 'experiment.txt'
        with open(x, encoding='utf8') as f:
            f = f.read()
            try:
                found = word_toS.findall(f)
            except (UnicodeDecodeError, TypeError): pass
        
    for word in found:
       yield word

# =============================================================================
# #Ok, I got this far... 
# #Here are the things I intend for this class to do...
# 1. should use concurrency once more than one word is provided.. the one_word should iterate through the words... if 
# it is coming from a file... 
# 
# 2. learn more about futures to be able to apply it here.
# #should be able to pop/clear the dictionary at every new call.
# #should be able to continiously give values, even after the first call.
# 
# =============================================================================




#%% IDEAS

#I could use itertools.dropwhile() to iterage and produce new values until the max no of specified values is achieved.
#I am thinking for the nested for loops, it may be worthwhile to see how to impliment it using itertools.product()


# The next phase is where I'll be using coroutines to achieve a good result 
    
#this is so that I can make the calls to the re form respond to permutations.

word_toS = re.compile('[a-zA-Z]+')
with open('experiment.txt', encoding='utf8') as f:
    a = f.read()
    try:
        found = word_toS.findall(a)
    except (UnicodeDecodeError, TypeError): pass
    finally:
        print(found)
        


#%% Trying to see IF I can use numpy to achieve a faster result output

def finder(words, _input = None, max_=5):
    my_dict = defaultdict(list)
    if _input is None:
        _input = input('Find the suitable abbreviation for: '.title())
    assert isinstance(_input, str)
    find = re.compile('[a-zA-Z]+').findall(_input)
    
    def iter_(f_):
        for word in f_:
            lent = len(word)
            a = word.lower()
            print(len(words))
            b = [len(words) == lent] #and [set(words).issubset(a)]
            b_inc = [x for x in words if set(x).issubset(a) and len(x) < lent]
            my_dict[word].append(words[b]) #+ sorted(b_inc, key=len, reverse = True))
            print(b)    
        for x, y in my_dict.items():
            print(f'RESULTS for "{x.upper()}" are: \n{y[0][:max_]} \n')
                
    return iter_(find)


#Still not working yet... I guess I have to make a function and map it.

def man_():
    while True:
        try:    
            mc_find_np()
        except KeyboardInterrupt:
            print('\n...\nOps:\nSearch Process has been Terminated by user')
            break
        except Exception as err:
            print(f'Some other error has occured, which is: \n{repr(err)}')
            break

mc_find_np = partial(finder, np.array(my_list, dtype=np.str_))


if __name__ == '__main__':
    man_()



#%% itertools.chain???











    
    
