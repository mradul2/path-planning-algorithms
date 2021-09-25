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

![1](assets/1.png)

#### Dijkstra2.py

![2](assets/2.png)

#### AstarAdmissible.py

![3](assets/3.png)

#### AstarAdmissible2.py

![4](assets/4.png)

#### AstarNonAdmissible.py

![5](assets/5.png)

#### AstarNonAdmissible2.py

![6](assets/6.png)

#### AstarDiagonal.py

![7](assets/7.png)

#### AstarDiagonal2.py

![8](assets/8.png)

#### AstarManhattan.py

![9](assets/9.png)

#### AstarManhattan2.py

![10](assets/10.png)

#### AstarEuclidean.py

![11](assets/11.png)

#### AstarEuclidean2.py

![12](assets/12.png)

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
