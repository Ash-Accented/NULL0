class PlayerBrief:
    """
    A brief summary of information about a player for passing over the network that contains enough information to render client side
    """
    def from_data(self, vx, vy, dx, dy, radius, color, color_eq, character):
        """
        Package data about a player into a PlayerBrief
        """
        self.vx = vx
        self.vy = vy
        self.dx = dx
        self.dy = dy
        self.r = radius
        self.drx, self.dry = 0, 0
        self.w, self.h = self.r*2, self.r*2
        self.rendered_rect = None
        self.hitbox = None
        self.color = color
        self.color_eq = color_eq
        self.character = character
    def to_bytes(self):
        """
        Convert a PlayerBrief into a bytearray and return it
        """
        as_bytes = bytearray()
        vx = int(self.vx*1000) #multiply vx (a float) by 1000 and cast to an int to preserve 3 bytes precision 
        vy = int(self.vy*1000) #same
        dx = int(self.dx*1000) #same
        dy = int(self.dy*1000) #same
        #rendered_rect = int(self.rendered_rect*1000)
        #hitbox = int(self.hitbox*1000)
        as_bytes.extend(vx.to_bytes(4, 'big')) #convert to a 4 byte int
        as_bytes.extend(vy.to_bytes(4, 'big')) #same
        as_bytes.extend(dx.to_bytes(4, 'big')) #same
        as_bytes.extend(dy.to_bytes(4, 'big')) #same
        #as_bytes.extend(rendered_rect.to_bytes(4, 'big'))
        #as_bytes.extend(hitbox.to_bytes(4, 'big'))
        return as_bytes
	
    def from_bytes(self, as_bytes):
        """
        Takes a byte array representation of a PlayerBrief and converts it back into a regular object
        """
        self.vx = int.from_bytes(as_bytes[0], 'big')/1000 #convert back to a float by casting the bytes to an int and then dividing by 1000. this inverts the steps of to_bytes
        self.vy = int.from_bytes(as_bytes[1], 'big')/1000 #same
        self.dx = int.from_bytes(as_bytes[2], 'big')/1000 #same
        self.dy = int.from_bytes(as_bytes[3], 'big')/1000 #same
    #    self.rendered_rect = int.from_bytes(as_bytes[4], 'big')/1000
     #   self.hitbox = int.from_bytes(as_bytes[5], 'big')/1000
