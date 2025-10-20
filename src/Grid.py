class Grid:
    def __init__(self, width: int, height: int):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")

        self._width = width
        self._height = height

    @property
    def width(self) -> int:
