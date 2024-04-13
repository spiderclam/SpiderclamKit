import bpy

class SetDistanceBySelected(bpy.types.Operator):
    bl_idname = "sc.co_ldc_set_distance_by_selected"
    bl_label = "Set Distance For Selection"
    bl_description = "Applies total length of selected bones to active bone's Limit Distance constraint"
    bl_options = {"REGISTER", "UNDO"}

    include_active: bpy.props.BoolProperty(
        name="Include active",
        default=False,
        description="Include the length of the active bone",
    )

    def execute(self, context):
        # Get selected bones
        selected_bones = [bone for bone in context.selected_pose_bones]

        # Get active bone
        active_bone = context.active_pose_bone

        # Apply total length to active bone's Limit Distance constraint
        if selected_bones and active_bone:
            total_length = self.calculate_total_bone_length(selected_bones, active_bone)

            limit_distance_constraint = active_bone.constraints.get("Limit Distance")

            if limit_distance_constraint:
                limit_distance_constraint.distance = total_length
            self.report({'INFO'}, "Total length applied to active bone's Limit Distance constraint successfully.")
        else:
            self.report({'ERROR'}, "Please select bones and ensure an active bone is selected.")

        return {'FINISHED'}

    def calculate_total_bone_length(self, selected_bones, active_bone):
        total_length = 0.0

        # Calculate total length of selected bones
        for bone in selected_bones:
            if bone != active_bone or self.include_active:
                total_length += bone.length

        return total_length


classes = [
    SetDistanceBySelected
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
 