import bpy

class ResetTransform(bpy.types.Operator):
    bl_idname = "sc.oo_reset_transform"
    bl_label = "Reset transform For Selection"
    bl_description = "Resets scale, rotation and location on all selected."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        selected_bones = context.selected_pose_bones
        if not selected_bones:
            self.report({'INFO'}, "No bones selected")
            return {'CANCELLED'}

        # Reset scale, rotation, and location for each bone
        for bone in selected_bones:
            bone.scale = (1, 1, 1)
            bone.rotation_euler = (0, 0, 0)
            bone.location = (0, 0, 0)

        self.report({'INFO'}, "Transforms reset for selected bones")
        return {'FINISHED'}


classes = [
    ResetTransform
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
