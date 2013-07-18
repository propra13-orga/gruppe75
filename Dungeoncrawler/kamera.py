''' Die Kamera-Klasse'''
class Kamera(object):
    
    game = None
    
    def initialisierung(figur, h, b):
        figur.hoehe = h
        figur.breite = w
        figur.x = 0
        figur.y = 0
        figur.edge = 7
    
    def get_viewport(figur):
        return figur.x, figur.y, figur.x + figur.breite, figur.y + figur.height
    
    def in_view(figur, x, y):
        if x >= figur.x and x <= figur.x + figur.breite:
            if y >= figur.y and y <= figur.y + figur.height:
                return True
        return False    
    
    def adjust(figur, position):
        x, y = position
        adj = False
        #justierung nach unten
        if y - figur.y > figur.height - figur.edge:
            figur.y += 1
            adj = True
        #justierung nach oben
        if y - figur.y < figur.edge:
            figur.y -= 1
            adj = True
            
        #ajustierung nach rechts
        if x - figur.x > figur.breite - figur.edge:
            figur.x += 1
            adj = True
        #justierung nach links
        if x - figur.x < figur.edge:
            figur.x -= 1
            adj = True
        return adj
