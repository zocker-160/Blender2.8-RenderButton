bl_info = {
	"name": "Blender 2.8x Simple RenderPanel",
	"author": "Mitsuma, Zocker_160",
	"version": (0, 0, 3),
	"blender": (2, 81, 0),
	"location": "Render Properties",
	"description": "",
	"warning": "",
	"wiki_url": "",
	"tracker_url": "",
	"category": "Render"}

import bpy 


class AddRenderPanel(bpy.types.Panel):
	"""Creates a Panel in the Object properties window"""
	bl_label = "Render"
	bl_idname = "OBJECT_PT_Add_Render"
	bl_space_type = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context = "render"

	def draw(self, context):
		layout = self.layout

		row1 = layout.row(align=True)
		row1.operator("render.render", text="Render", icon='RENDER_STILL')
		row1.operator("render.render", text="Animation", icon='RENDER_ANIMATION').animation = True
		
		row2 = layout.split()
		row2.label(text="Tile Order:")  	
		row2 = row2.row(align=True) 	
		row2.prop(bpy.context.scene.cycles, "tile_order", text="")
		
		row3 = layout.split()
		row3.label(text="Display:")
		row3 = row3.row(align=True)
		row3.prop(context.preferences.view, "render_display_type", text="")
		row3.prop(bpy.context.scene.render, "use_lock_interface", icon_only=True)

def register():
	bpy.utils.register_class(AddRenderPanel)

def unregister():
	bpy.utils.unregister_class(AddRenderPanel)

if __name__ == "__main__":
	register()
