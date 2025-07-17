import bpy
settings = bpy.context.scene.TemplateAddonSettings

settings.items.clear()
item_sub_1 = settings.items.add()
item_sub_1.name = 'Item'
item_sub_1.name = 'Item'
item_sub_1.item_int_setting = 2
settings.items_selected_index = 0
settings.int_setting = 3
settings.bool_setting = True
settings.str_setting = '_Default String'
settings.enum_setting = 'B'
settings.float_setting = 0.9599999785423279
