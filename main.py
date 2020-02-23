import arcade

width = 64
height = 42
screenColor = [0x36,0x45,0x4f]
backgroundColor = [0x0a,0x09,0x0c]
textColor = [0xee,0xe9,0xe5]

screenTitle = "TEXTREME"

class TEXTREME(arcade.Window):
    def __init__(self):
        self.screenWidth = 16*width
        self.screenHeight = 16*height
        self.charsize = 16
        super().__init__(self.screenWidth, self.screenHeight, screenTitle, resizable = True, antialiasing = False)
        arcade.set_background_color(backgroundColor)
        
        self.textBox = arcade.create_rectangle_filled(self.screenWidth/2, (self.screenHeight/2) - (self.charsize/2), self.screenWidth - self.charsize, self.screenHeight - (self.charsize*2), screenColor)
        
    def on_resize(self, w, h):
        super().on_resize(w, h)
        self.screenWidth = w
        self.screenHeight = h
        self.charsize = int(w/width) if width < height else int(h/height)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_xywh_rectangle_filled(self.charsize/2, self.charsize * 2.5, self.screenWidth - self.charsize, self.screenHeight - 3 * self.charsize, screenColor)
        arcade.draw_text("F1:SAVE F2:SAVE AS F3:LOAD F4:SET BPM F5:LINE WRAP", self.charsize/2, self.charsize/2, textColor, self.charsize, self.screenWidth - self.charsize, "center", "Fonts/C64_Pro_Mono-STYLE")
        
window = TEXTREME()
arcade.run()