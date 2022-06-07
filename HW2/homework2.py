
def histogram(data, n, b, h):
    # data is a list
    # n is an integer
    # b and h are floats
    
    # Write your code here

    # return the variable storing the histogram
    # Output should be a list
    thislist=[]
    if(n==0):
        return thislist
    
    if(b==h):
        print("b and h are the same value")
        return thislist
    if(b>h):
        thislist=n*[0]
        x=b
        b=h
        h=x
        w=(h-b)/n
        for y in data:
            for z in range(1,n):
                if y<h and y>b:
                    if y>b and y< b+w:
                        thislist[0]+=1
                    else:
                        if y>=b+z*w and y<b+(z+1) *w:
                            thislist[z]+=1
                else:
                    continue
    else:
        thislist=n*[0]
        w=(h-b)/n
        for y in data:
            for z in range(1,n):
                if y<h and y>b:
                    if y>b and y< b+w:
                        thislist[0]+=1
                    else:
                        if y>=b+z*w and y<b+(z+1) *w:
                            thislist[z]+=1
                else:
                    continue
                
    return thislist
def happybirthday(name_to_day, name_to_month, name_to_year):
    #name_to_day, name_to_month and name_to_year are dictionaries
    
    # Write your code here

    # return the variable storing name_to_all
    # Output should be a dictionary
    month_to_all={
        }
    for x in name_to_month:
        tuple1=(x)
        tuple2=(name_to_day[x],name_to_year[x],2022-name_to_year[x])
        tuple3=(tuple1,tuple2)
        month_to_all[name_to_month[x]]=tuple3
    
    return month_to_all
