bl_info = {
    "name" : "SpiderclamKit",
    "author" : "RWOverdijk",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Rigging"
}

from . import operations
from . import ui

modules = [
    operations,
    ui
]

def register():
    for module in modules:
        module.register()

def unregister():
    for module in modules:
        module.unregister()

if __name__ == "__main__":
    register()
