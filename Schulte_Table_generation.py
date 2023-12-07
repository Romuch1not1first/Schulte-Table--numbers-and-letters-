import numpy as np
import matplotlib.pyplot as plt
from matplotlib.table import Table
import string
import curses


def draw_shulte_table_with_custom_letters(size=5, use_cyrillic=False):
    """Draws a Shulte table with both numbers and custom letters (Latin or Cyrillic) of the specified size."""
    if use_cyrillic:
        # Limit the number of Cyrillic letters depending on the table size
        letters = np.array(['А', 'Б', 'В', 'Г', 'Д'][:size])
    else:
        # Limit the number of Latin letters
        letters = np.array(list(string.ascii_uppercase[:size]))

    # Create an array of elements, taking into account the limited number of letters
    numbers = np.arange(1, size ** 2 - len(letters) + 1)
    elements = np.concatenate((numbers, letters))
    np.random.shuffle(elements)
    elements = elements.reshape((size, size))

    # Create a matplotlib table to display the Shulte table
    fig, ax = plt.subplots(figsize=(8, 8))  # Increase figure size for larger cells
    ax.set_axis_off()
    tb = Table(ax, bbox=[0, 0, 1, 1])

    # Add cells with numbers and letters
    for i in range(size):
        for j in range(size):
            # Create a cell
            cell = tb.add_cell(i, j, 1/size, 1/size, text=elements[i, j], 
                               loc='center', facecolor='white')
            # Set the properties of the cell
            cell.set_fontsize(20)  # Increase font size
            cell.set_edgecolor('black')
            cell.set_text_props(color='black')

    # Add the table to the axes and display it
    ax.add_table(tb)
    plt.show()


def main(stdscr):
    # Initial parameters
    size = 3
    use_cyrillic = False

    # Customizing curses
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.clear()

    while True:
        stdscr.clear()
        stdscr.addstr(f"Current size: {size}\n")
        stdscr.addstr(f"Use Cyrillic: {'Yes' if use_cyrillic else 'No'}\n")
        stdscr.addstr("Press UP/DOWN to change size, LEFT/RIGHT to toggle Cyrillic, ENTER to draw table, Q to quit\n")

        # Keystroke processing
        key = stdscr.getch()
        if key == curses.KEY_UP and size < 9:
            size += 1
        elif key == curses.KEY_DOWN and size > 1:
            size -= 1
        elif key == curses.KEY_RIGHT or key == curses.KEY_LEFT:
            use_cyrillic = not use_cyrillic
        elif key == 10:  # ENTER key code
            # Close curses and open a Schulte table
            curses.endwin()
            draw_shulte_table_with_custom_letters(size, use_cyrillic)
            return
        elif key == ord('q') or key == ord('Q'):
            break

curses.wrapper(main)
