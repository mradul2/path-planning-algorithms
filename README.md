# Global Path Planning Algoritms

Analysis of Path Finding Algorithms based on their cost and time taken.

## Usage

```bash
git clone https://github.com/mradul2/path-planning-algorithms.git
python3 algorithm.py
```

### Available Algorithms

- AstarAdmissible
- AstarAdmissible2
- AstarDiagonal
- AstarDiagonal2
- AstarEuclidean
- AstarEuclidean2
- AstarManhattan
- AstarManhattan2
- AstarNonAdmissible
- AstarNonAdmissible2
- Dijkstra
- Dijkstra2

## Results

Cost of the Path found by the respective algorithms (1 pixel = 1 unit)

![graph1](assets/graph1.png)

Execution Time taken by each of the algorithm (In seconds)

![graph2](assets/graph2.png)

### Analysis

![analysis](assets/ana.png)

### Outputs

#### Dijkstra.py

<img src="assets/1.png" alt="1" width="450"/>

#### Dijkstra2.py

<img src="assets/2.png" alt="2" width="450"/>

#### AstarAdmissible.py

<img src="assets/3.png" alt="3" width="450"/>

#### AstarAdmissible2.py

<img src="assets/4.png" alt="4" width="450"/>

#### AstarNonAdmissible.py

<img src="assets/5.png" alt="5" width="450"/>

#### AstarNonAdmissible2.py

<img src="assets/6.png" alt="6" width="450"/>

#### AstarDiagonal.py

<img src="assets/7.png" alt="7" width="450"/>

#### AstarDiagonal2.py

<img src="assets/8.png" alt="8" width="450"/>

#### AstarManhattan.py

<img src="assets/9.png" alt="9" width="450"/>

#### AstarManhattan2.py

<img src="assets/10.png" alt="10" width="450"/>

#### AstarEuclidean.py

<img src="assets/11.png" alt="11" width="450"/>

#### AstarEuclidean2.py

<img src="assets/12.png" alt="12" width="450"/>

### Color code

| Node       | Colour |
|------------|--------|
| FINAL PATH | Blue   |
| CLOSED     | Orange |
| OPEN       | Gray   |
| OBSTACLE   | White  |
| MOVABLE    | Black  |
| START      | Green  |
| END        | Red    |

## About

`node.py` file contains a `Node` class along with functions for Constructing Path, Generating Neighbours of a Node, Checking for a valid Node, Calculating heuristic with different heuristic functions.

With the help of `Node` class, A matrix similar to the given image is created with elements as Nodes. And then a further appropriate algorithm is applied to these Nodes containing matrices. Which is finally translated into the given Image for demonstration. 

`utils.py` is a utility file with some Global constants including the given Image and some utility functions such as upScale used for upscaling the given Image.

There are 12 different algorithm files which on running in the terminal will give the Final Image containing `Path`, `Open Nodes`, `Closed Nodes` and `Unvisited Nodes` along with the time taken by the algorithm and cost of the path.
