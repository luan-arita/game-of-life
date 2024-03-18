# Conway's Game of Life

The Conway's Game of Life is actually a zero player game, where every cell follows a set of rules:

1. Any live cell with 0 or 1 live neighbors become dead, because of underpopulation
2. Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
3. Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
4. Any dead cell with exactly 3 neighbours becomes alive, by reproduction

By creating a initial pattern, which could be a random set of alive and dead cells or predefined formations, we can watch how births and deaths happen simultaneously to every cell and create unbelievably complex and beautiful patterns.

# Usage

Type in terminal:  ```python -u main.py [-w WIDTH] [-hs HEIGHT] [-g {1, 2, 3 4}] [-f] FILENAME```


options:

  `-h, --help`:                       show this help message and exit
  
  `-w WIDTH, --width WIDTH`:          Choose board's width.
  
  `-hs HEIGHT, --height HEIGHT`:      Choose board's height.
  
  `-g {1,2,3,4}, --game {1,2,3,4}`:   Choose which cellular automata you want to run. 1 is the default Game of Life, 2 is Langton's Ant, 3 is Seeds and 4 is Brian's Brain. 
    
  `-f FILE, --file`:                  Choose file for assigning initial state of the board.

  # Features

  By default, the board will be 100x100 and the initial state for the Game of Life will be a random one.

  By using _matplotlib's_ `FuncAnimation`, life can be watched.
  
<img src = "https://github.com/luan-arita/game-of-life/assets/35427506/fd0e8886-c0e6-40b6-a5ca-7c663eecba30" width = "600">



  Also features file input:
  
  <img src = "https://github.com/luan-arita/game-of-life/assets/35427506/42296ea4-e11e-44b0-bc3a-cad9e7a83a3a" width = "600">

  Features other cellular automata:

  ### Langton's Ant:

The ant moves according to these rules:

1. At a white square, turn 90° clockwise, flip the color of the square and move forward one unit.
2. At a black square, turn 90° counter-clockwise, flip the color of the square and move forward one unit.

The ant starts out by creating simple patterns which are often symmetric. After a few hundred moves, it starts moving in irregular patterns and it traces a pseudo-random path until around 10,000 steps. The ant ends up finding order amidst the chaos, and starts building a "highway pattern" which repeats indefinitely.

<img src = "https://github.com/luan-arita/game-of-life/assets/35427506/411d1051-de01-4301-9b70-b50af10b665a" width = "600">

 ### Brian's Brain: 

It adds a third "dying" state. All cells that were alive go into the dying state, and cells that were already in the dying state goes into the dead state. By setting a third color to this new state, new patterns can be watched.

<img src = "https://github.com/luan-arita/game-of-life/assets/35427506/4a231cb9-2b0b-4a2d-a2bd-a873da8ebd18" width = "600">


### Rock Paper Scissors automaton

Every cell picks a random neighbor, they both play RPS and the loser takes the winner's color. Credits to [luciopaiva](https://www.reddit.com/r/cellular_automata/comments/figqjt/rock_paper_scissors_automaton/) for the idea.

<img src = "https://github.com/luan-arita/game-of-life/assets/35427506/9bfe2a12-6f53-4a51-8683-2e5b6beb9d41" width = "600">


## Contact

[Luan Arita](https://www.linkedin.com/in/luan-arita-319870262/) - luan.arita@unesp.br

## Acknowledgements
* [Robert Heaton](https://robertheaton.com/2018/07/20/project-2-game-of-life/) for guiding on how to make this project.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/luan-arita/game-of-life/blob/main/LICENSE) file for details

  
