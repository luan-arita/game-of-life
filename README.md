# Conway's Game of Life

The Conway's Game of Life is a cellular automaton. A cellular automaton consists of a regular grid of cells, where each one is described by a kind of state (such as on/off or live/dead). Each cell interacts with eight of its neighbours, which are the cells directly adjacent to it. At each step of time, each cell updates its own state according to four rules:

1. Any live cell with 0 or 1 live neighbors become dead, because of underpopulation
2. Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
3. Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
4. Any dead cell with exactly 3 neighbours becomes alive, by reproduction

By creating a initial pattern, which could be a random set of alive and dead cells or predefined formations, we can watch how births and deaths happen simultaneously to every cell and create unbelievably complex and beautiful patterns.

Therefore, the "game" is actually a zero-player game, meaning that its evolution is determined by its initial state, needing no input from human players. You just interact with the Game of Life by creating an initial configuration and observe how it evolves.

## Other Cellular Automata

### Langton's Ant
Instead of a cell being dead or alive, these rules define the movement of a ant in a plane. The squares in a plane are colored black or white, and we arbitrarily identify one square as being the ant. The ant moves according to these rules:
1. At a white square, turn 90° clockwise, flip the color of the square and move forward one unit.
2. At a black square, turn 90° counter-clockwise, flip the color of the square and move forward one unit.
![](https://upload.wikimedia.org/wikipedia/commons/0/09/LangtonsAntAnimated.gif)

These simple rules end up creating distinct modes of behavior. The ant starts out by creating simple patterns which are often symmetric. After a few hundred moves, it starts moving in irregular patterns and it traces a pseudo-random path until around 10,000 steps. The ant ends up finding order amidst the chaos, and starts building a "highway pattern" which repeats indefinitely.

### Brian's Brain

Besides the alive or dead, this cellular automaton adds a third "dying" state. Each cell is considered to have eight neighbors, as in Conway's Game of Life. In each time step, the same rules from Conway's are applied, however all cells that were "alive" go into the "dying" state instead, which does not count as "alive" in the neighbor count and prevents any cell from being born there. Cells that were already in the dying state then goes into the dead state.



# Usage

```python -u main.py imageFilename [-i] [-c] [-m {1, 2, 3}] [-hs HEIGHT]```

Conway's Game of Life

options:

  `-h, --help`:                       show this help message and exit
  
  `-w WIDTH, --width WIDTH`:          Choose board's width.
  
  `-hs HEIGHT, --height HEIGHT`:      Choose board's height.
  
  `-g {1,2,3,4}, --game {1,2,3,4}`:   Choose which cellular automata you want to run. 1 is the default Game of Life, 2 is Langton's Ant, 3 is Seeds and 4 is Brian's Brain. 
    
  `-f FILE, --file FILE`

  By default, the board will be 100x100 and the initial state for the Game of Life will be a random one.

# Features

- Conway's Game of Life. 

