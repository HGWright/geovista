import geovista as gv
from geovista.pantry import lam
import geovista.theme

# load the sample data
sample = lam()

# create the mesh from the sample data
mesh = gv.Transform.from_unstructured(
    sample.lons,
    sample.lats,
    sample.connectivity,
    data=sample.data,
    start_index=sample.start_index,
)

# plot the mesh
plotter = gv.GeoPlotter()
sargs = dict(title=f"{sample.name} / {sample.units}")
plotter.add_mesh(mesh, cmap="balance", show_edges=False, scalar_bar_args=sargs)
plotter.add_base_layer(texture=gv.natural_earth_hypsometric())
resolution = "10m"
plotter.add_coastlines(resolution=resolution, color="white")
plotter.add_axes()
plotter.view_yz(negative=True)
plotter.add_text(
    f"CF UGRID LAM ({resolution} Coastlines)",
    position="upper_left",
    font_size=10,
    shadow=True,
)
plotter.show()
