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

