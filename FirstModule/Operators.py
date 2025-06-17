# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy

from bpy.types import Operator
from bl_operators.presets import AddPresetBase

from . import Functions
from .Functions import first_function

#######################################################################################
###################################### OPERATORS ######################################
#######################################################################################

##############
### PRESET ###
class GHISTEMPLATEADDON_OT_Template_AddPreset(AddPresetBase, bpy.types.Operator):
    bl_idname = 'ghistemplateaddon.template_addpreset'
    bl_label = 'Add preset'
    preset_menu = 'GHISTEMPLATEADDON_MT_Template_Presets'

    preset_defines = [ 'settings = bpy.context.scene.TemplateAddonSettings' ]

    preset_values = [
        'settings.items',
        'settings.items_selected_index',
        'settings.int_setting',
        'settings.bool_setting',
        'settings.str_setting',
        'settings.enum_setting',
        'settings.float_setting',
    ]

    preset_subdir = 'operator/ghistemplateaddon'

############
### LIST ###
class GHISTEMPLATEADDON_OT_List_NewItem(bpy.types.Operator):
    """Add a new item to the list."""
    bl_idname = "ghistemplateaddon.list_new_item"
    bl_label = "Add a new item"

    @classmethod
    def poll(cls, context):
        settings = context.scene.TemplateAddonSettings
        return len(settings.items) < 10 # limit to 10?

    def execute(self, context):
        settings = context.scene.TemplateAddonSettings

        settings.items.add()
        last_index = len(settings.items) - 1
        if last_index >= 0:
            settings.items_selected_index = last_index # update selected index

            new_item = settings.items[last_index]

            # assign unique name using .00X suffix
            name = "Item"
            name_suffix = 0
            names = [item.name for item in settings.items if new_item != item]
            while name in names:
                name_suffix += 1
                name_suffix_str = str(name_suffix).zfill(3)
                name = "Item." + name_suffix_str
            new_item.name = name
            new_item.item_int_setting = 0

            return{'FINISHED'}
        else:
            return {'CANCELLED'}

class GHISTEMPLATEADDON_OT_List_DeleteItem(bpy.types.Operator):
    """Delete the selected item from the list."""
    bl_idname = "ghistemplateaddon.list_delete_item"
    bl_label = "Deletes an item"

    @classmethod
    def poll(cls, context):
        settings = context.scene.TemplateAddonSettings
        try:
            return len(settings.items) > 0 # any item to delete?
        except:
            return False

    def execute(self, context):
        settings = context.scene.TemplateAddonSettings
        try:
            settings.items.remove(settings.items_selected_index)
            settings.items_selected_index = max(0, min(len(settings.items) - 1, settings.items_selected_index))

            return{'FINISHED'}
        except:
            return {'CANCELLED'}

class GHISTEMPLATEADDON_OT_List_MoveItem(bpy.types.Operator):
    """Move an item in the list."""
    bl_idname = "ghistemplateaddon.list_move_item"
    bl_label = "Move an item in the list"

    direction: bpy.props.EnumProperty(items=(
        ('UP', 'Up', ""),
        ('DOWN', 'Down', ""),
        ))

    @classmethod
    def poll(cls, context):
        settings = context.scene.TemplateAddonSettings
        try:
            return settings.items[settings.items_selected_index]
        except:
            return False

    def execute(self, context):
        settings = context.scene.TemplateAddonSettings
        try:
            index_offset = -1 if self.direction == 'UP' else 1
            settings.items.move(settings.items_selected_index + index_offset, settings.items_selected_index)
            settings.items_selected_index = max(0, min(settings.items_selected_index + index_offset, len(settings.items) - 1))
            return {'FINISHED'}
        except:
            return {'CANCELLED'}

############
### MAIN ###
class GHISTEMPLATEADDON_OT_FirstOperator(Operator):
    '''  '''
    bl_idname = "templateaddon.firstmodule_firstoperator"
    bl_label = "Do Something With Item"
    bl_category = "Template Addon"
    bl_description = ""
    
    @classmethod
    def poll(cls, context):
        settings = context.scene.TemplateAddonSettings
        try:
            return len(settings.items) > 0 # assume operation is performed on an item and so we need one. This is an example.
        except:
            return False


    def execute(self, context):
        # get settings
        settings = context.scene.TemplateAddonSettings

        success, msg = first_function(context, settings.int_setting)
        if success:
            self.report({'INFO'}, "Int is above 0. This is an example")
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, msg)
            return {'CANCELLED'}