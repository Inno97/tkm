
# Tkinter Manager
A framework that utilizes Tkinter and provides a simplified way to create GUI in Python.

## Preface

This framework builds upon tkinter and provides different Widget classes to manage GUI elements in a Python application. The goal of this framework is to abstract away the many method calls needed to setup tkinter Widgets and allow the user to easily track and manipulate these Widgets objects.

This framework (tkm) will not be able to fulfil all the user's needs in every application, but can be built off and improved on by the user should there not be a Widget that satisfies a specific use.

## Using the framework

As this framework builds off tkinter, it will use the same attributes that tkinter uses in configuring the Widgets. In general, Widgets in this framework will provide default values if the user does not specify them.

Child Widgets are meant to be added onto a parent Frame_Widget object, which should control access to the child Widgets. Actual placement of Widgets in the GUI is governed by the Grid system in tkinter, which utilizes rows and columns. 

Widgets in tkm will have the following common attributes:
1. column_start / row_start / column_end / row_end - The starting column / row of the Widget
2. padx / pady / ipadx / ipady - External and internal X and Y padding of the Widget
3. sticky - Where the Widget will be aligned to in its parent Widget
4. id - A string to identify the Widget as

Note that a child Widget's Grid rows and columns cannot exceed its parent.

### Manipulating Widgets

In order to add a Widget, they must be created with the appropriate arguments and then added to its parent via the add_widget() method:

> self.__sidebar_wrapper = tkm.base_widgets.Frame_Widget('file_wrapper', \
column_start=0, column_end=10, row_start=0, row_end=100,\
padx=10, pady=0, sticky='new')
parent.add_widget(self.__sidebar_wrapper)

In this example, a Frame_Widget object called __sidebar_widget is created and then added onto a parent object (declared elsewhere).
