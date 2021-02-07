
class Vehicle:  #makes a class called Vehicle
                #and initializes it with the following 
    def __init__(self, Make, Model, Year, Weight, Need_Maint = False, TSM = 0):
        self.carMake = Make
        self.carModel = Model
        self.carYear = Year
        self.carWeight = Weight

    def setMake(self, Make):
        self.carMake = Make
    
    def setModel(self, Model):
        self.carModel = Model
    
    def setYear(self, Year):
        self.carYear = Year
    
    def setWeight(self, Weight):
        self.carWeight = Weight

class Cars(Vehicle):    #TSM = tripsSinceMaintenance
    def __init__(self, Make, Model, Year, Weight, Need_Maint = False, TSM = 0, isDriving = False):
        Vehicle.__init__(self, Make, Model, Year, Weight, Need_Maint = False, TSM = 0)
        self.TSM = TSM
        self.isDriving = isDriving
        self.Need_Maint = Need_Maint
    def Drive(self):
        self.isDriving = True
    
    def stop(self):
        self.isDriving = False
        self.TSM += 50
        if self.TSM ==100:
            self.Need_Maint = True
    def Repair(self):
        self.TSM = 0
        self.Need_Maint = False



Car1 = Vehicle("Kia", "Optima", 2017, 2000,False) #Makes first car
Car2 = Cars("Ford", "F150",2010, 4000, False)   #makes Second car
Car3 = Cars("Toy", "Plastic", 2020,2, False)





# print(Car1.isDriving)         #prints useful info about each car
# # print(Car1.TSM)
# # print(Car1.Need_Maint)
# # print(Car2.isDriving)
# # print(Car2.TSM)
# # print(Car2.Need_Maint)


# #starts and stops the vehicles
# Car1.Drive()    
# Car1.stop()
# Car2.Drive()    
# Car2.stop()
# Car3.Drive()    
# Car3.stop()
# # print(Car1.isDriving)      #prints useful info about car after first trip
# # print(Car1.TSM)
# # print(Car1.Need_Maint)
# # print(Car2.isDriving)
# # print(Car2.TSM)
# # print(Car2.Need_Maint)
# # print(Car3.isDriving)
# # print(Car3.TSM)
# # print(Car3.Need_Maint)
# Car1.Drive()                    #starts driving again
# Car2.Drive()
# Car3.Drive()
# #print(Car1.isDriving)
# #print(Car2.isDriving)
# #print(Car3.isDriving)
# Car1.stop()             #stops cars again
# Car2.stop()
# Car3.stop()
# # print(Car1.TSM) #Prints the tripsSinceMaintenanc status needs maintenance
# # print(Car2.TSM)
# # print(Car3.TSM)
# # print(Car1.Need_Maint)  #prints need maintenance status
# # print(Car2.Need_Maint)
# # print(Car3.Need_Maint)
# # Car1.Repair()
# # Car2.Repair()
# # Car3.Repair()
# # print(Car1.TSM)
# # print(Car2.TSM)
# # print(Car3.TSM)
# Car3.setMake("Doggy")
# print(Car3.carMake)
