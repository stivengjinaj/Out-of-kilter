# Out-of-kilter algorithm

The out-of-kilter algorithm is a primal-dual algorithm. It adjusts edges working on the primal problem and the nodes working on the dual problem in order to find a feasible solution, and then to optimize the problem.

# Algorithm
algorithm out-of-kilter\
begin\
&nbsp;&nbsp;&nbsp; Let π = 0 and x an a feasible flow;\
&nbsp;&nbsp;&nbsp; Calculate G(x) and kilter number k_ij for each edge (i, j);\
&nbsp;&nbsp;&nbsp; while G(x) contains an edge (p, q) out-of-kilter do\
&nbsp;&nbsp;&nbsp;&nbsp; begin\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Define the cost of each edge (i, j) in G(x) like $c'_{ij}$ = max{$0, c_{ij}^π$ };\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Calculate in G(x) − {(q, p)} the minimum distances from q to all the other nodes compared to costs c'_{ij};\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Let P be the path if minimum cost from q to p; Update π′ = π − d;\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if c_pq{π}′ < 0 then\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; W = P ∪ {(p, q)};\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Calculate δ = min{rij : (i, j) ∈ W};\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Increment of δ unity the flow in the cycle W;\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Update x, G(x), reduced costs c_{ij}^π and kilter numbers k_ij;\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; end if\
&nbsp;&nbsp;&nbsp;&nbsp;end\
end

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
