#!/usr/bin/env python3


_maze = ['#################################',
        'S   #     #               #   # #',
        '# # # ##### ########### # # # # #',
        '# #   #     #     #     #   #   #',
        '# ### # ####### # # #############',
        '#   #   #     # # #       #     #',
        '### ##### # # # # ####### # ### #',
        '#   #   # # #   # #       #   # #',
        '# ### # # ####### # ####### ### #',
        '#     # #   #   # #   #     #   #',
        '####### ### ### ### # # ##### ###',
        '#       # #       # # #     #   #',
        '# ####### # ### # ### ##### # ###',
        '#   #     # #   # #   #   # #   #',
        '### # ####### # # # # # # # ### #',
        '#     #       # #   #   #   #   G',
        '#################################']


def setup_maze():
    maze = []
    for l in _maze:
        maze.append(list(l))
    return maze


def display(maze):
    for row in maze:
        print("".join(row))


def is_goal(maze, pos):
    return True if maze[pos[0]][pos[1]] == 'G' else False


def mark(maze, pos):
    maze[pos[0]][pos[1]] = '.'


def mark_goal(maze, pos):
    maze[pos[0]][pos[1]] = '@'


def is_unexplored_path(maze, pos):
    if pos[0] >= 0 and pos[1] >= 0:
        if maze[pos[0]][pos[1]] == ' ' or is_goal(maze, pos):
            return True
    return False


def go_right(pos):
    return (pos[0], pos[1] + 1)


def go_up(pos):
    return (pos[0] - 1, pos[1])


def go_left(pos):
    return (pos[0], pos[1] - 1)


def go_down(pos):
    return (pos[0] + 1, pos[1])


def explore(maze, pos):
    if is_goal(maze, pos):
        mark_goal(maze, pos)
        return True
    mark(maze, pos)
    if is_unexplored_path(maze, go_right(pos)) and explore(maze, go_right(pos)):     # Right
        return True
    elif is_unexplored_path(maze, go_up(pos)) and explore(maze, go_up(pos)):         # Up
        return True
    elif is_unexplored_path(maze, go_left(pos)) and explore(maze, go_left(pos)):     # Left
        return True
    elif is_unexplored_path(maze, go_down(pos)) and explore(maze, go_down(pos)):     # Down
        return True
    else:
        return False


if __name__ == '__main__':
    maze = setup_maze()
    if explore(maze, (1, 0)):  # Assuming (1, 0) is Start
        # Found path to goal
        display(maze)
    else:
        print("No route to Goal")

