
                 #CGPA CACULAOR FOR UBIT

o = []
n = int(input("### ENTER NUMBER OF COURSES IN SEMESTER ### ="))
for i in range (0,n):
    x = float(input(f"ENTER COURSE #{i+1} MARKS="))
    
                 #CONDITIONS
    
    if(x >= 90 and x <=100):
       a=(4.0)
    elif(x  >= 85 and x  <=89):
         a = (4.0)    
    elif(x  >= 80 and x <=84):
         a = (3.8)  
    elif(x >=75 and x  <=79 ):
         a = (3.4)    
    elif(x  >=71 and x  <=74):
         a = (3.2)    
    elif(x  >=68 and x  <=70):
         a = (2.8)      
    elif(x  >=64 and x  <=67):
         a = (2.4)    
    elif(x  >=61 and x  <=63):
         a = (2.0)    
    elif(x  >=57 and x  <=60):
         a = (1.8)    
    elif(x  >=53 and x  <=56):
        a = (1.4)        
    elif(x  >=50 and x  <=52):
         a = (1.0)
    elif(x  < 50):
         a = (0.0)
    o.append(a)  
    
                #CALCULATION AND OUTPUT
    
gpa = sum(o)/n

print("")

print(f" YOUR FINAL CGPA IS {round(gpa,2)}")  

    
    