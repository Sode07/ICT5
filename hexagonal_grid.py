from tkinter import *

class HexaCanvas(Canvas):
    print("sika")

    def __init__(self, master, *args, **kwargs):
        Canvas.__init__(self, master, *args, **kwargs)
    
        self.hexaSize = 20
    
    def setHexaSize(self, number):
        self.hexaSize = number
    
    
    def create_hexagone(self, x, y, color="black", fill="blue", color1=None, color2=None, color3=None, color4=None, color5=None, color6=None):

        size = self.hexaSize
        Δx = (size**2 - (size/2)**2)**0.5
    
        point1 = (x+Δx, y+size/2)
        point2 = (x+Δx, y-size/2)
        point3 = (x   , y-size  )
        point4 = (x-Δx, y-size/2)
        point5 = (x-Δx, y+size/2)
        point6 = (x   , y+size  )
    
        # This setting allows specifying a different color for each side.
        if color1 == None:
            color1 = color
        if color2 == None:
            color2 = color
        if color3 == None:
            color3 = color
        if color4 == None:
            color4 = color
        if color5 == None:
            color5 = color
        if color6 == None:
            color6 = color
    
        self.create_line(point1, point2, fill=color1, width=2)
        self.create_line(point2, point3, fill=color2, width=2)
        self.create_line(point3, point4, fill=color3, width=2)
        self.create_line(point4, point5, fill=color4, width=2)
        self.create_line(point5, point6, fill=color5, width=2)
        self.create_line(point6, point1, fill=color6, width=2)
    
        if fill != None:
            self.create_polygon(point1, point2, point3, point4, point5, point6, fill=fill)
    
class HexagonalGrid(HexaCanvas):
    print("kettu")
    """ A grid whose each cell is hexagonal """
    def __init__(self, master, scale, grid_width, grid_height, *args, **kwargs):
    
        Δx     = (scale**2 - (scale/2.0)**2)**0.5
        width  = 2 * Δx * grid_width + Δx
        height = 1.5 * scale * grid_height + 0.5 * scale

        HexaCanvas.__init__(self, master, background='white', width=width, height=height, *args, **kwargs)
        self.setHexaSize(scale)

        self.width = grid_width #Grid- ojektin pitäis tietää omat ulottuvuutensa, nii sitä ei tarvi hardcodaa
        self.height = grid_height

        # Store the fill colors of each hexagon in a dictionary
        self.hexagon_colors = {}

    def setCell(self, xCell, yCell, fill=None, *args, **kwargs):
        """ Create a content in the cell of coordinates x and y. Could specify options through keywords : color, fill, color1, color2, color3, color4; color5, color6"""
        # compute pixel coordinate of the center of the cell:
        size = self.hexaSize
        Δx = (size**2 - (size/2)**2)**0.5
    
        pix_x = Δx + 2*Δx*xCell
        if yCell%2 == 1 :
            pix_x += Δx
    
        # Add 5 to avoid clipping on top row of hexes
        pix_y = size + yCell*1.5*size + 5
    
        self.create_hexagone(pix_x, pix_y, fill=fill, *args, **kwargs)

        # Store the fill color of the hexagon
        self.hexagon_colors[(xCell, yCell)] = fill
    
    def getFill(self, xCell, yCell):
        """ Retrieve the fill color of the hexagon at coordinates xCell, yCell """
        return self.hexagon_colors.get((xCell, yCell), None)

    def getIndexFromXY(self,x,y): #hakee indeksin csv-filust nii ei tarvi kirjottaa indeksi = xCell * yCell
        return y * self.width + x