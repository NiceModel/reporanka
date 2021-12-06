from entities.blog import Blog
from utilities.csv_utilities import read_blogs_csv, write_blogs_csv

class BlogRepository:

    def __init__(self, path=NULL):
        self._path = path
        self._blogs = read_blogs_csv(self._path)

    def find_all(self, blog):
        if isinstance(blog, Blog):
            if not self._is_duplicate(blog):
                self._blogs.append(blog)
                write_blogs_csv(blog, self._path)
                return blog
            return "duplicate"
        raise TypeError(
            f"Object should be <class 'Blog'>, but was {type(blog)}")

    def _is_duplicate(self, new_blog):
        for blog in self._blogs:
            if str(blog) == str(new_blog):
                return True
        return False
            

BLOG_REPOSITORY = BlogRepository()