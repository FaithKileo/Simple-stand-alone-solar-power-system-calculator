from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("SIMPLE STAND ALONE SOLAR POWER SYSTEM CALCULATOR")

root.geometry("565x550+0+0")
root.resizable(0,0)

#FUNCTIONS
def calculator():
    if e_totalLoad.get() == "":
       messagebox.showinfo("Information", "Please fill in the inputs")

    elif e_numberOfHours.get() == "":
        messagebox.showinfo("Information", "Please fill in the inputs")

    elif e_totalLoad.get() == "" and e_numberOfHours.get() == "":
        messagebox.showinfo("Information", "Please fill in the inputs")

    else:
        if var1.get() == 0 and var2.get() == 0:
            messagebox.showinfo("Information", "Please select one battery type")

        elif var1.get() == 1 and var2.get() == 1:
            messagebox.showinfo("Information", "Please select one battery type")

        else:

            if var1.get() == 1:

                #For Lithium-ion
                item1 = int(e_totalLoad.get())
                item2 = int(eval(e_numberOfHours.get()))

                sizeOfInverter = int((item1 + (0.3*item1)))

                totalLoadPower = item1 + (0.15*sizeOfInverter)
                batteryInkWh = (((totalLoadPower*item2)/1000)/0.8)

                sizeOfBattery = int(((batteryInkWh*1000)/12))

                sizeOfPanelf = ((batteryInkWh*1.3)/7)
                sizeOfPanel = round(sizeOfPanelf, 4)

                inverterSizeVar.set(str(sizeOfInverter) + 'Watts')
                batterySizeVar.set(str(sizeOfBattery) + 'Ah')
                panelSizeVar.set(str(sizeOfPanel) + 'kW')

            if var2.get() == 1:   

                #For Lead-acid 
                item1 = int(e_totalLoad.get())
                item2 = int(e_numberOfHours.get())

                sizeOfInverter = int((item1 + (0.3*item1)))

                totalLoadPower = item1 + (0.15*sizeOfInverter)
                batteryInkWh = (((totalLoadPower*item2)/1000)/0.5)

                sizeOfBattery = int(((batteryInkWh*1000)/12))

                sizeOfPanelf = ((batteryInkWh*1.3)/7)
                sizeOfPanel = round(sizeOfPanelf, 4)

                inverterSizeVar.set(str(sizeOfInverter) + 'Watts')
                batterySizeVar.set(str(sizeOfBattery) + 'Ah')
                panelSizeVar.set(str(sizeOfPanel) + 'kW')

def clear():
    textTotalLoad.delete(0, END)
    textNumberOfHours.delete(0, END)

    inverterSizeVar.set("")
    batterySizeVar.set("")
    panelSizeVar.set("")
#FRAMES
inputFrame = Frame(root, bd=10, relief=RIDGE)
inputFrame.pack(side = TOP)

#VARIABLES
var1 = IntVar()
var2 = IntVar()

e_totalLoad = StringVar()
e_numberOfHours = StringVar()

inverterSizeVar = StringVar()
batterySizeVar = StringVar()
panelSizeVar = StringVar()


#INPUT FRAME inputs
totalLoadLabel = Label(inputFrame, text="Please input total load in watts:",  font = ('arial',18,'bold'), width=24)
totalLoadLabel.grid(row=0, column=0, sticky=W)

numberOfHours = Label(inputFrame, text = "Please input load running hours:", font=('arial', 18, 'bold'), width=25)
numberOfHours.grid(row=1, column=0, sticky=W)

batteryTypeLabel = Label(inputFrame, text="Please choose battery type:",  font = ('arial',18,'bold'), width=21)
batteryTypeLabel.grid(row=2, column=0, sticky=W)

lithiumIonBattery = Checkbutton(inputFrame, text="Lithium-ion", onvalue=1, offvalue=0, font=('arial', 18, 'bold'), variable=var1 )
lithiumIonBattery.grid(row=2, column=1, sticky=W)

leadAcidBattery = Checkbutton(inputFrame, text= "Lead-acid", onvalue=1, offvalue=0, font=('arial', 18, 'bold'), variable=var2 )
leadAcidBattery.grid(row=3, column=1, sticky=W)

#empty labels to allow the outputs to be a little lower
emptyLabelOne = Label(inputFrame, text=" ",  font = ('arial',18,'bold'))
emptyLabelOne.grid(row=4, column=0, sticky=W)

emptyLabelTwo  = Label(inputFrame, text=" ",  font = ('arial',18,'bold'))
emptyLabelTwo.grid(row=6, column=0, sticky=W)

emptyLabelThree  = Label(inputFrame, text=" ",  font = ('arial',18,'bold'))
emptyLabelThree.grid(row=10, column=0, sticky=W)


#INPUT FRAME entry field
textTotalLoad = Entry(inputFrame, font=('arial', 11, 'bold'), bd=5, width=19, textvariable=e_totalLoad)
textTotalLoad.grid(row=0, column=1)

textNumberOfHours = Entry(inputFrame, font=('arial', 11, 'bold'), bd=5, width=19, textvariable=e_numberOfHours)
textNumberOfHours.grid(row=1, column=1)

#OUTPUTS
inverterSizeLabel = Label(inputFrame, text='Inverter size for your system', font = ('arial',18,'bold'), width=22)
inverterSizeLabel.grid(row=7, column=0, sticky=W)

batterySizeLabel = Label(inputFrame, text='Battery size for your system', font = ('arial',18,'bold'), width=21)
batterySizeLabel.grid(row=8, column=0, sticky=W)

panelSizeLabel = Label(inputFrame, text='Panel size for your system', font = ('arial',18,'bold'), width=20)
panelSizeLabel.grid(row=9, column=0, sticky=W)

#OUTPUTS ENTRY field
textInverterSize = Entry(inputFrame, font=('arial', 11, 'bold'), bd=5, width=19,  state = 'readonly', textvariable = inverterSizeVar)
textInverterSize.grid(row=7, column=1)

textbatterySize = Entry(inputFrame, font=('arial', 11, 'bold'), bd=5, width=19, state = 'readonly', textvariable = batterySizeVar)
textbatterySize.grid(row=8, column=1)

textpanelSize = Entry(inputFrame, font=('arial', 11, 'bold'), bd=5, width=19, state = 'readonly', textvariable = panelSizeVar)
textpanelSize.grid(row=9, column=1)

#BUTTONS
calculateButton = Button(inputFrame, text='CALCULATE', font=('arial', 11, 'bold'), bd= 3, command = calculator)
calculateButton.grid(row=5, column=0)

clearButton = Button(inputFrame, text='CLEAR', font=('arial', 11, 'bold'), bd= 3, command = clear)
clearButton.grid(row=11, column=0)

#NOTIFICATIONS
noteLabelOne = Label(inputFrame, text=" ",  font = ('arial',10,'bold'), width=24)
noteLabelOne.grid(row=13, column=0, sticky= W )

noteLabelTwo = Label(inputFrame, text=" ",  font = ('arial',10,'bold'), width=24)
noteLabelTwo.grid(row=14, column=0, sticky= W )

sunHoursLabel = Label(inputFrame, text="Note: Number of sun hours estimated is 7hrs ",  font = ('arial',10,'bold'), width=35)
sunHoursLabel.grid(row=15, column=0, sticky= W )

inverterEfficiency = Label(inputFrame, text="Note: Efficiency of inverter has to be not less than 85%  ",  font = ('arial',10,'bold'), width=43)
inverterEfficiency.grid(row=16, column=0, sticky= W )

root.mainloop()