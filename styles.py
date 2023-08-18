import qdarktheme

# Colors
PRIMARY_COLOR = "#d1d1d1"
DARKER_PRIMARY_COLOR = "#949494"
DARKEST_PRIMARY_COLOR = "#616161"

# FONTS
FONT_FAMILY = "Baloo,Arial"

# Sizing
X_AND_O_SIZE = 70
BIG_FONT_SIZE = 50
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 18
TEXT_MARGIN = 15
MINIMUM_WIDTH = 500

qss = f"""
    QPushButton[cssClass="ButtonCSS"] {{
        color: #232323;
        background: {PRIMARY_COLOR};
        font-family: {FONT_FAMILY};
    }}
    QPushButton[cssClass="ButtonCSS"]:hover {{
        color: #232323;
        background: {DARKER_PRIMARY_COLOR};
        font-family: {FONT_FAMILY};
    }}
    QPushButton[cssClass="ButtonCSS"]:pressed {{
        color: #232323;
        background: {DARKEST_PRIMARY_COLOR};
        font-family: {FONT_FAMILY};
    }}"""


def setupTheme():
    qdarktheme.setup_theme(
        theme="dark",
        corner_shape="rounded",
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}",
            },
            "[light]": {
                "primary": f"{PRIMARY_COLOR}",
            },
        },
        additional_qss=qss,
    )
