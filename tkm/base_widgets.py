##################################################
# Base Widgets
##################################################

# Contains the basic Widgets to be used.
# Advanced widgets should be based off a combination of these Widgets.
import tkinter as tk
from tkinter import *

class Widget:
    """The basic widget object to be inherited by other classes.

    Contains the methods for setting up the Widget via Grid().

    For any handling of dimensions, do it in the child class that inherits this.
    """
    def __init__(self, id='', widget=None, column=1, columnspan=1, row=1, rowspan=1,\
        padx=1, pady=1, ipadx=1, ipady=1, sticky='ew'):
        self.__id = id
        self._widget = widget
        self.__column = column
        self.__columnspan = columnspan
        self.__row = row
        self.__rowspan = rowspan
        self.__padx = padx
        self.__pady = pady
        self.__ipadx = ipadx
        self.__ipady = ipady
        self.__sticky = sticky
        self.__is_init = False

    def __init_widget(self):
        raise NotImplementedError('Widget has no __init_widget() method overridden')

    def init_grid(self):
        """Uses the Grid geometry manager to organize Widget.
        """
        if self.__rowspan == 0 and self.__columnspan == 0:
            self._widget.grid(column=self.__column, row=self.__row,\
                padx=self.__padx, pady=self.__pady,ipadx=self.__ipadx,\
                    ipady=self.__ipady, sticky=self.__sticky)
        elif self.__rowspan == 0 :
            self._widget.grid(column=self.__column, row=self.__row,\
                columnspan=self.__columnspan, padx=self.__padx, pady=self.__pady,\
                    ipadx=self.__ipadx, ipady=self.__ipady, sticky=self.__sticky)
        elif self.__columnspan == 0:
            self._widget.grid(column=self.__column, row=self.__row,\
                rowspan=self.__rowspan, padx=self.__padx, pady=self.__pady,\
                    ipadx=self.__ipadx, ipady=self.__ipady, sticky=self.__sticky)
        else:
            self._widget.grid(column=self.__column, row=self.__row,\
                columnspan=self.__columnspan, rowspan=self.__rowspan,\
                    padx=self.__padx, pady=self.__pady, ipadx=self.__ipadx,\
                        ipady=self.__ipady, sticky=self.__sticky)

    def setup(self, parent):
        """Inits the widget to a parent widget.
        """
        self.__init_widget(parent)
        self.__init_grid()

    def enable_widget(self):
        self._widget.configure(state='enabled')

    def disable_widget(self):
        self._widget.configure(state='disabled')

    # setters
    def set_widget(self, widget):
        """Sets internal Widget before __init_widget.
        """
        self._widget = widget

    def set_id(self, value):
        self.__id = value

    def set_column_start(self, value):
        self.__column = value
        if self.__is_init:
            self._widget.grid(column=self.__column, \
                columnspan=self.__columnspan)
        else:
            raise UnboundLocalError('Widget not initialized')

    def set_column_end(self, value):
        self.__columnspan = value - self.__column
        if self.__is_init:
            self._widget.grid(column=self.__column, \
                columnspan=self.__columnspan)
        else:
            raise UnboundLocalError('Widget not initialized')

    def set_row_start(self, value):
        self.__row = value
        if self.__is_init:
            self._widget.grid(row=self.__row, \
                rowspan=self.__rowspan)
        else:
            raise UnboundLocalError('Widget not initialized')

    def set_row_end(self, value):
        self.__rowspan = value - self.__row
        if self.__is_init:
            self._widget.grid(row=self.__row, \
                rowspan=self.__rowspan)
        else:
            raise UnboundLocalError('Widget not initialized')

    def set_padx(self, value):
        self.__padx = value
        if self.__is_init:
            self._widget.grid(padx=value)
        else:
            raise UnboundLocalError('Widget not initialized')

    def set_pady(self, value):
        self.__pady = value
        if self.__is_init:
            self._widget.grid(pady=value)
        else:
            raise UnboundLocalError('Widget not initialized')

    def set_ipadx(self, value):
        self.__ipadx = value
        if self.__is_init:
            self._widget.grid(ipadx=value)
        else:
            raise UnboundLocalError('Widget not initialized')

    def set_ipady(self, value):
        self.__ipady = value
        if self.__is_init:
            self._widget.grid(ipady=value)
        else:
            raise UnboundLocalError('Widget not initialized')

    def set_sticky(self, value):
        self.__sticky = value
        if self.__is_init:
            self._widget.grid(sticky=value)
        else:
            raise UnboundLocalError('Widget not initialized')

    def set_init(self):
        self.__is_init = True

    # getters
    def get_widget(self):
        return self._widget

    def get_id(self):
        return self.__id

    def get_width(self):
        return self.__columnspan

    def get_height(self):
        return self.__rowspan

    def get_column_start(self):
        return self.__column

    def get_column_end(self):
        return self.__columnspan + self.__column

    def get_row_start(self):
        return self.__row

    def get_row_end(self):
        return self.__rowspan + self.__row

    def get_padx(self):
        return self.__padx

    def get_pady(self):
        return self.__pady

    def get_ipadx(self):
        return self.__ipadx

    def get_ipady(self):
        return self.__ipady

    def get_sticky(self):
        return self.__sticky

    def is_init(self):
        return self.__is_init

    def __str__(self):
        return str(self.__id) + ' with col / span / row / span ' + str(self.__column) +\
            ' ' + str(self.__columnspan) + ' ' + str(self.__row) + ' ' +\
                str(self.__rowspan) + ' pad xy / ipad xy ' + str(self.__padx) +\
                    ' ' + str(self.__pady) + ' ' + str(self.__ipadx) + ' ' + \
                        str(self.__ipady) + ' sticky ' + str(self.__sticky) + \
                            ' init: ' + str(self.__is_init)

class Frame_Widget(Widget):
    """The widget containing a Frame, which acts as a container for other widgets.

    Contains a Dictionary of key-value pair for the Widget name and the Widget.
    """
    def __init__(self, id, parent=None, column_start=0, column_end=0,\
        row_start=0, row_end=0, padx=5, pady=5, ipadx=1, ipady=1, \
            sticky='nsew', bg=None, border_color=None, borderwidth=0):
        super().__init__(id=str(id), column=column_start, \
            columnspan=column_end - column_start, row=row_start, \
                rowspan = row_end - row_start, padx=padx, pady=pady, \
                    ipadx=ipadx, ipady=ipady, sticky=sticky)
        """
        Args:
            parent (Frame): The parent window of this widget, defaults to None.
            If provided, inits the widget, else, do not.
            id (string): The ID to identify the widget as.
            padx (int): The external padding in the x-axis for the widget, defaults to 5.
            pady (int): The external padding in the y-axis for the widget, defaults to 5.
            ipadx (int): The internal padding in the x-axis for the widget, defaults to 1.
            ipady (int): The internal padding in the y-axis for the widget, defaults to 1.
        """
        self.__height = row_end - row_start
        self.__width = column_end - column_start
        self.__bg = bg
        self.__borderwidth = borderwidth
        self.__border_color = border_color
        self._widgets = {}

        if parent is not None:
            self.__init_widget(parent)
            self.init_grid()
            self.set_init()

    def __init_widget(self, parent):
        self.set_widget(tk.Frame(parent, height=self.__height,\
            width=self.__width, bg=self.__bg))
        if self.__border_color is not None:
            self.get_widget().config(highlightbackground=self.__border_color)
            self.get_widget().config(highlightthickness=self.__borderwidth)
        self.set_init()

    def setup(self, parent):
        """Inits the widget to a parent widget.
        """
        self.__init_widget(parent)
        self.init_grid()

    def add_widget(self, widget):
        """Adds a Widget object to the Frame.

        Widgets added must be strictly contained inside the parent Widget's Grid.
        Meaning that it must be within the parent's column / row.
        """
        assert self.is_widget_within_frame(widget), 'Widget ' + widget.get_id() + ' exceeds parent Grid coordinates'
        self._widgets[widget.get_id()] = widget
        widget.setup(self.get_frame())

    def is_widget_present(self, widget_name):
        """Returns True if a widget_name exists in the Frame.

        Use this to ensure that no duplicate Widgets are present.
        """
        try:
            self._widgets[widget_name]
            return True
        except KeyError:
            return False

    def is_widget_within_frame(self, widget):
        """Returns True if the Widget will be containined in this Frame Widget.
        """
        return widget.get_column_start() >= self.get_column_start() and \
            widget.get_column_end() <= self.get_column_end() and \
                widget.get_row_start() >= self.get_row_start() and \
                    widget.get_row_end() <= self.get_row_end()

    # setters
    def set_height(self, value): 
        self.__height = value
        self._widget.config(height=value)

    def set_width(self, value): 
        self.__width = value
        self._widget.config(width=value)

    def set_bg(self, value):
        self.__bg = value
        self._widget.config(bg=value)

    def set_borderwidth(self, value):
        self.__borderwidth = value
        self._widget.config(borderwidth=value)

    def set_border_color(self, value):
        self.__border_color = value
        self._widget.config(border_color=value)

    def set_row_weight(self, start_index, end_index, weight):
        """Sets the weight of the given row.

        By default, all rows have weight of 0, which mean that they do not 
        scale at all to the Widget. Setting a value of more than 1 will
        scale the inner child Widgets to the ratio of their weight to the
        total weight of this Frame_Widget.

        Args:
            start_index (int): The starting row to set.
            end_index (int): The ending row to set.
            weight (int): The weight to set to
        """
        for i in range(start_index, end_index + 1):
            self.get_widget().rowconfigure(i, weight=weight)

    def set_column_weight(self, start_index, end_index, weight):
        """Sets the weight of the given column.

        By default, all columns have weight of 0, which mean that they do not 
        scale at all to the Widget. Setting a value of more than 1 will
        scale the inner child Widgets to the ratio of their weight to the
        total weight of this Frame_Widget.

        Args:
            start_index (int): The starting column to set.
            end_index (int): The ending column to set.
            weight (int): The weight to set to
        """
        for i in range(start_index, end_index + 1):
            self.get_widget().columnconfigure(i, weight=weight)
                
    # getters
    def get_child_widget(self, widget_name):
        """Returns the Widget by name, or None if not present.
        """
        try:
            return self._widgets[widget_name]
        except KeyError:
            return None

    def get_child_widget_keys(self):
        return self._widgets.keys()

    def get_child_widgets(self):
        return self._widgets

    def get_height(self): 
        return self.__height

    def get_width(self): 
        return self.__width

    def get_bg(self):
        return self.__bg

    def get_borderwidth(self):
        return self.__borderwidth

    def get_border_color(self):
        return self.__border_color

    def get_frame(self):
        return self.get_widget()

class Label_Text_Widget(Widget):
    """The widget containing a Label for text.

    Width of this Widget in characters is set to the larger of the length of
    text in the Widget, or the difference in column_end and column_start.
    """
    def __init__(self, id, text='',parent=None, column_start=0, column_end=0,\
        row_start=0, row_end=0, padx=5, pady=5, ipadx=1, ipady=1, sticky='nsew',\
            font='', font_size=11):
        super().__init__(id=str(id), column=column_start, \
            columnspan=column_end - column_start, row=row_start, \
                rowspan=row_end - row_start, padx=padx, pady=pady, \
                    ipadx=ipadx, ipady=ipady, sticky=sticky)

        self.__text = text
        self.__font = font
        
        self.__width = max(len(text), column_end - column_start)

        self.__height = row_end - row_start
        self.__font_size = font_size

        if parent is not None:
            self.__init_widget(parent)
            self.init_grid()
            self.set_init()

    def __init_widget(self, parent):
        self.set_widget(tk.Label(parent, text=self.__text))
        try:    
            self.get_widget().config(font=(self.__font, self.__font_size),\
                width=self.__width, height=self.__height, anchor=self.get_sticky())
        except TclError:
            # if the anchor specified is not appropriate
            self.get_widget().config(font=(self.__font, self.__font_size),\
                width=self.__width, height=self.__height, anchor='center')

        self.set_init()

    def setup(self, parent):
        """Inits the widget to a parent widget.
        """
        self.__init_widget(parent)
        self.init_grid()
        self.set_init()

    # setters
    def set_text(self, value): 
        self.__text = value
        self._widget.config(text=value)

    def set_font(self, value): 
        self.__font = value
        self._widget.config(font=value)

    def set_font_size(self, value): 
        self.__font_size = value
        self._widget.config(font_size=value)

    def set_width(self, value):
        self.__width = value
        self.get_widget().config(width=value)
        
    def set_height(self, value):
        self.__height = value
        self.get_widget().config(height=value)

    # getters
    def get_text(self):
        return self.__text

    def get_font(self):
        return self.__font

    def get_font_size(self):
        return self.__font_size

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

class Textbox_Widget(Widget):
    """The widget containing a text box with scroll bar.
    """
    def __init__(self, id, parent=None, column_start=0, column_end=10,\
        row_start=0, row_end=10, padx=5, pady=5, ipadx=1, ipady=1, sticky='nsew',\
            font='', font_size=11):
        super().__init__(id=str(id), column=column_start, \
            columnspan=column_end - column_start, row=row_start, \
                rowspan = row_end - row_start, padx=padx, pady=pady, \
                    ipadx=ipadx, ipady=ipady, sticky=sticky)

        self.__height = row_end - row_start
        self.__width = column_end - column_start

        if parent is not None:
            self.__init_widget(parent)
            self.init_grid()
            self.set_init()

    def __init_widget(self, parent):
        self.set_widget(scrolledtext.ScrolledText(parent, \
            height=self.__height, width=self.__width, state='disabled'))
        self.set_init()
    
    def setup(self, parent):
        """Inits the widget to a parent widget.
        """
        self.__init_widget(parent)
        self.init_grid()

    def write(self, text):
        """Writes the given text to the Textbox, and scrolls down to the end.
        """
        self.get_widget().configure(state='normal')
        self.get_widget().insert(tk.END, text)
        self.get_widget().see('end')
        self.get_widget().configure(state='disabled')
        self.get_widget().update()
        
    def flush(self):
        """Clears the Textbox.
        """
        self.get_widget().configure(state='normal')
        self.get_widget().delete('1.0', 'end')
        self.get_widget().configure(state='disabled')
        self.get_widget().update()

    # setters
    def set_height(self, value): 
        self.__height = value
        self.get_widget().config(height=value)

    def set_width(self, value): 
        self.__width = value
        self.get_widget().config(width=value)
        
    # getters
    def get_text(self):
        return self.get_widget().get('1.0', tk.END)

    def get_height(self): 
        return self.__height

    def get_width(self): 
        return self.__width

class Dropdown_Widget(Widget):
    """The widget containing a dropdown menu.

    A function or method can be passed in to trigger when a new value is selected.
    """
    def __init__(self, id, text='',parent=None, column_start=0, column_end=0,\
        row_start=0, row_end=0, padx=5, pady=5, ipadx=1, ipady=1, sticky='nsew',\
            values=[], current=0, function=None):
        super().__init__(id=str(id), column=column_start, \
            columnspan=column_end - column_start, row=row_start, \
                rowspan = row_end - row_start, padx=padx, pady=pady, \
                    ipadx=ipadx, ipady=ipady, sticky=sticky)

        self.__width = column_end - column_start
        self.__height = row_end - row_start
        self.__values = values
        self.__current = current
        self.__function = function

        if parent is not None:
            self.__init_widget(parent)
            self.bind_function(self.__function)
            self.init_grid()
            self.set_init()

    def __init_widget(self, parent):
        self.set_widget(Combobox(parent, width=self.__width))
        self.set_values(self.__values)
        self.set_init()

    def __init_grid(self):
        self._widget.grid(column=self.__column, row=self.__row, \
            sticky=NSEW, padx=self.__padx, pady=self.__pady, \
                ipadx=self.__ipadx, ipady=self.__ipady)

    def setup(self, parent):
        """Inits the widget to a parent widget.
        """
        self.__init_widget(parent)
        self.init_grid()

    def bind_function(self, function):
        """Binds a function to the Widget.

        Pass in the function (do not include parentheses in the arg).
        """
        if function is not None and self.get_widget() is not None:
            self.get_widget().bind("<<ComboboxSelected>>", function)
            set_function(function)
        elif function is None:
            raise TypeError('None passed in as args')
        else:
            raise AttributeError('Widget not initialized')

    def flush(self):
        self.get_widget().set('')

    # setters
    def set_values(self, values):
        """Sets the values in the dropdown options.

        Args:
            values (List): The List of strings of values for the dropdown options.
        """
        self.__values = values
        self.get_widget()['values'] = values

    def set_current_value(self, index):
        """Sets the current value based on the index of the option.

        Args:
            index (int): The index of the current option as an int.
        """
        self.__current = index
        self.get_widget().current(index)

    def set_width(self, value): 
        self.__width = value
        self.get_widget().config(width=value)
        
    def set_height(self, value): 
        self.__height = value
        self.get_widget().config(height=value)
        
    def set_function(self, value): 
        self.__function = value
        self.get_widget().bind("<<ComboboxSelected>>", function)
        
    # getters
    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_selected_value(self):
        """Gets the current selected value.
        """
        return self.get_widget().get()

    def get_values(self):
        """Gets the List of values in the Widget.
        """
        # TODO: check if self.get_widget()['values'] works
        return self.__values

    def get_selected_value_index(self):
        """Gets the index of the current option selected.
        """
        return self.__current

    def get_function(self):
        """Returns the Function object.
        """
        return self.__function

class Button_Widget(Widget):
    """The widget containing a button.

    Utilizes a custom Style object per button.

    Height is always default to 1.
    Changing of button height is done via internal padding.
    """
    def __init__(self, id, text='',parent=None, column_start=0, column_end=0,\
        row_start=0, row_end=0, padx=5, pady=5, ipadx=1, ipady=1, sticky='nsew',\
            font='', font_size=11, font_color='#000', \
                image=None, function=None):
        super().__init__(id=str(id), column=column_start, \
            columnspan=column_end - column_start, row=row_start, rowspan=row_end - row_start,\
                padx=padx, pady=pady, ipadx=0, ipady=0, sticky=sticky)

        self.__width = column_end - column_start
        self.__image = image
        self.__text = text
        self.__function = function
        self.__is_enabled = True

        # style
        self.__style = str(self.get_id()) + '.TButton'
        self.__style_obj = ttk.Style() # custom style object
        self.__font = font
        self.__font_size = font_size
        self.__font_color = font_color
        
        if parent is not None:
            self.__init_widget(parent)
            self.bind_function(self.__function)
            self.init_grid()
            self.set_init()

    # override
    def __init_widget(self, parent):
        self.set_widget(ttk.Button(parent, text=self.__text, \
            style=self.__style, command=self.__function))
        self.update_style()

    def setup(self, parent):
        """Inits the widget to a parent widget.
        """
        self.__init_widget(parent)
        self.init_grid()

    def bind_function(self, function):
        """Binds a function to the Widget.

        Pass in the function (do not include parentheses in the arg).
        """
        if function is not None:
            self.get_widget().config(command=function)

    def update_style(self):
        self.__style_obj.configure(self.__style, \
            font=(self.__font, self.__font_size))
        self.__style_obj.configure(self.__style, \
            foreground=self.__font_color)

    def toggle_state(self):
        """Toggles the state between enabled and disabled.
        """
        if self.__is_enabled:
            self.get_widget().configure(state='disabled')
        else:
            self.get_widget().configure(state='enabled`')
        self.__is_enabled = not self.__is_enabled

    # setters
    def set_width(self, value):
        self.__width = value
        self.get_widget().config(width=value)

    def set_font_color(self, value): 
        self.__font_color = value
        self.get_widget().config(font_color=value)

    def set_image(self, value): 
        self.__image = value
        # create the PhotoImage object
        self.get_widget().config(image=PhotoImage(file=r + value))

    def set_text(self, value): 
        self.__text = value
        self.get_widget().config(text=value)

    def set_function(self, value): 
        self.__function = value

    def set_style(self, value):
        self.__style = value
        self.get_widget().config(style=value)

    def set_font(self, value): 
        self.get_widget().config(font=value)

    def set_font_size(self, value): 
        self.get_widget().config(font_size=value)

    # getters
    def get_width(self):
        return self.__width

    def get_image(self):
        return self.__image

    def get_text(self):
        return self.__text

    def get_function(self):
        return self.__function

    def get_style(self):
        return self.__style

    def get_font_color(self):
        return self.__font_color

    def get_font(self):
        return self.__font

    def get_font_size(self):
        return self.__font_size
