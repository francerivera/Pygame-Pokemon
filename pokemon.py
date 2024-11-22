from PIL import Image
import os

class Pokemon:
    def __init__(self, name:str, type:str, health:str, power:str, file_path:str) -> None:
        self.name = name
        self.type = type
        self.health = health
        self.power = power
        self.file_path = file_path
        
    # convert gif file to multiple images/frames
    def animation_frames(self):
        self.frames = []
        gif = Image.open(self.file_path)
        for frame in range(gif.n_frames):
            gif.seek(frame)
            frame_image = gif.copy()
            frame_path = (f"./bin/frame_{frame}.png")
            frame_image.save(frame_path)
            self.frames.append(frame_path)
        return self.frames
    
    def animation_clean_up(self):
        for frame in self.frames:
            os.remove(frame)
            
butterfree = Pokemon("Charizard", "Fire", 100, 100, "./assets/butterfree.gif")  
charizard = Pokemon("Charizard", "Fire", 100, 100, "./assets/charizard.gif")
dugtrio = Pokemon("Charizard", "Fire", 100, 100, "./assets/dugtrio.gif")
golbat = Pokemon("Charizard", "Fire", 100, 100, "./assets/golbat.gif")
kadabra = Pokemon("Charizard", "Fire", 100, 100, "./assets/kadabra.gif")
meowth = Pokemon("Charizard", "Fire", 100, 100, "./assets/meowth.gif")
nidoking = Pokemon("Charizard", "Fire", 100, 100, "./assets/nidoking.gif")
pidgeot = Pokemon("Charizard", "Fire", 100, 100, "./assets/pidgeot.gif")
pikachu = Pokemon("Charizard", "Fire", 100, 100, "./assets/pikachu.gif")
venonat = Pokemon("Charizard", "Fire", 100, 100, "./assets/venonat.gif")
venusaur = Pokemon("Charizard", "Fire", 100, 100, "./assets/venusaur.gif")
wartortle = Pokemon("Charizard", "Fire", 100, 100, "./assets/wartortle.gif")