# Car configuring app
The car configuring app, developed with Python 3.7.1 using Tkinter. 

## Summary
The app contains 2 classes: `CarBuilder` and `CarConfigGUI`

`CarConfigGUI` creates the GUI of the app.  `Frames` are used to organise the elements and widgets of this GUI. The input frame is on the left and the output frame is on the right. The output frame is filled with a `Text` widget and provides the overview of the car. The input frame is populated by different widgets depending on the type of car selected.

During initialisation of the app, a new `CarBuilder` object is created. This object provides the list of car types that populates the `Car type` dropdown menu as well as the widgets that are available for each car type. This means that more widgets can be added without modifying the `CarConfigGUI` class.

The car can be configured using the widgets provided. Once the form is filled out, the user can press the `Confirm` button and the output field will provide an overview of the car.

In the `CarBuilder` class, the available car types and their associated configurable options are stored using a Dict. The key of each element is the type of the car, and the value is a list. Each element of this list is an available option. For example:
 `{'Petrol': [['Wheel Size: ','entry',1,[], new_car.set_wheels_size]]}`
 Here, the car type is Petrol. The list is used to generate the widget to change the wheel size. 
 - `labeltext` is used to create the label.
 - `widgettype` is an indicator of which type of widget this is, in this case a textbox.
 - `row` position of this widget on the input frame.
 - `options=None` a list of options for widgets that offer list selections.
 - `function=None` the function associated with this widget.