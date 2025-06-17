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

from bpy.types import Panel
from bl_ui.utils import PresetPanel

#from . import Functions
#from .Functions import ###

####################################################################################
###################################### PANELS ######################################
####################################################################################

###############
### PRESETS ###
class GHISTEMPLATEADDON_MT_Template_Presets(bpy.types.Menu):
    bl_label = 'Ghis Template Addon Presets'
    preset_subdir = 'operator/ghistemplateaddon'
    preset_operator = 'script.execute_preset'
    draw = bpy.types.Menu.draw_preset

class GHISTEMPLATEADDON_PT_Template_Preset(PresetPanel, bpy.types.Panel):
    bl_label = 'Ghis Template Addon Presets'
    preset_subdir = 'operator/ghistemplateaddon'
    preset_operator = 'script.execute_preset'
    preset_add_operator = 'ghistemplateaddon.template_addpreset'

############
### LIST ###
class GHISTEMPLATEADDON_UL_List(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        settings = context.scene.TemplateAddonSettings
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            if item.name:
                layout.prop(item, "name", text="", emboss=False, icon="DOT")
            else:
                layout.label(text="", translate=False, icon="ERROR")
        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            layout.label(text="", icon="ANIM_DATA")

############
### MAIN ###
class GHISTEMPLATEADDON_PT_MainPanel(Panel):
    ''' '''
    bl_idname = "GHISTEMPLATEADDON_PT_mainpanel"
    bl_label = "Template Addon"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Template Addon"
    bl_order = 0

    #bl_options = {'DEFAULT_CLOSED'}

    def draw_header_preset(self, _context):
        GHISTEMPLATEADDON_PT_Template_Preset.draw_panel_header(self.layout)

    def draw(self, context):
        layout = self.layout

class GHISTEMPLATEADDON_PT_Panel(Panel):
    ''' '''
    bl_idname = "GHISTEMPLATEADDON_PT_firstpanel"
    bl_parent_id = "GHISTEMPLATEADDON_PT_mainpanel" # child of main panel
    bl_label = "Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Template Addon"
    bl_order = 0
    
    #bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        # get settings
        settings = context.scene.TemplateAddonSettings
        
        row = layout.row()
        row.template_list("GHISTEMPLATEADDON_UL_List", "", settings, "items", settings, "items_selected_index", rows=5)

        col = row.column(align=True)
        col.operator("ghistemplateaddon.list_new_item", text="", icon="ADD")
        col.operator("ghistemplateaddon.list_delete_item", text="", icon="REMOVE")

        col.separator()

        sub_col = col.column(align=True)
        sub_col.operator("ghistemplateaddon.list_move_item", text="", icon="TRIA_UP").direction = "UP"
        sub_col.enabled = len(settings.items) > 1 and settings.items_selected_index > 0

        sub_col = col.column(align=True)
        sub_col.operator("ghistemplateaddon.list_move_item", text="", icon="TRIA_DOWN").direction = "DOWN"
        sub_col.enabled = len(settings.items) > 1 and settings.items_selected_index < (len(settings.items) - 1)

        try:
            item = settings.items[settings.items_selected_index]
            row = layout.row()
            row.prop(item, "item_int_setting")
        except:
            pass

        row = layout.row()
        row.scale_y = 1.5
        row.operator("templateaddon.firstmodule_firstoperator")

class GHISTEMPLATEADDON_PT_SubPanel(Panel):
    ''' Tag-related settings & operators '''
    bl_idname = "GHISTEMPLATEADDON_PT_subpanel"
    bl_parent_id = "GHISTEMPLATEADDON_PT_firstpanel"
    bl_label = "SubPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Template Addon"
    bl_order = 1
    
    #bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return True # some condition to show the panel

    def draw_header(self, context):
        layout = self.layout
        scene = context.scene
        settings = scene.TemplateAddonSettings

        layout.prop(settings, "bool_setting", text="")

    def draw(self, context):
        layout = self.layout

        # get settings
        settings = context.scene.TemplateAddonSettings

        # gray out whole sub panel if header setting is off
        layout.enabled = settings.bool_setting

        row = layout.row()
        row.prop(settings, "int_setting")

        row = layout.row()
        row.prop(settings, "float_setting")

        # add some space
        layout.separator(factor=1.0, type='AUTO')

        row = layout.row()
        row.prop(settings, "enum_setting")