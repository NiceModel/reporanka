class Blog:

    def __init__(self, blogger, name, post, address, published):
        #self.id = id
        self.name = name
        self.post = post
        self.address = address
        self.blogger = blogger
        self.published = published

    def __str__(self):
        return f"{self.blogger}: {self.name}, {self.post}, {self.published}, ({self.address})"
