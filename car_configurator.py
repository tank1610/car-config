from tkinter import *

class CarBuilder():
    '''
    The class to build a car model
    '''
    def __init__(self):
        self.car_type = ''
        self.car_size = ''
        self.wheels = {'size': '',
                       'material': ''}
        self.colour = ''
        self.window_type = ''
        self.transmission = ''
        self.battery = ''
        self.car_options = {}

    def get_widgets(self):
        #Provides a list of available widgets for each car type
        return self.car_options[self.car_type]
    def get_wheels(self):
        return self.wheels
    def get_type(self):
        return self.car_type
    def get_size(self):
        return self.car_size
    def get_colour(self):
        return self.colour
    def get_windows(self):
        return self.window_type
    def get_transmission(self):
        return self.transmission
    def get_battery(self):
        return self.battery
    def get_car_options(self):
        return self.car_options.keys()
    def get_overview(self):
        if self.car_type == 'Petrol':
            return (f"Car type: {self.car_type}\nCar size: {self.car_size}\nColour: {self.colour}\n"
                               f"Wheels: {self.wheels}\nTransmission: {self.transmission}")
        else:
            return (f"Car type: {self.car_type}\nCar size: {self.car_size}\nColour: {self.colour}\n"
                               f"Wheels: {self.wheels}\nBattery: {self.battery}")
    def set_wheels_size(self, size):
        self.wheels['size'] = size
    def set_wheels_material(self, material):
        self.wheels['material'] = material
    def set_type(self, car_type):
        self.car_type = car_type
    def set_size(self, car_size):
        self.car_size = car_size
    def set_colour(self, colour):
        self.colour = colour
    def set_windows(self, windows):
        self.window_type = windows
    def set_transmission(self, transmission):
        self.transmission = transmission
    def set_battery(self, battery):
        self.battery = battery
    def set_car_options(self, car_options):
        self.car_options = car_options

class CarConfigGUI():
    '''
    The GUI class that creates and exposes GUI elements of the configurator
    
    The inputs and output are framed separately.

    The input frame contains 2 separate frames:
            *option_frame which contains the button to select car type.
            *config_frame which contains the configuration options.
    The output frame contains a Text widget to describe the car.
    '''
    def __init__(self,master, new_car):

        '''
        Initialise the frames and populate them with the initial widgets.
        Initilise a new car to configure.
        '''
        self.master = master
        master.title("Car Configurator")

        self.input_frame = Frame(master, highlightbackground="black", highlightcolor="black",
                                 highlightthickness=1)
        self.input_frame.grid(row=0, column=0)
        self.option_frame = Frame(self.input_frame)
        self.option_frame.grid(row=0)

        self.config_frame = Frame(self.input_frame)
        self.config_frame.grid(row=1)

        self.output_frame = Frame(master, highlightbackground="black", highlightcolor="black",
                                  highlightthickness=1)
        self.output_frame.grid(row=0, column=1)
        self.car_output = Text(self.output_frame)
        self.car_output.insert(INSERT, '')
        self.car_output.pack()
        # self.output_label = Label(self.output_frame, text="Output")
        # self.output_label.pack()
        self.new_car = new_car
        self.add_car_menu()



    def add_car_menu(self):
        '''
        Provides a menu to select from available car types. A button is also
        added to confirm the configuration to update the output.
        '''
        car_list = self.new_car.get_car_options()
        selected_type = StringVar()

        option_menu = OptionMenu(self.option_frame, selected_type, *car_list,
                                 command=self.display_config)
        
        self.input_label = Label(self.option_frame, text="Car type ")
        self.input_label.grid(row=0)
        option_menu.grid(row=0,column=1)
        self.confirm_button = Button(self.option_frame, text='Confirm', command=self.update_overview)
        self.confirm_button.grid(row=0,column=2)

    def display_config(self, selected_type):
        '''
        Calls a function depending on the car type.
        '''
        for widget in self.config_frame.winfo_children(): #clear the frame of widgets
            widget.destroy()

        self.new_car.set_type(selected_type)
        available_options = self.new_car.get_widgets()
        for option in available_options:
            self.add_widget(*option)
    def update_overview(self):
        '''
        Updates the output field with the car's properties.
        '''
        self.car_output.delete('1.0', END)
        self.car_output.insert(INSERT, self.new_car.get_overview())

    def add_widget(self, labeltext, widgettype, row, options=None, function=None):
        '''
        Function to add generic widgets.
        '''
        def update_value(event=None):
            function(widget.get())
        if widgettype == 'entry':
            label = Label(self.config_frame, text=labeltext)
            widget = Entry(self.config_frame)
            widget.bind('<Return>', update_value)
            label.grid(row=row,column=0)
            widget.grid(row=row,column=1)
        elif widgettype == 'options':
            label = Label(self.config_frame, text=labeltext)
            selected_var = StringVar()
            widget = OptionMenu(self.config_frame, selected_var,*options,command=function)
            label.grid(row=row,column=0)
            widget.grid(row=row,column=1)

if __name__ == "__main__":
    new_car = CarBuilder()      #Create a new CarBuilder object and give it some options
    new_car.set_car_options({'Petrol': [
                ['Wheel Size: ','entry',1,[], new_car.set_wheels_size],
                ['Wheel Material: ', 'options', 2, ['Aluminium', 'Steel'], new_car.set_wheels_material],
                ['Colour: ', 'options', 3, ['Red', 'Blue', 'Black'], new_car.set_colour],
                ['Car size: ', 'options', 4, ['3-door', '5-door'], new_car.set_size],
                ['Transmission: ', 'options', 5, ['Manual', 'Auto'], new_car.set_transmission]]
                , 'Electric': [
                ['Wheel Size: ','entry',1,new_car.set_wheels_size],
                ['Wheel Material: ', 'options', 2, ['Aluminium', 'Steel'], new_car.set_wheels_material],
                ['Colour: ', 'options', 3, ['Red', 'Blue', 'Black'], new_car.set_colour],
                ['Car size: ', 'options', 4, ['3-door', '5-door'], new_car.set_size],
                ['Battery: ', 'options', 5, ['Small', 'Medium', 'Large'], new_car.set_battery]
            ]})
    root = Tk()
    my_gui = CarConfigGUI(root,new_car)
    root.mainloop()