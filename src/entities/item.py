'''Module for reading tip item objects.'''
from utilities.utilities import generate_id

class Item:
    '''Superclass for reading tip entities.

    attr:
        cat: str: category of the item; defaults to 'item'
        id: str: unique identifier for the item
        creator: str: creator of the item
        title: str: title of the item
        published: str: publishing date or year of the item'''
    def __init__(self, creator, title, published, item_id, cat='item'):
        self._cat = cat
        self._id = generate_id() if item_id is None else item_id
        self._creator = creator
        self._title = title
        self._published = published

    @property
    def item_id(self):
        return self._id

    @property
    def info(self):
        return [self._cat, self._id, self._creator, self._title]

    @property
    def details(self):
        return {
            'type': self._cat, 'id': self._id, 'creator': self._creator,
            'title': self._title, 'published': self._published
        }

    @property
    def csv_data(self):
        return ';'.join(self.details.values())

    def __str__(self):
        return f'{self._creator}: {self._title} ({self._published})'

class Book(Item):
    '''Class for book entities.

    attr:
        cat: str: 'book'
        id: str: unique identifier for the item
        creator: str: authhor of the book
        title: str: name of the book
        published: str: publishing year of the book'''
    def __init__(self, author, title, published, item_id=None):
        super().__init__(author, title, published, item_id, 'book')

    @property
    def details(self):
        return {
            'type': self._cat, 'id': self._id, 'author': self._creator,
            'name': self._title, 'published': self._published
        }

class Blog(Item):
    '''Class for blog post entities.
    
    attr:
        cat: str: 'blog'
        id: str: unique identifier for the item
        creator: str: creator of the blog post
        title: str: title of the blog post
        name: str: name of the blog
        published: str: publishing date of the blog post
        url: str: web address of the blog post
    '''
    def __init__(self, creator, blog_name, post_title, url, published, item_id=None):
        super().__init__(creator, post_title, published, item_id, 'blog')
        self._name = blog_name
        self._url = url

    @property
    def details(self):
        return {
            'type': self._cat, 'id': self._id, 'creator': self._creator,
            'blog': self._name, 'post': self._title,
            'url': self._url, 'published': self._published
        }

class Video(Item):
    '''Class for video entities.
    
    attr:
        cat: str: 'video'
        id: str: unique identifier for the item
        creator: str: creator of the video
        title: str: title of the video
        published: str: publishing date or year of the video
        url: str: web address of the video
    '''
    def __init__(self, creator, title, url, published, item_id=None):
        super().__init__(creator, title, published, item_id)
        self._url = url

    @property
    def details(self):
        return {
            'type': self._cat, 'id': self._id, 'creator': self._creator,
            'name': self._title, 'url': self._url, 'published': self._published
        }
