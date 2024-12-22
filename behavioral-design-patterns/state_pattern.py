from abc import ABC, abstractmethod


class Tool(ABC):
    @abstractmethod
    def mouse_up(self):
        pass

    @abstractmethod
    def mouse_down(self):
        pass


class SelectionTool(Tool):
    def mouse_down(self):
        print('Selection icon')
        return super().mouse_down()

    def mouse_up(self):
        print('Draw a dashed rectangle')
        return super().mouse_up()


class BrushTool(Tool):
    def mouse_down(self):
        print('Brush icon')
        return super().mouse_down()

    def mouse_up(self):
        print('Draw a line')
        return super().mouse_up()


class EraserTool(Tool):
    def mouse_down(self):
        print('Eraser icon')
        return super().mouse_down()

    def mouse_up(self):
        print('Erase something')
        return super().mouse_up()


class Canvas:
    def __init__(self, current_tool: Tool):
        self.current_tool = current_tool

    @property
    def current_tool(self):
        return self.__current_tool

    @current_tool.setter
    def current_tool(self, tool: Tool):
        self.__current_tool = tool

    def mouse_down(self):
        self.__current_tool.mouse_down()

    def mouse_up(self):
        self.__current_tool.mouse_up()


selection_tool = SelectionTool()
canvas = Canvas(selection_tool)
canvas.mouse_down()
canvas.mouse_up()
