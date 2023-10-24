# Out-of-kilter algorithm

The out-of-kilter algorithm is a primal-dual algorithm. It adjusts edges working on the primal problem and the nodes working on the dual problem in order to find a feasible solution and then to optimize the problem.

## Algorithm

The algorithm can be expressed in a more readable form using LaTeX-style math formatting:

```latex
\[
\begin{align*}
\text{Let } \pi &= 0 \text{ and } x \text{ be a feasible flow;} \\
\text{Calculate } G(x) \text{ and kilter number } k_{ij} \text{ for each edge } (i, j); \\
\text{while } G(x) \text{ contains an edge } (p, q) \text{ out-of-kilter do} \\
\begin{cases}
\text{Define the cost of each edge } (i, j) \text{ in } G(x) \text{ as } c'_{ij} = \max\{0, c_{ij}^\pi\}; \\
\text{Calculate in } G(x) - \{(q, p)\} \text{ the minimum distances from } q \text{ to all other nodes compared to costs } c'_{ij}; \\
\text{Let } P \text{ be the path of minimum cost from } q \text{ to } p; \text{ Update } \pi' = \pi - d; \\
\text{if } c'_{pq}^\pi < 0 \text{ then} \\
\begin{cases}
W = P \cup \{(p, q)\}; \\
\text{Calculate } \delta = \min\{r_{ij} : (i, j) \in W\}; \\
\text{Increment } \delta \text{ in the flow in the cycle } W; \\
\text{Update } x, G(x), \text{reduced costs } c_{ij}^\pi, \text{ and kilter numbers } k_{ij};
\end{cases}
\end{cases}
\end{cases}
\end{align*}
\]

```


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
