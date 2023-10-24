# Out-of-kilter algorithm

The out-of-kilter algorithm is a primal-dual algorithm. It adjusts edges working on the primal problem and the nodes working on the dual problem in order to find a feasible solution, and then to optimize the problem.

# Algorithm
The mathematical procedure followed by this algorithm is the same as the one in the following video: https://www.youtube.com/watch?v=CgJhTJkDhwk&pp=ygUXb3V0IG9mIGtpbHRlciBhbGdvcml0aG0%3D
```latex
algorithm out-of-kilter
begin
  Let π = 0 and x an a feasible flow;
  Calculate G(x) and kilter number k_{ij} for each edge (i, j);
  while G(x) contains an edge (p, q) out-of-kilter do
  begin
    Define the cost of each edge (i, j) in G(x) like c′ij = max{0, c_{ij}^π };
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

Python required: https://www.python.org/downloads/ . 

**WINDOWS users**

Don't forget to add it on PATH.

**IMPORTANT**

If **pip** is not installed, run these commands (python required) :
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python get-pip.py
```

**WINDOWS users**

Add pip to PATH 

Run this command to install the requirements:

```bash
pip install -r requirements.txt
```


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

The program starts by taking a **_.txt_** file that contains the information about the graph to be solved.
Be careful to input the data the correct way in the **_.txt_** file. There are 2 **_.txt_** files in the project: **graph.txt** and **graph2.txt**. In the current configuration, the algorithm solves the graph in **graph2.txt** file. To change the graph file just change the input file name in file **create_graph.py**
```python
def create_graph():

    with open("graph2.txt", 'r') as file:
        lines = file.readlines()
```

The data in the **.txt** file is organized as follows: **source, destination, lowerBound, upperBound, cost**. When the problem doesn't provide a **lowerBound** (minimum capacity), assign it to 0.

**IMPORTANT:** Note that the last line of the .txt file contains an edge that goes from the last node (destination) to the first node (source). **_This edge must be always added_**. In this edge the lowerBound and upperBound are equal to the flow starting from the source node, while the cost is 0. In the example below the data is written as follows: 6 1 4 4 0

The graph solved in the example:

![Example](https://github.com/stivengjinaj/Out-of-kilter/blob/master/solved%20example.png)

When you run the program, all the iterations with kilter numbers, flows and reduced costs will be printed in terminal. 

**_NOTE:_** The program plots the graphs in order to understand better the solution. If you run the program on terminal, a window containing the initial graph will open. If you close this window, you will be able to see the graph of the solution.

The initial graph plotted by the program:

![Initial graph](https://github.com/stivengjinaj/Out-of-kilter/blob/master/initial_graph.png)

The final graph plotted by the solution of the program:

![Final graph](https://github.com/stivengjinaj/Out-of-kilter/blob/master/final_graph.png)

**_NOTE:_** There is a section in **main.py** that is commented. If you de-comment it you will get plot of the graph in each iteration of the algorithm until reaching the solution

```python
    # Uncomment to see all steps plotted
    # iteration_graph = update_plot(flow)
    # plot_graph(iteration_graph, "ITERATION: " + str(iterations) + " GRAPH (capacity, flow)\n", "Associated cost: " + str(np.sum(cost * flow)))
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
