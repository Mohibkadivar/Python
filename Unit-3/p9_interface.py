from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_details(self):
        pass

class Saveable(ABC):
    @abstractmethod
    def save(self):
        pass

class Document(Printable, Saveable):
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def print_details(self):
        print(f"Title: {self.title}")
        print(f"Content: {self.content}")

    def save(self):
        print(f"Document '{self.title}' saved successfully.")

doc = Document("Report", "This is a sample report.")
doc.print_details()
doc.save()
