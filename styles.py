import qdarktheme


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
        # additional_qss=qss,
    )


# Colors
PRIMARY_COLOR = "#faad1e"
DARKER_PRIMARY_COLOR = "#d99518"
DARKEST_PRIMARY_COLOR = "#b07912"

# Sizing
X_AND_O_SIZE = 70
BIG_FONT_SIZE = 50
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 18
TEXT_MARGIN = 15
MINIMUM_WIDTH = 500
