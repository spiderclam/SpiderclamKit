import bpy
from bpy.types import Menu


class POSE_MT_Spiderclam_Pose_Kit(Menu):
    bl_idname = "POSE_MT_Spiderclam_Pose_Kit"
    bl_label = "Fast Pose Tools"

    def draw(self, context):

        layout = self.layout

        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        
        pie.operator("sc.oo_reset_transform", icon="TRANSFORM_ORIGINS")
        pie.operator("sc.oo_extrude_bone_to_cursor", icon="CURSOR")
        pie.operator("sc.oo_add_bone_at_cursor", icon="PLUS")
        pie.operator("sc.oo_move_bone_to_cursor", icon="ORIENTATION_CURSOR")

        if context.object and context.object.mode == 'POSE':
            pie.operator("sc.co_ldc_set_distance_by_selected", icon="MOD_LENGTH")

        if context.object and context.object.mode.startswith('EDIT'):
            pie.operator("sc.oo_make_org_bones", icon="DUPLICATE")


global_addon_keymaps = []


def register():
    bpy.utils.register_class(POSE_MT_Spiderclam_Pose_Kit)

    window_manager = bpy.context.window_manager
    if window_manager.keyconfigs.addon:
        keymap = window_manager.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D', region_type='WINDOW')

        keymap_item = keymap.keymap_items.new('wm.call_menu_pie', "O", "PRESS", alt=True, shift=True)
        keymap_item.properties.name = "POSE_MT_Spiderclam_Pose_Kit"

        # save the key map to deregister later
        global_addon_keymaps.append((keymap, keymap_item))


def unregister():
    bpy.utils.unregister_class(POSE_MT_Spiderclam_Pose_Kit)

    window_manager = bpy.context.window_manager
    if window_manager and window_manager.keyconfigs and window_manager.keyconfigs.addon:

        for keymap, keymap_item in global_addon_keymaps:
            keymap.keymap_items.remove(keymap_item)

    global_addon_keymaps.clear()


if __name__ == "__main__":
    register()

    bpy.ops.wm.call_menu_pie(name="POSE_MT_Spiderclam_Pose_Kit")
