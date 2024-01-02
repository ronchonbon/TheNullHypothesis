init -1:

    default NewsPool = NewsPoolClass()
            
init -2 python:

    class ArticleClass(object):
        def __init__(self, name, photo, author, headline, subheadline, body):
            self.name = name

            self.photo = photo

            self.author = author

            self.headline = headline

            self.subheadline = subheadline

            self.body = body

    class NewsPoolClass(object):
        def __init__(self):
            self.Articles = {}

        def update(self, N):
            self.Articles[N.name] = N

            return

        def remove(self, N):
            if N.name in self.Articles.keys():
                del self.Articles[N.name]
                
            return