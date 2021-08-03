class IndicesOutOfBoundsError(Exception):
    """Exception raised when a list of indices passed to a DiceCup constructor is out of range"""
    
    def __init__(self, indices, message="You passed an invalid index"):
        self.message = message
        self.indices = indices
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.indices} <- {self.message}'