from modules.library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self,title,subject,upc,volume,issue):
        LibraryItem.__init__(self,title,subject,upc)
        self.volume = volume
        self.issue = issue
