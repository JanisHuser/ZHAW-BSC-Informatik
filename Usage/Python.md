# Python

Im [Mdbook](https://summary.ateastar.ddns.net) kann Python Code getestet werden.
Zusätzlich gibt es Snippets, welche das Plugin benutzen.

## Module
- Numpy
- Matplotlib


## Verwendung

Die folgende Blockstruktur kann verwendet werden, um Python Code einzufügen.

	```python,editable
	import numpy as np

	print (np.array([1,2,3]))
	```

```python,editable
import numpy as np

print (np.array([1,2,3]))
```


## Matplotlib

Bilder im print ("img="+base64) werden als Bild ausgegeben.

```python
print ("img=" +base64.b64encode(buf.read()).decode('UTF-8'))
```


```python,editable
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np
import io, base64

# First create the x and y coordinates of the points.
n_angles = 36
n_radii = 8
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles

x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
z = (np.cos(radii) * np.cos(3 * angles)).flatten()

# Create the Triangulation; no triangles so Delaunay triangulation created.
triang = tri.Triangulation(x, y)

# Mask off unwanted triangles.
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)

fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tpc = ax1.tripcolor(triang, z, shading='flat')
fig1.colorbar(tpc)
ax1.set_title('tripcolor of Delaunay triangulation, flat shading')

buf = io.BytesIO()
fig1.savefig(buf, format='png')
buf.seek(0)

print ("img=" +base64.b64encode(buf.read()).decode('UTF-8'))
```