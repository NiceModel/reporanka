class Blog:

    def __init__(self, name, post, blogger, address, published):
        #self.id = id
        self.name = name
        self.post = post
        self.address = address
        self.blogger = blogger
        self.published = published

    def __str__(self):
        return f"{self.name}: {self.post}, {self.address}, {self.blogger}, ({self.published})"