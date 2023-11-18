from abc import ABC, abstractmethod 

class Ride_sharing:

    def __init__(self,company_name) -> None:
        self.company_name=company_name
        self.Riders=[]
        self.Drivers=[]

    def add_rider(self,rider_obj):
        self.Riders.append(rider_obj)
    def add_Drivers(self,driver_obj):
        self.Drivers.append(driver_obj)
    def __repr__(self) -> str:
        result=f"{self.company_name} has {len(self.Riders)} riders and {len(self.Drivers)} Drivers"
        return result
    
class User(ABC):

    def __init__(self,name,email,national_id) -> None:
        self.name=name
        self.email=email
        self.__national_id=national_id

    @abstractmethod
    def Display_Profile(self):
        raise NotImplementedError

class Driver(User):

    def __init__(self,name,email,national_id,current_location) -> None:
        super().__init__(name,email,national_id)
        self.current_location=current_location
    def Display_Profile(self,Driver):
        print(f"Driver Name : {self.name}")

class Rider(User):

    def __init__(self, name, email, national_id,wallet,Start_location) -> None:
        super().__init__(name, email, national_id)
        self.__wallet=wallet
        self.Start_location=Start_location
        self.current_ride=None
    
    def Display_Profile(self):
        print(f"Rider Name : {self.name}")

    def show_current_location(self):
        print(f"Current Location : {self.Start_location} and his name : self{self.name}")

    def Ride_Request(self,Uber,Destination):
        print('Looking for Ride')
        if not self.current_ride:
            obj =Ride_Matching(Uber.Drivers)
            Result=obj.has_driver(self,Destination)
            print(Result)
            self.current_ride = Result
            return True
        else :
            return False    

class Ride_Matching:

    def __init__(self,drivers) -> None:
        self.drivers=drivers
    
    def has_driver(self,Uber_driver,destination):

        if len(self.drivers) >0 :
            ride=Ride(Uber_driver.Start_location,destination)
            return ride
        else:
            return f"Sorry,no driver Found"



class Ride:

    def __init__(self,Start_location,End_location) -> None:
        self.Driver=None
        self.Rider=None
        self.Start_location=Start_location
        self.End_location=End_location

    def start_rider(self):
        pass
    
    def end_rider(self):
        pass
    
    def __repr__(self) -> str:
        return f"start from {self.Start_location} to {self.End_location}"



Pataho=Ride_sharing('Pathao')
Farhan=Driver('Farhan', 'kenaa@example.com', 12345678,'Dhaka')
Zaman=Driver('Zaman', 'zaman@example.com', 1245678,'Rangpur')
Shakib=Rider('Shakib', 'kenaa@example.com', 1234567,500,'Feni')
Tamjid=Rider('Tamjid', 'tamjid@example.com', 1234567,1000,'Noakhali')
Pataho.add_Drivers(Farhan)
Pataho.add_Drivers(Zaman)

Pataho.add_rider(Shakib)
Pataho.add_rider(Tamjid)
print(Pataho)

if(Tamjid.Ride_Request(Pataho,'Dhaka')):
    print('Travelling')
else :
    print('Not Travelling')
