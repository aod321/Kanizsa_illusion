import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import animation
from typing import List, Tuple, Union, Optional
from typeguard import typechecked


class Kanizsa:
    def __init__(self,
                 width=224, height=224,
                 center=(112, 112), radius=10, distance=1, polygon='triangle',
                 pad_face_color="white",
                 circle_color="black",
                 circle_edge_color=None,
                 all_circles=False,
                 polygon_rgba=(1, 1, 1, 1)
                 ):
        self.width = width
        self.height = height
        self.center = center
        self.radius = radius
        self.distance = distance
        self.polygon = polygon
        self.polygon_rgba = polygon_rgba
        self.face_color = pad_face_color
        self.circle_color = circle_color
        self.circle_edge_color = circle_edge_color
        self.cen_xy = None
        self.circle_patches = None
        self.polygon_patches = None
        self.all_circles = all_circles

    @staticmethod
    def _get_circle_set(center=(112, 112), radius=10, distance=1, face_color='black', edge_color=None):
        circle_patches = []
        cen_xy = np.zeros((3, 3, 2))
        bound_width = 2 * radius + distance
        for i, iy in enumerate([bound_width, 0, -bound_width]):
            for j, ix in enumerate([-bound_width, 0, bound_width]):
                cen_xy[i, j] = (center[0] + ix, center[1] + iy)
                circle_patches.append(mpatches.Circle(cen_xy[i, j],
                                                      radius=radius, facecolor=face_color,
                                                      edgecolor=edge_color)
                                      )
        return cen_xy, circle_patches

    @staticmethod
    def _get_polygon(circles_cen_xy, polygon='triangle', rgba=(1, 1, 1, 1)):
        xy = None
        if polygon == 'triangle':
            xy = [circles_cen_xy[0, 1], circles_cen_xy[2, 0], circles_cen_xy[2, 2]]
        elif polygon == 'rectangle':
            xy = [circles_cen_xy[0, 0], circles_cen_xy[0, 2], circles_cen_xy[2, 2], circles_cen_xy[2, 0]]
        if not xy:
            raise RuntimeError("Error Polygon type, please input 'triangle' or 'rectangle' ")
        return mpatches.Polygon(xy, color=rgba)

    def draw(self, face_color=None, all_circles=-1, plot=True, show_axis=True):
        if face_color is not None:
            self.face_color = face_color
        if all_circles != -1:
            self.all_circles = all_circles
        fig, ax = plt.subplots()
        ax.set_facecolor(self.face_color)
        ax.axis([0, self.width, 0, self.height])
        ax.set_aspect("equal")
        self.cen_xy, self.circle_patches = self._get_circle_set(center=self.center, radius=self.radius,
                                                                distance=self.distance, face_color=self.circle_color,
                                                                edge_color=self.circle_edge_color
                                                                )
        self.polygon_patches = self._get_polygon(self.cen_xy, polygon=self.polygon, rgba=self.polygon_rgba)
        show_range = range(len(self.circle_patches))
        if not self.all_circles:
            if self.polygon == 'triangle':
                # only show 3 circles
                show_range = [1, 6, 8]
            elif self.polygon == 'rectangle':
                # only show 4 circles
                show_range = [0, 2, 6, 8]
        # start drawing
        for i in show_range:
            ax.add_patch(self.circle_patches[i])
        ax.add_patch(self.polygon_patches)
        if plot:
            if not show_axis:
                plt.xticks([])
                plt.yticks([])
            plt.show()
        return fig, ax

    @typechecked
    def update(self,
               distance: Optional[Union[int, float]] = None,
               radius: Optional[Union[int, float]] = None,
               width: Optional[Union[int, float]] = None,
               height: Optional[Union[int, float]] = None,
               center: Optional[Union[List[int], Tuple[int], List[float], Tuple[float]]] = None,
               polygon: Optional[str] = None,
               face_color: Optional[str] = None,
               circle_color: Optional[str] = None,
               circle_edge_color: Optional[str] = None,
               polygon_rgba: Optional[Union[List[int], Tuple[int], List[float], Tuple[float]]] = None,
               all_circles: Union[int, bool] = -1
               ):
        if all_circles != -1:
            self.all_circles = all_circles
        if face_color is not None:
            self.face_color = face_color
        if distance is not None:
            self.distance = distance
        if radius is not None:
            self.radius = radius
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if center is not None:
            self.center = center
        if polygon is not None:
            self.polygon = polygon
        if circle_color is not None:
            self.circle_color = circle_color
        if circle_edge_color is not None:
            self.circle_edge_color = circle_edge_color
        if polygon_rgba is not None:
            self.polygon_rgba = polygon_rgba
        if self.circle_patches:
            cen_xy, _ = self._get_circle_set(center=self.center, radius=self.radius, distance=self.distance)
            for i in range(len(self.circle_patches)):
                self.circle_patches[i].center = cen_xy.reshape(-1, 2)[i]
            polygon_patches = self._get_polygon(circles_cen_xy=cen_xy, polygon=self.polygon, rgba=self.polygon_rgba)
            self.polygon_patches.xy = polygon_patches.xy

    def animate(self, frames=np.linspace(1, 100, 100), interval=50, repeat_delay=1000, plot=False):
        fig, ax = self.draw(face_color=self.face_color, all_circles=self.all_circles, plot=plot)
        ani = animation.FuncAnimation(fig, self.update, frames=frames,
                                      interval=interval, repeat_delay=repeat_delay)
        return ani


if __name__ == '__main__':
    a = Kanizsa()
    a.draw(all_circles=True)
    a.draw(all_circles=False)
