# graphics 
screen_w = 640
screen_h = 480
screen_size = (screen_w, screen_h)

def split_surface(surface, w, h):
    result =[]
	
    for y in range(0, surface.get_height(), h):
        for x in range (0, surface.get_width(), w):
            result.append(surface.subsurface((x,y), (w,h)))
    return result
	
class Animation(object):

    def __init__ (self, frames, frame_duration):
        self.frames = frames
        self.frame_duration = frame_duration
        self.length = len[frames] * frame_duration
        self.timer = 0
		
		
		# dt = numer ob miliesconds after the last update
		
    def update(self, dt):
        self.timer = (self.timer * dt) % self.length
			
    def current_frame(self):
    # return the current frame in the animation
        return self.frames[self.timer / self.frame_duration]
        
    def reset(self):
        self.timer = 0