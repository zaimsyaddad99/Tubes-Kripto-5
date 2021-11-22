import page.menu as guistart

def initialize():
	global status, SorV, p, q, e
	status = "Status: App succesfully opened"
	SorV = ""
	f = open("key.config", "r")
	p, q, e = f.read().split(" ")
	p, q, e = int(p), int(q), int(e)
initialize()

if __name__ == '__main__':
	guistart.vp_start_gui()