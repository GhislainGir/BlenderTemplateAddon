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

#######################################################################################
###################################### FUNCTIONS ######################################
#######################################################################################

def first_function(context: bpy.types.Context, int_arg: int) -> tuple[bool, int]:
    """
    
    :param context:
    :param int_arg:
    :return: the function's success, potential error message
    :rtype: tuple
    """
    if int_arg > 0:
        return (True, "")
    
    else:
        return(False, "Int is not above 0. This is an example.")