# Kombinierend (kartesisches Produkt)

$$
R \times S
$$
```python
from Scripts.Joins.Cartesian import CartesianJoin

header_R = [
    'A', 'B'
]

header_S = [
    'B', 'C', 'D'
]

data_R = [
    [1, 2],
    [3, 4]
]
data_S = [
    [2, 5, 6],
    [4, 7, 8],
    [9, 10, 11]
]

cartesian_join = CartesianJoin(header_R, header_S, 'R', 'S')
new_header, new_data = cartesian_join.join(data_R, data_S, True)
```

# Natural Join
$$
\bowtie
$$
```python
from Scripts.Joins.NaturalJoin import NaturalJoin

header_a = ['A', 'B', 'C', 'D']
header_b = ['B', 'D', 'E']

natural_join = NaturalJoin(header_a, header_b)

data_a = [
    ['A', 1, 'A', 'a'],
    ['B', 2, 'Y', 'a'],
    ['Y', 4, 'B', 'b'],
    ['A', 1, 'Y', 'a'],
    ['S', 2, 'B', 'b']]

data_b = [
    [1, 'a', 'A'],
    [1, 'a', 'B']
]

new_attributes, new_table = natural_join.join(data_a, data_b, True)
```

## Nachteile
- **Voraussetzung**: Gemeinsame Attribute (d.h. Gleiche Bezeichnung, gleiche Domäne, gleiche Bedeutung). Das ist bei realen Datenbanken oft nicht gegeben.
- **Join-Kriterium:** Übereinstimmung (Gleichheit) in allen Attributwerten der gemeinsamen Attribute
- Nur ein Test auf **Gleichheit** möglich

# Theta-Join
$$
\bowtie_p
$$
```python
from Scripts.Joins.Theta import ThetaJoin

header_a = ['A', 'B', 'C', ]
header_b = ['B', 'C', 'D']

theta = ThetaJoin(header_a, header_b, 'R', 'S')

data_a = [
    [1,2,3],
    [6,7,8],
    [9,7,8]
]

data_b = [
    [2,5,6],
    [2,3,5],
    [7,8,10]
]

query = "(A < D) and (R.B is not S.B)"

new_headers, new_data = theta.join(data_a, data_b, query, True)
```



# Left Outer Join
```python
from Scripts.Joins.LeftOuterJoin import LeftOuterJoin

header_R = [
    'A', 'B', 'C'
]

header_S = [
    'C', 'D', 'E'
]

data_R = [
    ['a1', 'b1', 'c1'],
    ['a2', 'b2', 'c2']
]
data_S = [
    ['c1', 'd1', 'e1'],
    ['c3', 'd2', 'e2']
]

left_outer = LeftOuterJoin(header_R, header_S)
left_outer.set_bag(False)
new_header, new_data = left_outer.join(data_R, data_S, True)
```

# Right Outer Join

```python
from Scripts.Joins.RightOuterJoin import RightOuterJoin

header_R = [
    'A', 'B', 'C'
]

header_S = [
    'C', 'D', 'E'
]

data_R = [
    ['a1', 'b1', 'c1'],
    ['a2', 'b2', 'c2']
]
data_S = [
    ['c1', 'd1', 'e1'],
    ['c3', 'd2', 'e2']
]

right_outer = RightOuterJoin(header_R, header_S)
right_outer.set_bag(False)
new_header, new_data = right_outer.join(data_R, data_S, True)
```

# Full Outer Join

```python
from Scripts.Joins.FullOuterJoin import FullOuterJoin

header_R = [
    'A', 'B', 'C'
]

header_S = [
    'C', 'D', 'E'
]

data_R = [
    ['a1', 'b1', 'c1'],
    ['a2', 'b2', 'c2']
]
data_S = [
    ['c1', 'd1', 'e1'],
    ['c3', 'd2', 'e2']
]

full_outer = FullOuterJoin(header_R, header_S)
new_header, new_data = full_outer.join(data_R, data_S, True)
```

