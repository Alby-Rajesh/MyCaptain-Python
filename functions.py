def most_frequent(string):
    d={}
    count=1
    for i in string:
        if i not in d:
            d[i]=count
        elif i in d:
            d[i]=d[i]+1
    sort = sorted(d.values(),reverse=True)
    print(sort)
    newdict={}
    for i in sort:
        for k in d.keys():
            if d[k] == i:
                newdict[k] = d[k]
                
    print(newdict)        
        
most_frequent("Mississippi")
        
            
        
    
