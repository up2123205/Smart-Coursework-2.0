"""A class that creates SmartPlug"""
class SmartPlug():

    def __init__(self, consumptionRate):
        """sets switched On to False and consumptionRate to 0)"""
        self.switchedOn = False
        self.consumptionRate = consumptionRate
    
    def toggleSwitch(self):
        """toggleSwitch to on or off"""
        if self.switchedOn == False:
            self.switchedOn = True
        else:
            self.switchedOn = False
            
            
    def getSwitchedOn(self):
        """return to switchedOn"""
        return self.switchedOn
    
    def setConsumptionRate(self, newconsumptionRate):
        """sets the number between 0 and 150"""
        if  0 <= newconsumptionRate <= 150:
            self.consumptionRate = newconsumptionRate
        else:
            return "Consumption rate out of range 0 to 150: "
        
    def getConsumptionRate(self):
        """return the consumption rate"""
        return self.consumptionRate

    def __str__(self):
        """return the output for the switch to either on or off and will return a string representation of smartPlug"""
        if self.switchedOn == True:
            status = "On"
        else:
            status = "Off"

        output = "Plug: {}, consumption rate: {}".format(status, self.consumptionRate)
        return output

def testSmartPlug():
    sp = SmartPlug(45)
    sp.toggleSwitch()
    print("Smartplug status:", sp.getSwitchedOn())
    print("Smartplug consumption rate:", sp.getConsumptionRate())
    sp.setConsumptionRate(50)
    print("Smartplug consumption rate:", sp.getConsumptionRate())
    print(sp)

#testSmartPlug()
    
class SmartDoorBell():
    def __init__(self):
        self.switchedOn = False
        self.sleepMode = False
        
    def toggleSwitch(self):
        if self.switchedOn == False:
            self.switchedOn = True
        else:
            self.switchedOn = False
            
    def getSwitchedOn(self):
        """return to switchedOn"""
        return self.switchedOn
    
    def getSleepMode(self):
        return self.sleepMode
    
    def setSleepMode(self, sleepMode):
        self.sleepMode = sleepMode
        
    def __str__(self):
        if self.switchedOn == True:
            status = "On"
        else:
            status = "Off"
        if self.sleepMode == True:
            mode = "On"
        else:
            mode = "Off"
        
        output = "DoorBell: {}, sleep mode: {}".format(status, mode)
        return output
    
def testSmartDoorBell():
    """a function to test SmartDoorBell"""
    sdb = SmartDoorBell()
    print(sdb)
    sdb.toggleSwitch()
    print("Doorbell status:", sdb.getSwitchedOn())
    print("Doorbell sleep mode:", sdb.getSleepMode())
    sdb.setSleepMode(True)
    print("Doorbell sleep mode:", sdb.getSleepMode())
    print(sdb)
        
#testSmartDoorBell()
        
class SmartHome():
    def __init__(self):
        """set devices to empty list"""
        self.devices = []
        
    def getDevices(self):
        """return the list of items in the smart home"""
        return self.devices
    
    def getDeviceAt(self, index):
        if 0 <= index < len(self.devices):
            return self.devices[index]
        else:
            return None
        
    def removeDeviceAt(self,index):
         if 0 <= index < len(self.devices):
            del self.devices[index]

    def numberofDevices(self):
        """return the number of devices"""
        return len(self.devices)

        
    def addDevice(self,device):
        """add the device to the list"""
        self.devices.append(device)
       
    def toggleSwitch(self, index):
        device = self.getDeviceAt(index)
        device.toggleSwitch()
            
    def turnOnAll(self):
        """Turn on all the devices in the device list"""
        for device in self.devices:
            device.switchedOn = True
            
    def turnOffAll(self):
        """Turn off all of the devices in the device list"""
        for device in self.devices:
            device.switchedOn = False
            
    def __str__(self):
        output = "Smart Home contains:\n"
        for device in self.devices:
            output += f"{device}\n"
        return output
    
def testSmartHome():
    """function to test SmartHome"""
    home = SmartHome()
    plug1 = SmartPlug(45)
    plug2 = SmartPlug(45)
    bell = SmartDoorBell()
    
    plug1.toggleSwitch()
    plug1.setConsumptionRate(150)
    
    plug2.setConsumptionRate(25)
    
    bell.setSleepMode(True)
    
    home.addDevice(plug1)
    home.addDevice(plug2)
    home.addDevice(bell)
    print(home)
    
    home.toggleSwitch(1)   # toggles second plug (position [1] in list)
    print(home)
    
    home.turnOnAll()
    print(home)
    
    home.removeDeviceAt(0) # removes first plug (position [0] in list)
    print(home)
    
    
#testSmartHome()
    
            
            
            
        
            
        
        
       
    
       
       
    
        
        
        
        
        
    
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
    

        
        
        
        
        
        
            
    
            
            
            
            
    
    
    

    
    
      