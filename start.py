import page.menu as guistart

def initialize():
	global status, SorV
	status = "Status: App succesfully opened"
	SorV = ""
initialize()

if __name__ == '__main__':
	guistart.vp_start_gui()