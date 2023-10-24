# Out-of-kilter algorithm

The out-of-kilter algorithm is a primal-dual algorithm. It adjusts edges working on the primal problem and the nodes working on the dual problem in order to find a feasible solution, and then to optimize the problem.

# Algorithm
```latex
algorithm out-of-kilter
begin
  Let π = 0 and x an a feasible flow;
  Calculate G(x) and kilter number k_{ij} for each edge (i, j);
  while G(x) contains an edge (p, q) out-of-kilter do
  begin
    Define the cost of each edge (i, j) in G(x) like $ c′ij $ = max{0, c_{ij}^π };
    Calculate in G(x) − {(q, p)} the minimum distances from q to all the other nodes compared to
    costs c'_{ij};
    Let P be the path if minimum cost from q to p; Update π′ = π − d;
    if c_pq{π}′ < 0 then
      W = P ∪ {(p, q)};
      Calculate δ = min{rij : (i, j) ∈ W};
      Increment of δ unity the flow in the cycle W;
      Update x, G(x), reduced costs c_{ij}^π and kilter numbers k_ij;
    end if
  end
end
```
## Installation

Required only the installation of python: https://www.python.org/downloads/


## Usage

If the program is run from PyCharm or any other IDE, you have to run the main file, otherwise just use this terminal command (assuming Python is installed)

```bash
python3 main.py
```
or
```bash
python main.py
```

## Instructions

The program starts by taking a .txt file that contains the information about the graph to be solved.
Be careful to input the data the correct way in the .txt file. There are 2 .txt files in the project: graph.txt and graph2.txt. In the current configuration, the algorithm solves the graph in graph2.txt file. To change the graph file just change the input file name in file create_graph.py
```python
def create_graph():

    with open("graph2.txt", 'r') as file:
        lines = file.readlines()

....................................................
```

The data in the .txt file is organized as follows: source, destination, lowerBound, upperBound, cost. When the problem doesn't provide a lowerBound (minimum capacity), assign it to 0.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
