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
    BOAT = 'boat'
    BOGOSITY = 'bogosity'
    BOTTOM_LEFT_CORNER = 'bottom_left_corner'
    BOTTOM_RIGHT_CORNER = 'bottom_right_corner'
    BOTTOM_SIDE = 'bottom_side'
    BOTTOM_TEE = 'bottom_tee'
    BOX_SPIRAL = 'box_spiral'
    CENTER_PTR = 'center_ptr'
    CIRCLE = 'circle'
    CLOCK = 'clock'
    COFFEE_MUG = 'coffee_mug'
    CROSS = 'cross'
    CROSS_REVERSE = 'cross_reverse'
    CROSSHAIR = 'crosshair'
    DIAMOND_CROSS = 'diamond_cross'
    DOT = 'dot'
    DOTBOX = 'dotbox'
    DOUBLE_ARROW = 'double_arrow'
    DRAFT_LARGE = 'draft_large'
    DRAFT_SMALL = 'draft_small'
    DRAPED_BOX = 'draped_box'
    EXCHANGE = 'exchange'
    FLEUR = 'fleur'
    GOBBLER = 'gobbler'
    GUMBY = 'gumby'
    HAND1 = 'hand1'
    HAND2 = 'hand2'
    HEART = 'heart'
    ICON = 'icon'
    IRON_CROSS = 'iron_cross'
    LEFT_PTR = 'left_ptr'
    LEFT_SIDE = 'left_side'
    LEFT_TEE = 'left_tee'
    LEFTBUTTON = 'leftbutton'
    LL_ANGLE = 'll_angle'
    LR_ANGLE = 'lr_angle'
    MAN = 'man'
    MIDDLEBUTTON = 'middlebutton'
    MOUSE = 'mouse'
    PENCIL = 'pencil'
    PIRATE = 'pirate'
    PLUS = 'plus'
    QUESTION_ARROW = 'question_arrow'
    RIGHT_PTR = 'right_ptr'
    RIGHT_SIDE = 'right_side'
    RIGHT_TEE = 'right_tee'
    RIGHTBUTTON = 'rightbutton'
    RTL_LOGO = 'rtl_logo'
    SAILBOAT = 'sailboat'
    SB_DOWN_ARROW = 'sb_down_arrow'
    SB_H_DOUBLE_ARROW = 'sb_h_double_arrow'
    SB_LEFT_ARROW = 'sb_left_arrow'
    SB_RIGHT_ARROW = 'sb_right_arrow'
    SB_UP_ARROW = 'sb_up_arrow'
    SB_V_DOUBLE_ARROW = 'sb_v_double_arrow'
    SHUTTLE = 'shuttle'
    SIZING = 'sizing'
    SPIDER = 'spider'
    SPRAYCAN = 'spraycan'
    STAR = 'star'
    TARGET = 'target'
    TCROSS = 'tcross'
    TOP_LEFT_ARROW = 'top_left_arrow'
    TOP_LEFT_CORNER = 'top_left_corner'
    TOP_RIGHT_CORNER = 'top_right_corner'
    TOP_SIDE = 'top_side'
    TOP_TEE = 'top_tee'
    TREK = 'trek'
    UL_ANGLE = 'ul_angle'
    UMBRELLA = 'umbrella'
    UR_ANGLE = 'ur_angle'
    WATCH = 'watch'
    XTERM = 'xterm'
    X_CURSOR = 'X_cursor'


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
