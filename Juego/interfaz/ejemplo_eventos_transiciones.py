from cocos.director import director
from cocos.scene import Scene
from cocos.sprite import Sprite
from cocos.scenes.transitions import *
from cocos import layer  

class Capa1(layer.Layer):  
    is_event_handler = True
    contador = 0

    def __init__(self):
        super().__init__()
        mi_sprite = Sprite('fondo.jpg', (320, 240))
        self.add(mi_sprite)

    def on_mouse_release(self, x, y, buttons, modifiers):
        if Capa1.contador == 0:
            Capa1.contador += 1
            director.replace(RotoZoomTransition(Scene(Capa2()), 3))
        elif Capa1.contador == 1:
            Capa1.contador += 1
            director.replace(SlideInBTransition(Scene(Capa2()), 2))
        elif Capa1.contador == 2:
            Capa1.contador += 1
            director.replace(TurnOffTilesTransition(Scene(Capa2()), 2))
        elif Capa1.contador == 3:
            Capa1.contador += 1
            director.replace(EnvelopeTransition(Scene(Capa2()), 2))
        elif Capa1.contador == 4:
            Capa1.contador += 1
            director.replace(JumpZoomTransition(Scene(Capa2()), 2))
        elif Capa1.contador == 5:
            Capa1.contador += 1
            director.replace(FadeDownTransition(Scene(Capa2()), 2))
        elif Capa1.contador == 6:
            Capa1.contador += 1
            director.replace(CornerMoveTransition(Scene(Capa2()), 2))
        elif Capa1.contador == 7:
            Capa1.contador += 1
            director.replace(MoveInLTransition(Scene(Capa2()), 2))
        elif Capa1.contador == 8:
            Capa1.contador += 1
            director.replace(FlipX3DTransition(Scene(Capa2()), 2))

class Capa2(layer.Layer): 
    is_event_handler = True

    def __init__(self):
        super().__init__()
        mi_sprite = Sprite('fondo2.png', (320, 248))
        self.add(mi_sprite)

    def on_mouse_release(self, x, y, buttons, modifiers):
        if Capa1.contador == 1:
            director.replace(FlipAngular3DTransition(Scene(Capa1()), 2))
        elif Capa1.contador == 2:
            director.replace(ShuffleTransition(Scene(Capa1()), 2))
        elif Capa1.contador == 3:
            director.replace(ShrinkGrowTransition(Scene(Capa1()), 2))
        elif Capa1.contador == 4:
            director.replace(SplitColsTransition(Scene(Capa1()), 2))
        elif Capa1.contador == 5:
            director.replace(MoveInRTransition(Scene(Capa1()), 2))
        elif Capa1.contador == 6:
            director.replace(FlipY3DTransition(Scene(Capa1()), 2))
        elif Capa1.contador == 7:
            director.replace(FadeTRTransition(Scene(Capa1()), 2))
        elif Capa1.contador == 8:
            director.replace(MoveInTTransition(Scene(Capa1()), 2))
        elif Capa1.contador == 9:
            director.replace(SplitRowsTransition(Scene(Capa1()), 2))

if __name__ == "__main__":
    director.init(caption='Ejemplo de eventos y transiciones')
    director.window.set_location(600, 200)
    director.run(Scene(Capa1()))
