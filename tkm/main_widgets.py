import tkinter as tk

class GUI:
    """The GUI class for an app.
    """
    def __init__(self, title, geometry, maxsize):
        """
        Args:
            title (string): The title of the GUI.
            geometry (string): The string of 'AxB', where A and B are the X and
            Y size of the GUI respectively.  
            maxsize (List): The Tuple of ints of the maximum X, Y size of the GUI.
        """
        self.__window = Tk()
        self.__title = title
        self.__geometry = geometry
        self.__maxsize = maxsize
        self._widgets = {}
        self.__set_attributes()

    def add_widget(self, widget):
        """Adds a Widget object to the Frame.
        """
        self._widgets[widget.get_id()] = widget
        widget.setup(self.get_frame())

    def __set_attributes(self):
        # set the attributes of the GUI
        self.set_title(self.__title)
        self.set_geometry(self.__geometry)
        self.set_maxsize(self.__maxsize)
        self.set_unresizable()

    def start(self):
        self.__window.mainloop()

    def exit(self):
        """Exits the application.

        Program exit should be called via this.
        """
        self.__window.quit()

    # setters
    def set_title(self, value):
        self.__title = value
        self.__window.title(value)

    def set_geometry(self, value):
        self.__geometry = value
        self.__window.geometry(value)

    def set_maxsize(self, value):
        """
        Args:
            value (List): The List of int of X, Y size.
        """
        self.__maxsize = value
        self.__window.maxsize(self.__maxsize[0], self.__maxsize[1])

    def set_unresizable(self):
        self.__window.resizable(width=False, height=False)

    # getters
    def get_parent_frame(self):
        return self.__window

    def get_widget_keys(self):
        return self._widgets.keys()

    def get_widget(self, widget_name):
        """
        Returns:
            The widget specified, or None if not found.
        """
        try:
            return self._widgets[widget_name]
        except KeyError:
            return None

    def get_frame(self):
        return self.__window
