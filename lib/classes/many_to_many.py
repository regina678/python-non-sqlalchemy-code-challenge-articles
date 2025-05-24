class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author  # Uses property setter
        self.magazine = magazine  # Uses property setter
        self.title = title  # Uses property setter
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            raise AttributeError("Title cannot be changed after initialization")
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not 5 <= len(title) <= 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        self._magazine = magazine


class Author:
    def __init__(self, name):
        self.name = name  # Uses property setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed after initialization")
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        magazines = list(set(article.magazine for article in self.articles()))
        return magazines if magazines else None

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        areas = list(set(magazine.category for magazine in self.magazines() if magazine))
        return areas if areas else None


class Magazine:
    def __init__(self, name, category):
        self.name = name  # Uses property setter
        self.category = category  # Uses property setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not 2 <= len(value) <= 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if len(value) == 0:
            raise ValueError("Category cannot be empty")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        contributors = list(set(article.author for article in self.articles()))
        return contributors if contributors else None

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        from collections import Counter
        authors = [article.author for article in self.articles()]
        author_count = Counter(authors)
        result = [author for author, count in author_count.items() if count > 2]
        return result if result else None