import arcade, math

width = 64
height = 42
screenColor = [0x36,0x45,0x4f]
backgroundColor = [0x0a,0x09,0x0c]
textColor = [0xee,0xe9,0xe5]
font = "Fonts/BigBlue_TerminalPlus"

screenTitle = "TEXTREME"

class TEXTREME(arcade.Window):
    def __init__(self):
        self.charsize = 16
        self.screenWidth = self.charsize*width
        self.screenHeight = self.charsize*height
        super().__init__(self.screenWidth, self.screenHeight, screenTitle, resizable = True, antialiasing = False)
        arcade.set_background_color(backgroundColor)
        
        self.textBox = arcade.create_rectangle_filled(self.screenWidth/2, (self.screenHeight/2) - (self.charsize/2), self.screenWidth - self.charsize, self.screenHeight - (self.charsize*2), screenColor)
        
    def setup(self):
        self.text = ["data","lorem ipsum","blah blah blah blah blah blah blah blah blah blah blah blah blah blah"]
        self.visibleRows = math.floor(self.screenHeight/self.charsize)
        self.visibleColumns = math.floor(self.screenWidth/self.charsize)
        self.firstColumn = 0
        self.firstRow = 0
        
    def on_resize(self, w, h):
        super().on_resize(w, h)
        self.screenWidth = w
        self.screenHeight = h
        self.charsize = int(w/width) if width < height else int(h/height)
        
        self.visibleRows = math.floor(self.screenHeight/self.charsize)
        self.visibleColumns = math.floor(self.screenWidth/self.charsize)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_xywh_rectangle_filled(self.charsize/2, self.charsize * 2.5, self.screenWidth - self.charsize, self.screenHeight - 3 * self.charsize, screenColor)
        arcade.draw_text("F1:SAVE F2:SAVE AS F3:LOAD F4:SET BPM F5:LINE WRAP", self.charsize/2, self.charsize/2, textColor, self.charsize, self.screenWidth - self.charsize, "center", font)
        
        for line in range(self.firstRow, self.firstRow + self.visibleRows):
            if line >= len(self.text):
                break
            arcade.draw_text(self.text[line], self.charsize/2, self.screenHeight - self.charsize * (line - self.firstRow + 1.5), textColor, self.charsize, self.screenWidth - self.charsize, "center", font)
        
window = TEXTREME()
window.setup()
arcade.run()