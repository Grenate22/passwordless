class EmailNotValid(Exception):
    def __init__(self, message="Email did not exist") -> None:
        self.message = message
        super().__init__(self.message)