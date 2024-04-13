import bpy

class SpiderRig_PT_rigui(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Item'
    bl_label = "Rig UI"
    bl_idname = "SpiderRig_PT_rigui"


### Check if the selected rig has the corresponding RigID
    @classmethod
    def poll(cls, context):
        if context.active_object.type != 'ARMATURE':
            return False

        return cls.has_rows(context)

    @classmethod
    def has_rows(cls, context):
        collections = bpy.data.armatures.get(context.active_object.data.name).collections

        if collections:
            for collection in collections:
                if "row" in collection:
                    return True

        return False

    def draw(self, context):
        layout = self.layout
        collections = bpy.data.armatures[context.active_object.data.name].collections
        grouped_collections = {}

        for collection in collections:
            if "row" in collection:                
                row_value = collection["row"]

                if row_value not in grouped_collections:
                    grouped_collections[row_value] = []
                grouped_collections[row_value].append(collection)
                
        if not grouped_collections:
            return
                
        col = layout.column()
        col.label(text="Rig controls for: " + context.active_object.data.name)

        for row_value, items in grouped_collections.items():
            row = col.row(align=True)
            for item in items:
                row.prop(item, 'is_visible', toggle=True, text=item.name)
        
classes = (SpiderRig_PT_rigui,)

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()
 