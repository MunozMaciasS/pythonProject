#Crée par Samuel Munoz Mars 2023
#but: Faire en sorte d’afficher 20 cercles de couleur différente à des positions aléatoires dans la fenêtre(sans toucher les coins)

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
         arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY, arcade.color.AERO_BLUE,arcade.color.BITTERSWEET_SHIMMER]

class Cercle():
   def __init__(self,rayon,center_x,center_y,color):
       self.rayon = rayon
       self.center_x = center_x
       self.center_y = center_y
       self.color = color

   def draw(self):
       arcade.draw_circle_filled(self.center_x,self.center_y,self.rayon,self.color)
       pass


class MyGame(arcade.Window):
   def __init__(self):
       super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
       self.liste_cercles = []

   def setup(self):
       # remplir la liste avec 20 objets de type Cercle
       for _ in range(20):
           rayon = random.randint(10,50)
           center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
           center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
           color = random.choice(COLORS)
           self.liste_cercles.append(Cercle(rayon,center_x,center_y,color)) #on appelle le contrustor et on append l'object crée

   def on_draw(self):
       arcade.start_render()

       for cercle in self.liste_cercles:
           cercle.draw()


def main():
   my_game = MyGame()
   my_game.setup()

   arcade.run()


main()
