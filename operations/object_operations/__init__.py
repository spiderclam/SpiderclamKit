from . import reset_transform
from . import make_org_bones

modules = [
    reset_transform,
    make_org_bones
]

def register():
    for module in modules:
        module.register()

def unregister():
    for module in modules:
        module.unregister()

if __name__ == "__main__":
    register()
