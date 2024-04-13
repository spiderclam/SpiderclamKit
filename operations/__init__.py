from . import object_operations
from . import constraint_operations

modules = [
    object_operations,
    constraint_operations
]


def register():
    for module in modules:
        module.register()


def unregister():
    for module in modules:
        module.unregister()


if __name__ == "__main__":
    register()
