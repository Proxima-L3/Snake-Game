"""Run SnakeGame from program entry point.

This module imports the RootWindow class and calls its .run() method from which
the program begins.
"""

from menu_screens.root_window import RootWindow


def main() -> None:
    """Create instance of RootWindow and call its run() method."""
    snake = RootWindow()
    snake.run()


if __name__ == '__main__':
    main()
