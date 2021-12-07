"""Module for Blog objects."""
class Blog:
    """Class for describing a Blog object.

    attr:
        name: str: name of the blog
        post: str: title of the blog post
        address: str: url to the blog post
        blogger: str: name of the blogger
        published: str: publication date of the blog post
    """

    def __init__(self, blogger, post, name, address, published):
        #self.id = id
        self.name = name
        self.post = post
        self.address = address
        self.blogger = blogger
        self.published = published

    def __str__(self):
        return f"{self.blogger}: {self.name}, {self.post}, {self.published}, ({self.address})"
