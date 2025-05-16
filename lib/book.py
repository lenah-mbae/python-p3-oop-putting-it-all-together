#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        """"The title property"""
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        """"Page_count must be an interger"""
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    @property
    def turn_page(self):
        """"The turn_page property"""
        return self._turn_page
    
   
    def turn_page(self):
       
            print("Flipping the page...wow, you read fast!")

