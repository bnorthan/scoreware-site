import Levenshtein
import math

def matchRunner(first1, last1, gender1, age1, city1, first2, last2, gender2, age2, city2):
    fscore=matchFirstName(first1, first2)
    lscore=2*matchLastName(last1, last2)
    cscore=matchCity(city1, city2)
    ascore=matchAge(age1, age2)
    gscore=matchGender(gender1, gender2)
    if (fscore+lscore+gscore+cscore+ascore>4.8):
        print(first1,first2,last1,last2,city1,city2,age1,age2,gender1,gender2)
        print(fscore,lscore,cscore,ascore,gscore)
        print(fscore+lscore+gscore+cscore+ascore)
        print()
    return fscore+lscore+gscore+cscore+ascore

def matchGender(gender1, gender2):
    if (gender1.lower()[0]==gender2.lower()[0]):
        return 1
    else:
        return 0
        

def matchFirstName(first1, first2):
    return Levenshtein.ratio(first1, first2)

def matchLastName(last1, last2):
    return Levenshtein.ratio(last1, last2)

def matchCity(city1, city2):
    return Levenshtein.ratio(city1,city2)

def matchAge(age1, age2):
    try:
        return 2/(1+math.exp(0.5*float(abs(age1-age2))))
    except:
        return 0.5




