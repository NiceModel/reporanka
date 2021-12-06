from entities.blog import Blog
from repositories.blog_repository import (BLOG_REPOSITORY as default_blog_repository)
from services.id_generator import (id_generator as default_id_generator)

class BlogService:

    def __init__(self, blog_repository = default_blog_repository, id_generator = default_id_generator):
        self._blog_repository = blog_repository
        self._id_generator = id_generator


    def create_blog(self, name, post, address, blogger, published):
        blog_id = self._id_generator.new_id()
        blog = self._blog_repository.create(Blog(blog_id, name, post, address, blogger, published))
        return blog

    def find_all_blogs(self):
        blogs = self._blog_repository.find_all()
        return sorted(blogs, key=lambda blog: blog.blog.lower())

BLOG_SERVICE = BlogService()