"""Run SnakeGame from program entry point.

This module imports the RootWindow class and calls its .run() method from which
the program begins.
"""

import asyncio
from menu_screens.root_window import RootWindow


async def main() -> None:
    """Create instance of RootWindow and call its run() method."""
    snake = RootWindow()
    await snake.run()


if __name__ == '__main__':
    asyncio.run(main())
