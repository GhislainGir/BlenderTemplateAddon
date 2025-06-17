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

from bpy.props import PointerProperty, BoolProperty, FloatProperty, EnumProperty, StringProperty, IntProperty, CollectionProperty, FloatVectorProperty
from bpy.types import PropertyGroup

#############################################################################################
###################################### PROPERTY GROUPS ######################################
#############################################################################################
class  GHISTEMPLATEADDON_PG_ListSettings(PropertyGroup):
    """ """
    name: StringProperty(name="Name", default="", description="The item's name")
    item_int_setting: IntProperty(name="An Item Int", min=0, default=1, description="")

class GHISTEMPLATEADDON_PG_Settings(PropertyGroup):
    ''' '''
    my_enum = [
            ("A", "A", "A first option named A"),
            ("B", "B", "A second option named B"),
            ("C", "C", "A third option named C")
        ]

    int_setting: IntProperty(name="An Int", min=0, default=1, description="")
    bool_setting: BoolProperty(name="A Bool", default=True, description="")
    str_setting: StringProperty(name="A String", default="_Default String", description="")
    enum_setting: EnumProperty(name="An Enum", items=my_enum, default=2, description="")
    float_setting: FloatProperty(name="A Float", min=0, default=0, description="")

    items: CollectionProperty(type=GHISTEMPLATEADDON_PG_ListSettings)
    items_selected_index: IntProperty(name="Selected", default=0)

def register():
    bpy.types.Scene.TemplateAddonSettings = PointerProperty(type=GHISTEMPLATEADDON_PG_Settings) # instanciate property group per scene

def unregister():
    del bpy.types.Scene.TemplateAddonSettings