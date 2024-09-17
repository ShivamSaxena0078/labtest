import numpy as np
flightSchedule=np.array([[1234,"IND","AUS",1200,5,20],[2345,"USA","PAK",1310,6,4],[5678,"NZL","UAE",1100,10,16],[3678,"SAO","ARG",2030,0,0]])
print(flightSchedule)
passengerRecords=np.array([[123456,"raj",1234,"BC",2],[234567,"ram",3678,"EC",3],[123456,"raj",3678,"BC",2]])

print(passengerRecords)
def find(id,rec):
    
    for x in rec:
        for y in x:
            if y==id:
                print(x[1],"booked flight in class -",x[3], "in flight number :",x[2])
                
print(find('123456',passengerRecords))

def update(fid,sch,clas,upd):
    
    for x in sch:
        for y in x:
            if y==fid:
                if clas=="BC":
                    x[4]-=upd
                if clas=="EC":
                    x[5]-=upd
                
                
update('1234',flightSchedule)
def froute(fsch):
    max=999999
    min=0
    for x in fsch:
        for y in x:


def booked(fsch):
    
    for x in fsch:
        if x[4]=='0' and x[5]=='0':
                print("flight id : ",x[0]," is fully booked")
    
print(booked(flightSchedule))
            
            
