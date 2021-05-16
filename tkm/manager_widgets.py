##################################################
# Manager Widgets
##################################################

# Contains Widgets that are meant to hold other Widgets.

# These manager Widgets come in the form of tabs or sidebars or anything similar.

import tkinter as tk
from tkinter import *
from tkinter.ttk import *

from .base_widgets import Frame_Widget, Button_Widget

class Tab_Sidebar_Widget(Frame_Widget):
    """The Widget containing the ability to tab between multiple tabs,
    whcih act as a sidebar.

    Contains two segments. Top segment is a Frame_Widget that has Button_Widgets to
    switch between different tabs, and takes the first row. The bottom segment is 
    another Frame_Widget that contains the tabs in the sidebar.

    Add any Frame_Widgets to this Widget in order to add them to the sidebar.
    The buttons are automatically generated.
    """
    def __init__(self, id, parent=None, column_start=0, column_end=10, row_start=0,\
        row_end=10, padx=1, pady=1, ipadx=1, ipady=1, sticky='nsew',\
            bg=None, borderwidth=1, border_color=''):
        super().__init__(id=str(id), parent=parent, column_start=column_start,\
            column_end=column_end, row_start=row_start,\
                row_end=row_end, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady,\
                        sticky=sticky, bg=bg, borderwidth=borderwidth)
        # for containing the buttons to switch tabs
        self.__button_wrapper = Frame_Widget('button_wrapper', \
            column_start=column_start, column_end=column_end, row_start=row_start,\
                row_end=row_start, padx=padx, pady=0, ipadx=ipadx, ipady=ipady,\
                    sticky='new', border_color='black', borderwidth=0, bg='white')

        # for containing the tabs
        self.__tab_wrapper = Frame_Widget('tab_wrapper', \
            column_start=column_start, column_end=column_end, row_start=row_start + 1,\
                row_end=row_end - 1, padx=padx, pady=0, ipadx=ipadx, ipady=ipady,\
                    sticky='new', border_color='black', borderwidth=0, bg='white')

        # for adding on any other widgets
        self.__bottom_wrapper = Frame_Widget('bottom_wrapper', \
            column_start=column_start, column_end=column_end, row_start=row_end,\
                row_end=row_end, padx=padx, pady=0, ipadx=ipadx, ipady=ipady,\
                    sticky='new', border_color='black', borderwidth=0, bg='white')

        if bg is None:
            bg_cover_frame = 'white'
        else:
            bg_cover_frame = bg

        self.__cover_frame = Frame_Widget('cover', parent=self.get_widget(),\
            column_start=column_start, column_end=column_end, row_start=row_start + 1,\
                row_end=row_end - 1, padx=padx, pady=0, ipadx=ipadx, ipady=ipady,\
                    sticky='nsew', bg=bg_cover_frame)

        self.__num_tabs = 0
        self.__first_widget_id = None
        self.__borderwidth = borderwidth
        self.__border_color = border_color

    def __init_widget(self, parent):
        self.set_widget(tk.Frame(parent, height=self.get_height(), \
            width=self.get_width(), bg=self.get_bg(), \
                borderwidth=self.get_borderwidth()))
        if self.__border_color is not None:
            self.get_widget().config(highlightbackground=self.__border_color)
            self.get_widget().config(highlightthickness=self.__borderwidth)

        self.init_grid()
        self.set_init()

    def __add_button_to_sidebar(self):
        """Adds a button to this Widget.
        """
        self.__button_wrapper.add_widget(Button_Widget('button_' + str(self.__num_tabs),\
            'Tab ' + str(self.__num_tabs), column_start=self.__num_tabs, \
                column_end=self.__num_tabs, row_start=self.get_row_start(),\
                    row_end=self.get_row_start(), padx=self.get_padx(), \
                        pady=self.get_pady(),ipadx=self.get_ipadx(),\
                            ipady=self.get_ipady()))

        self.__button_wrapper.set_column_weight(self.__num_tabs,\
            self.__num_tabs, 1)

    def __switch_to_tab(self, id):
        """Binds the switching function to 
        """
        # lower all widgets before lifting the specified one
        for key in self.__tab_wrapper.get_child_widgets().keys():
            if key != 'tab_wrapper' and key != 'cover':
                self.__tab_wrapper.get_child_widget(key).get_widget().lower(self.__cover_frame.get_widget())

        self.__tab_wrapper.get_child_widget(id).get_widget().lift(self.__cover_frame.get_widget())

    def setup(self, parent):
        """Inits the widget to a parent widget.
        """
        self.__init_widget(parent)
        self.init_grid()
        self.add_widget(self.__button_wrapper)
        self.add_widget(self.__tab_wrapper)
        self.__tab_wrapper.add_widget(self.__cover_frame)

        self.__button_wrapper.set_row_weight(self.get_row_start(),\
            self.get_row_start(), 1)

    def add_tab(self, widget):
        if self.__first_widget_id is None:
            self.__first_widget_id = widget.get_id()

        self.__tab_wrapper.add_widget(widget)
        self.__add_button_to_sidebar()

        # use lambda to bind the function with the id of the widget
        self.__button_wrapper.get_child_widget(self.get_button_id(self.__num_tabs)).\
            bind_function(lambda: self.__switch_to_tab(widget.get_id()))

        self.__num_tabs += 1

    def switch_to_first_tab(self):
        self.__switch_to_tab(self.__first_widget_id)

    def add_widget_to_bottom(self, widget):
        """Adds a Widget to the bottom Frame_Widget of this Widget.
        """
        self.__bottom_wrapper.add_widget(widget)

    def set_tab_name(self, index, value):
        """Sets the name of the tab at the given index.
        """
        self.__button_wrapper.get_child_widget('button_' + str(index)).set_text(value)

    def get_child_widget(self, widget_name):
        return self.__tab_wrapper.get_child_widget(widget_name)

    def get_child_widget_keys(self):
        return self.__tab_wrapper.get_child_widget_keys()

    def get_button_id(self, index):
        """Returns the ID of the Button_Widget specified by the index.
        """
        return 'button_' + str(index)
