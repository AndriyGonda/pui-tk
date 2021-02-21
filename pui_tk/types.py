from enum import Enum, unique


class StrEnum(Enum):
    def __str__(self):
        return str(self.value)


@unique
class EventType(StrEnum):
    LEFT_BUTTON_CLICK = '<Button-1>'
    RIGHT_BUTTON_CLICK = '<Button-3>'
    MIDDLE_BUTTON_CLICK = '<Button-2>'
    CONFIGURE = '<Configure>'
    KEY_RELEASE = '<KeyRelease>'
    KEY_PRESS = '<KeyPress>'


class TkProperty:
    def __init__(self, name, type=object):
        self._name = name
        self._type = type

    def __get__(self, instance, owner):
        return instance.tk_ref[self._name]

    def validate(self, value):
        pass

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise TypeError(f'Invalid type. Expected {self._type} type.')
        self.validate(value)
        instance.tk_ref[self._name] = value


@unique
class Cursor(StrEnum):
    ARROW = 'arrow'
    DOT = 'dot'
    CIRCLE = 'circle'
    CLOCK = 'clock'
    CROSS = 'cross'
    DOTBOX = 'dotbox'
    EXCHANGE = 'exchange'
    FLEUR = 'fleur'
    HEART = 'heart'
    MAN = 'man'
    MOUSE = 'mouse'
    PIRATE = 'pirate'
    PLUS = 'plus'
    SHUTTLE = 'shuttle'
    SIZING = 'sizing'
    SPIDER = 'spider'
    SPRAYCAN = 'spraycan'
    STAR = 'star'
    TARGET = 'target'
    TCROSS = 'tcross'
    TREK = 'trek'
    WATCH = 'watch'


@unique
class Relief(StrEnum):
    FLAT = 'flat'
    RAISED = 'raised'
    SUNKEN = 'sunken'
    GROOVE = 'groove'
    RIDGE = 'ridge'
    SOLID = 'solid'


@unique
class Justify(StrEnum):
    LEFT = 'left'
    CENTER = 'center'
    RIGHT = 'right'


@unique
class Side(StrEnum):
    TOP = 'top'
    BOTTOM = 'bottom'
    LEFT = 'left'
    RIGHT = 'right'


@unique
class State(StrEnum):
    ACTIVE = 'active'
    NORMAL = 'normal'
    DISABLED = 'disabled'
