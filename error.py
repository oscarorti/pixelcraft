class NotValidURL(Exception):
    def __init__(self, message="The provided string is not a valid URL"):
        super().__init__(message)
