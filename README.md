# Out-of-kilter algorithm

The out-of-kilter algorithm is a primal-dual algorithm. It adjusts edges working on the primal problem and the nodes working on the dual problem in order to find a feasible solution and then to optimize the problem.

## Algorithm

The algorithm can be expressed in a more readable form using MathJax formatting:

```markdown
1. Let \( \pi = 0 \) and \( x \) be a feasible flow;
2. Calculate \( G(x) \) and kilter number \( k_{ij} \) for each edge \( (i, j) \);
3. while \( G(x) \) contains an edge \( (p, q) \) out-of-kilter do:
   - Define the cost of each edge \( (i, j) \) in \( G(x) \) as \( c'_{ij} = \max(0, c_{ij}^\pi) \);
   - Calculate in \( G(x) - \{(q, p)\} \) the minimum distances from \( q \) to all other nodes compared to costs \( c'_{ij} \);
   - Let \( P \) be the path of minimum cost from \( q \) to \( p \). Update \( \pi' = \pi - d \);
   - if \( c'_{pq}^\pi < 0 \) then:
     - \( W = P \cup \{(p, q)\} \);
     - Calculate \( \delta = \min\{r_{ij} : (i, j) \in W\} \);
     - Increment \( \delta \) in the flow in the cycle \( W \);
     - Update \( x \), \( G(x) \), reduced costs \( c_{ij}^\pi \), and kilter numbers \( k_{ij} \).

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
