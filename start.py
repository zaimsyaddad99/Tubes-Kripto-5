import page.menu as guistart

def initialize():
	global SorV, p, q, e
	SorV = ""
	f = open("key.config", "r")
	p, q, e = f.read().split(" ")
	p, q, e = int(p), int(q), int(e)
initialize()

if __name__ == '__main__':
	guistart.vp_start_gui()