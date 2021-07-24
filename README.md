# Kanizsa_illusion

A Python library for simply generating Kanizsa illusion graphics (triangles and rectangles).

# Installation
### Install from source
```
git clone http://git.thbi.cc/yinzi/Kanizsa_illusion.git
cd Kanizsa_illusion/
pip install ./
```
### Install from PyPi
```
pip install kanizsa
```

# Get Started
```python
# Import the class
from kanizsa import Kanizsa
# Instantiate
kani = Kanizsa()
# Change default parameters
kani.update(distance=10)
# Draw a kanizsa triangle
kani.draw()
```
<div align="center">
  <img src="https://i.loli.net/2021/07/24/Tn6JdFItpYcwqoC.png" alt="Kanizsa triangle(all circles)" />
</div>

```python
# Draw a kanizsa triangle with the control circles
kani.draw(all_circles=True)
```
<div align="center">
  <img src="https://i.loli.net/2021/07/24/J2OgjPUQrl7vk1Z.png" alt="Kanizsa triangle(all circles)" />
</div>

```python
kani.update(polygon='rectangle')
# Draw a kanizsa rectangle
kani.draw(all_circles=False)
```
<div align="center">
  <img src="https://i.loli.net/2021/07/24/JVeEGuLlpktmOaj.png" alt="Kanizsa rectangle" />
</div>

# Animation (*ffmpeg needed*)
```python
# Import the class
from kanizsa import Kanizsa
import numpy as np
# Instantiate
kani = Kanizsa()
# kanizsa triangle Animating: changing the distance of circle_set from 1 to 100, step 1
ani = kani.animate(frames=np.linspace(1, 100, 100), interval=50, repeat_delay=1000, plot=False)
# save as video
ani.save('kani_triangle.mp4') 
# save as gif
ani.save('kani_triangle.gif') 
# kanizsa triangle Animating: changing the distance of circle_set from 1 to 100, step 1
kani.update(polygon='rectangle')
# kanizsa Rectangle Animating: changing the distance of circle_set from 1 to 100, step 1
ani2 = kani.animate(frames=np.linspace(1, 100, 100), interval=50, repeat_delay=1000, plot=False)
# save as video
ani2.save('kani_rectangle.mp4') 
# save as gif
ani2.save('kani_rectangle.gif') 
```

<div align="center">
  <img src="https://i.loli.net/2021/07/24/JHsFRtBm6XwnD1e.gif" alt="Kanizsa package examples1" />
  <img src="https://i.loli.net/2021/07/24/zC8pXhAu9ayYxtm.gif" alt="Kanizsa package examples2" />
</div>
