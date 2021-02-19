from enum import Enum, unique


@unique
class EventType(Enum):

    def __str__(self):
        return str(self.value)

    LEFT_BUTTON_CLICK = '<Button-1>'
    RIGHT_BUTTON_CLICK = '<Button-3>'
    MIDDLE_BUTTON_CLICK = '<Button-2>'
    CONFIGURE = '<Configure>'
