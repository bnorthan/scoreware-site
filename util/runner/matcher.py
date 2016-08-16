import Levenshtein

def matchRunner(first1, last1, age1, city1, first2, last2, age2, city2):
    fscore=matchFirstName(first1, first2)
    lscore=matchLastName(last1, last2)
    cscore=matchCity(city1, city2)
    ascore=matchAge(age1, age2)

    return fscore+lscore+cscore+ascore

def matchFirstName(first1, first2):
    return Levenshtein.ratio(first1, first2)

def matchLastName(last1, last2):
    return Levenshtein.ratio(last1, last2)

def matchCity(city1, city2):
    return Levenshtein.ratio(city1,city2)

def matchAge(age1, age2):
    return 1-(float(abs(age1-age2))/float((age1+age2)))




