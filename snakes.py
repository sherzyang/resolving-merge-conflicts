class Snake:
    """A dangerous and/or hamless serpent.""""
    pass 

class Cobra(Snake): 
    """Definitely dangerous, yup."""
    def bite(self,other):
        """Deliver a dose of venmo."""
        super().__init__()
	self.size = 'medium'
    
class BoaConstrictor(Snake):
    """This one gives really good hugs."""
    
    def squeeze(self, other): 
        """Give a hug."""
        pass

