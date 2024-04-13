import bpy

class RIG_PANEL_PT_Spiderclam_Pose_Kit(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Item'
    bl_label = "Rig UI"
    bl_idname = "RIG_PANEL_PT_Spiderclam_Pose_Kit"


    @classmethod
    def poll(cls, context):
        return (context.active_object.type == 'ARMATURE') and cls.has_rows(context)


    @classmethod
    def has_rows(cls, context):
        collections = bpy.data.armatures.get(context.active_object.data.name).collections

        return any("row" in collection for collection in collections)


    def draw(self, context):
        layout = self.layout
        collections = bpy.data.armatures[context.active_object.data.name].collections
        grouped_collections = {}

        for collection in collections:
            if "row" in collection:
                row_value = collection["row"]
                grouped_collections.setdefault(row_value, []).append(collection)
                
        if not grouped_collections:
            return
                
        col = layout.column()
        col.label(text="Rig controls for: " + context.active_object.data.name)

        for row_value, items in grouped_collections.items():
            row = col.row(align=True)
            for item in items:
                row.prop(item, 'is_visible', toggle=True, text=item.name)
          
classes = (RIG_PANEL_PT_Spiderclam_Pose_Kit,)

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()
