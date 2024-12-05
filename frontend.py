import tkinter

from backend import *
from tkinter import *

class SmartHomeSystem:

    def __init__(self, home):
      self.home = home
      self.win = Tk()



      self.mainFrame = Frame(self.win)
      self.mainFrame.grid(
          row=0,
          column=0,
          padx=10,
          pady=10,
      )
      self.newDeviceName = StringVar()

      self.widgets = []

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        turnOnAllButton = Button(
            self.mainFrame,
            text="Turn On All",
            # command= # Add the name of the method that turns everything on here

        )
        turnOnAllButton.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
        )

        
        turnOffAllButton = Button(
            self.mainFrame,
            text="Turn Off All",

        )
        turnOffAllButton.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
        )


        numberofDevices = len(self.home.getDevices())
        for i in range(numberofDevices):
            device = self.home.getDeviceAt(i)
            deviceLabel = Label(
                self.mainFrame,
                text=device

            )



            deviceLabel.grid(
                row=i + 1,
                column=0,
                padx=5,
                pady=5,

            )
            self.widgets.append(deviceLabel)


            toggleButton = Button(
                self.mainFrame,
                text="Toggle",
                command=lambda index=i: self.toggleButton(index)

            )

            toggleButton.grid(
                row=i + 1,
                column=1,
                padx=5,
                pady=5,
            )
            self.widgets.append(toggleButton)


            editButton = Button(
                self.mainFrame,
                text="Edit",
                command=lambda index=i: self.editButton(index)

            )

            editButton.grid(
                row=i + 1,
                column=2,
                padx=5,
                pady=5,
            )
            self.widgets.append(editButton)


            deleteDeviceButton = Button(
                self.mainFrame,
                text="Delete",
                command=lambda index=i: self.deleteDeviceButton(index)


            )

            deleteDeviceButton.grid(
                row=i + 1,
                column=3,
                padx=5,
                pady=5,
            )
            self.widgets.append(deleteDeviceButton)


        addButton = Button(
            self.mainFrame,
            text="Add",
            command=lambda index=i: self.addButton(index)

        )

        addButton.grid(
            row= 6,
            column=0,
            padx=5,
            pady=5,
        )
        self.widgets.append(addButton)



    def turnOnAll(self):
        self.home.turnOnAll()
        self.newDeviceName.set("")
        self.createWidgets()


    def turnOffAll(self):
        self.home.turnOffAllDevices
        self.createWidgets()

    def deleteAllWidgets(self):
        for widget in self.createWidgets:
            widget.destroy()
        self.createWidgets = []





def setUpHome():
    home = SmartHome()
    print("Welcome to the SmartHome app")
    print("Please add five new devices to your smart home")
    for device in range(5):
        choice = int(input("Enter 1 for SmartPlug or 2 for SmartDoorBell: "))
        if choice == 1:
            consumptionRate = int(input("Enter the value for the consumption rate: "))
            plug = SmartPlug(consumptionRate)
            home.addDevice(plug)

        else:
            bell = SmartDoorBell()
            home.addDevice(bell)
    app = SmartHomeSystem(home)
    app.run()





setUpHome()

