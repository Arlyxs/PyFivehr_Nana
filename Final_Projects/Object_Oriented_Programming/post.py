# Create Class


class Post:
    def __init__(self, message, author):
        self.message = message
        self.author = author

    def get_post_info(self):
        return f"Post: {self.message} written by {self.author}"
