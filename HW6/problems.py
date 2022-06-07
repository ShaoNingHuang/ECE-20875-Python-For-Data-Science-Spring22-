import re

def problem1(searchstring):
    """
    Match phone numbers.

    :param searchstring: string
    :return: True or False
    """
    p=re.match("\+",searchstring)
    if p:
        q=re.compile("\\+(1|52)\s([\d]{3}\-|[\d]{3}|\([\d]{3}\)\s)([\d]{3})(\-[\d]{4}|[\d]{4})$")
        result=q.match(searchstring)
        if result:
            return True
        else:
            return False
    else:
        q=re.compile("[\d]{3}\-[\d]{4}")
        result=q.match(searchstring)
        if result:
            return True
        else:
            return False
        
def problem2(searchstring):
    """
    Extract street name from address.

    :param searchstring: string
    :return: string
    """
    result=re.search("([\d]+)(( [A-Z][a-z]*)+)( [A-Z][a-z]*\.)",searchstring)       
    a=result.group(1)+result.group(2)
    return a
   
def problem3(searchstring):
    """
    Garble Street name.

    :param searchstring: string
    :return: string
    """
    r=re.search("([\d]+)(( [A-Z][a-z]*)+ )([A-Z][a-z]*\.)",searchstring)
    a=r.group(2)
    old=a
    new=a[::-1]
    maxreplace=1
    result=new.join(searchstring.rsplit(old,maxreplace))
    return result
   


if __name__ == '__main__' :
    print("\nProblem 1:")
    print("Answer correct?", problem1('+1 765-494-4600') == True)
    print("Answer correct?", problem1('+52 765-494-4600 ') == False)
    print("Answer correct?", problem1('+1 (765) 494 4600') == False)
    print("Answer correct?", problem1('+52 (765) 494-4600') == True)
    print("Answer correct?", problem1('+52 7654944600') == True)
    print("Answer correct?", problem1('494-4600') == True)

    print("\nProblem 2:")
    print("Answer correct?",problem2('Please flip your wallet at 465 Northwestern Ave.') == "465 Northwestern")
    print("Answer correct?",problem2('Meet me at 201 South First St. at noon') == "201 South First")
    print("Answer correct?",problem2('Type "404 Not Found St" on your phone at 201 South First St. at noon') == "201 South First")
    print("Answer correct?",problem2("123 Mayb3 Y0u 222 Did not th1nk 333 This Through Rd. Did Y0u Ave.") == "333 This Through")
    print("\nProblem 3:")
    print("Answer correct?",problem3('The EE building is at 465 Northwestern Ave.') == "The EE building is at 465 nretsewhtroN Ave.")
    print("Answer correct?",problem3('Meet me at 201 South First St. at noon') == "Meet me at 201 tsriF htuoS St. at noon")

