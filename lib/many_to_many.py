# This file contains the classes for Authors, Magazines, and Articles

class Author:
    # Keep track of all Author instances
    all = []

    def __init__(self, name):
        # Make sure name is a string and not empty
        if not isinstance(name, str):
            raise Exception("Author name must be a string")
        if len(name) == 0:
            raise Exception("Author name must be longer than 0 characters")
        # Removed the incorrect check for _name attribute to allow correct initialization
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        # Return the author's name
        return self._name

    @name.setter
    def name(self, value):
        # Ignore any attempt to change name to maintain immutability
        pass

    def articles(self):
        # Return all articles written by this author
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        # Return a list of unique magazines this author has written for
        magazines = []
        for article in self.articles():
            if article.magazine not in magazines:
                magazines.append(article.magazine)
        return magazines

    def add_article(self, magazine, title):
        # Make sure magazine is a Magazine instance
        if not isinstance(magazine, Magazine):
            raise Exception("Argument 'magazine' must be a Magazine instance")
        # Create a new Article with this author, the magazine, and title
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        # Return unique categories of magazines this author has written for,
        # or None if no articles
        if not self.articles():
            return None
        categories = set(article.magazine.category for article in self.articles())
        return list(categories)


class Magazine:
    # Keep track of all Magazine instances
    all = []

    def __init__(self, name, category):
        # Validate name and category types and lengths
        if not isinstance(name, str):
            raise Exception("Magazine name must be a string")
        if not (2 <= len(name) <= 16):
            raise Exception("Magazine name must be between 2 and 16 characters inclusive")
        if not isinstance(category, str):
            raise Exception("Magazine category must be a string")
        if len(category) == 0:
            raise Exception("Magazine category must be longer than 0 characters")
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        # Return magazine name
        return self._name

    @name.setter
    def name(self, new_name):
        # Validate new name before setting
        if not isinstance(new_name, str):
            # Ignore invalid assignment (tests expect original value to remain)
            return
        if not (2 <= len(new_name) <= 16):
            # Ignore invalid assignment
            return
        self._name = new_name

    @property
    def category(self):
        # Return category
        return self._category

    @category.setter
    def category(self, new_category):
        # Validate new category before setting
        if not isinstance(new_category, str):
            return
        if len(new_category) == 0:
            return
        self._category = new_category

    def articles(self):
        # Return all articles published in this magazine
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # Return unique authors who have articles in this magazine
        contributors = []
        for article in self.articles():
            if article.author not in contributors:
                contributors.append(article.author)
        return contributors

    def article_titles(self):
        # Return list of titles of articles published, else None
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        # Return authors with more than 2 articles in this magazine, else None
        authors = self.contributors()
        contrib_more_than_two = []
        for author in authors:
            count = len([article for article in self.articles() if article.author == author])
            if count > 2:
                contrib_more_than_two.append(author)
        if len(contrib_more_than_two) == 0:
            return None
        return contrib_more_than_two

    @classmethod
    def top_publisher(cls):
        # Return the magazine with the most articles, else None
        if not Article.all:
            return None
        counts = {}
        for article in Article.all:
            counts[article.magazine] = counts.get(article.magazine, 0) + 1
        top_magazine = max(counts.items(), key=lambda item: item[1])[0]
        return top_magazine


class Article:
    # Keep track of all Article instances
    all = []

    def __init__(self, author, magazine, title):
        # Validate inputs for type and length
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine instance")
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be between 5 and 50 characters inclusive")

        self._author = author
        self._magazine = magazine
        self._title = title

        Article.all.append(self)

    @property
    def title(self):
        # Return the article's title
        return self._title

    # Title cannot be changed, no setter

    @property
    def author(self):
        # Return author
        return self._author

    @author.setter
    def author(self, new_author):
        # Validate new author before setting
        if not isinstance(new_author, Author):
            raise Exception("Author must be an Author instance")
        self._author = new_author

    @property
    def magazine(self):
        # Return magazine
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        # Validate new magazine before setting
        if not isinstance(new_magazine, Magazine):
            raise Exception("Magazine must be a Magazine instance")
        self._magazine = new_magazine
