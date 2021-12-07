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

    def __init__(self, blogger, post_title, blog_name, address, published):
        #self.id = id
        self.blogger = blogger
        self.title = post_title
        self.name = blog_name
        self.address = address
        self.published = published

    def __str__(self):
        return f"{self.blogger}: {self.name}, {self.title}, {self.published}, ({self.address})"
