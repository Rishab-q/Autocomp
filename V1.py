import requests,time
url="http://35.200.185.69:8000/v1/autocomplete"
count=0
T=time.time()
def diff_char(s1,s2):
    x=min(len(s1),len(s2))
    y=""
    for i in range(x):
        if(s1[i]==s2[i]):
            y+=s1[i]
        else :
            return y,s1[i] or ''
    return y,''
S=set()
def My_func(a,b):
 global count
 global T
 for x in range(ord(b),123):
    if(count%100==0 and count!=0):
        B=time.time()
       
        time.sleep(65-int(B-T))
        T=time.time() 
                 
    response= requests.get(url,{'query':a+chr(x)})
    count=count+1
    p=response.json()['results']
    print(a+chr(x),count)
    if response.json()['count']==10:
        y,t=diff_char(p[9],p[8])
        y1,t1=diff_char(p[0],p[9])
        if y==y1:
            S.update(p)
            My_func(y,t)
        else:
            S.update(p)
            My_func(y[:-1],y[-1])      
    elif response.json()['count']>1:
        S.update(p)
 return

z=time.time()
My_func('','a')       
print(S,len(S)) 
        
        
        

    

   
    

