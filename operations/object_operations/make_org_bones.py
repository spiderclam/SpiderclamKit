import bpy

class MakeOrgBones(bpy.types.Operator):
    bl_idname = "sc.oo_make_org_bones"
    bl_label = "Make ORG bones"
    bl_description = "Make ORG bones"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.mode == 'EDIT_ARMATURE'


    def execute(self, context):
        armature = bpy.context.object
        collections = armature.data.collections
        collection_org = collections.get("ORG")
        collection_def = collections.get("DEF")
        selected_bones_original_order = []

        for bone in context.selected_bones:
            if not bone.name.startswith("DEF_"):
                self.report({'ERROR'}, "All selected bones must have the prefix 'DEF_'")
                return {'CANCELLED'}
            selected_bones_original_order.append(bone)

        bpy.ops.armature.duplicate()

        # Make sure ORG collection exists
        if not collection_org:
            collection_org = collections.new(name='ORG')

        bpy.ops.object.mode_set(mode='POSE')

        for original_bone, duplicated_bone in zip(selected_bones_original_order, context.selected_pose_bones):
            duplicated_bone.name = original_bone.name.replace("DEF_", "ORG_")
            constraint = armature.pose.bones.get(original_bone.name).constraints.new(type='COPY_TRANSFORMS')

            constraint.target = armature
            constraint.subtarget = duplicated_bone.name

            collection_org.assign(duplicated_bone)

            if collection_def:
              collection_def.unassign(bone=duplicated_bone)

        self.report({'INFO'}, "ORG bones successfully created")

        bpy.ops.object.mode_set(mode='EDIT')

        return {'FINISHED'}


classes = [
    MakeOrgBones
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
