import bpy

def prepare_armature_state(context):
    armature = context.scene.last_active_armature

    # Store last active
    last_active = context.view_layer.objects.active

    # Store last mode
    last_mode = last_active.mode

    # Switch to object mode
    bpy.ops.object.mode_set(mode='OBJECT')

    context.view_layer.objects.active = armature

    bpy.ops.object.mode_set(mode='EDIT')

    return last_active, last_mode, armature

def restore_previous_state(last_active, last_mode):
    # Restore active object and mode
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.view_layer.objects.active = last_active
    bpy.ops.object.mode_set(mode=last_mode)


class ExtrudeBoneToCursor(bpy.types.Operator):
    bl_idname = "sc.oo_extrude_bone_to_cursor"
    bl_label = "Extrude bone to cursor"
    bl_description = "Extrude bone to cursor"
    bl_options = {"REGISTER", "UNDO"}
    
    @classmethod
    def poll(cls, context):
        return context.scene.last_active_armature

    def execute(self, context):
        last_active, last_mode, _ = prepare_armature_state(context)

        bpy.ops.armature.extrude_move(TRANSFORM_OT_translate={"value":(0, 0, 1)})

        # Now move the newly extruded bone to the cursor
        bpy.context.active_bone.tail = bpy.context.scene.cursor.location

        # Now put everything back where it was
        restore_previous_state(last_active, last_mode)

        return {'FINISHED'}
    

class AddBoneAtCursor(bpy.types.Operator):
    bl_idname = "sc.oo_add_bone_at_cursor"
    bl_label = "Add bone at cursor"
    bl_description = "Add bone at cursor"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.scene.last_active_armature

    def execute(self, context):        
        last_active, last_mode, armature = prepare_armature_state(context)

        bpy.ops.armature.bone_primitive_add()
        armature.data.edit_bones.active = armature.data.edit_bones[-1]

        # Now put everything back where it was
        restore_previous_state(last_active, last_mode)

        return {'FINISHED'}
    

class MoveBoneToCursor(bpy.types.Operator):
    bl_idname = "sc.oo_move_bone_to_cursor"
    bl_label = "Move bone to cursor"
    bl_description = "Move bone to cursor"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.scene.last_active_armature

    def execute(self, context):
        last_active, last_mode, _ = prepare_armature_state(context)

        bpy.context.active_bone.tail = bpy.context.scene.cursor.location

        # Now put everything back where it was
        restore_previous_state(last_active, last_mode)

        return {'FINISHED'}
    

def selection_changed_handler(scene):    
    if bpy.context.active_object and bpy.context.active_object.type == 'ARMATURE':
        bpy.context.scene.last_active_armature = bpy.context.active_object


classes = [
    ExtrudeBoneToCursor,
    AddBoneAtCursor,
    MoveBoneToCursor
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.last_active_armature = bpy.props.PointerProperty(type=bpy.types.Object)
    bpy.app.handlers.depsgraph_update_post.append(selection_changed_handler)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    if selection_changed_handler in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(selection_changed_handler)

    del bpy.types.Scene.last_active_armature


if __name__ == "__main__":
    register()
