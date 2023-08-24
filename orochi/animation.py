from orochi.object import Object
class Animation:
    def __init__(self):
        self.__src = None
        self.frames = []
        self.frame_width = 0
        self.frame_height = 0
        self.reset_frame = 0
    def set_sprite_sheet(self, src, frame_width, frame_height, start_frame=-9999999, end_frame=9999999):
        start_frame = start_frame -1
        end_frame = end_frame - 1
        frames_number = 0  # Initialize frames_number to 0 instead of 1
        self.__src = src
        self.frame_width = frame_width
        self.frame_height = frame_height
        rows = int(self.__src.height / frame_height)
        columns = int(self.__src.width / frame_width)
        for row in range(rows):
            for column in range(columns):
                if start_frame <= frames_number <= end_frame:
                    self.frames.append({"x": 0 + (column * frame_width), "y": 0 + (row * frame_height)})
                frames_number += 1  # Increment frames_number here, after adding a frame
        self.frames.append(self.frames[-1])
    def play(self,speed,object : Object):
        object.animation = self
        speed = speed / 10
        src = self.__src
        if(object.image != src):
            object.image = src
        object.frame_x = self.frames[int(object.frame)]['x']
        object.frame_y = self.frames[int(object.frame)]['y']
        object.frame_width = self.frame_width
        object.frame_height = self.frame_height
        if(object.frame < len(self.frames) - 1):
            object.frame += speed
        else:
            object.frame = 0

