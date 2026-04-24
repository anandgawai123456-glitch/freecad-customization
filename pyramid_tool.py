import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument("Pyramid")

# Base points
v1 = App.Vector(0, 0, 0)
v2 = App.Vector(50, 0, 0)
v3 = App.Vector(50, 50, 0)
v4 = App.Vector(0, 50, 0)
top = App.Vector(25, 25, 100)

# Faces
faces = [
    Part.Face(Part.makePolygon([v1, v2, top, v1])),
    Part.Face(Part.makePolygon([v2, v3, top, v2])),
    Part.Face(Part.makePolygon([v3, v4, top, v3])),
    Part.Face(Part.makePolygon([v4, v1, top, v4])),
    Part.Face(Part.makePolygon([v1, v2, v3, v4, v1]))
]

shell = Part.makeShell(faces)
solid = Part.makeSolid(shell)

Part.show(solid)