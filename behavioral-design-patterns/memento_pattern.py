class EditorState:
    def __init__(self, content):
        self.content = content

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value


class Editor:
    def __init__(self, content=''):
        self.content = content

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value

    def create_state(self):
        return EditorState(self.__content)

    def restore(self, state: EditorState):
        try:
            self.__content = state.content
        except AttributeError:
            print('No content found.')

    def __repr__(self):
        return self.__content


class History:
    def __init__(self):
        self.states: list = []

    def push(self, state: EditorState):
        self.states.append(state)

    def pop(self):
        if len(self.states) == 0:
            print('State is empty!')
        else:
            return self.states.pop()


editor = Editor()
history = History()

editor.content = 'Added file via upload'
history.push(editor.create_state())

editor.content = 'Uploaded file via shell'
history.push(editor.create_state())

editor.content = 'Deleted file'
editor.restore(history.pop())
