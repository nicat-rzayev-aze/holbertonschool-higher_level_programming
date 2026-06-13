class NotifiedList(list):
    """
    A custom list class that extends Python's built-in list class to provide 
    notifications whenever items are added, removed, or modified.
    
    This class overrides common list modification methods to print notification
    messages, allowing users to track all changes made to the list.
    """
    
    def append(self, item):
        """
        Add an item to the end of the list and notify.
        
        Args:
            item: The item to be added to the list.
        """
        super().append(item)
        print(f"Appended [{item}] to the list.")
    
    def remove(self, item):
        """
        Remove the first occurrence of an item from the list and notify.
        
        Args:
            item: The item to be removed from the list.
            
        Raises:
            ValueError: If the item is not found in the list.
        """
        super().remove(item)
        print(f"Removed [{item}] from the list.")
    
    def pop(self, index=-1):
        """
        Remove and return an item at the given index (default last item) and notify.
        
        Args:
            index: The index of the item to pop (default is -1 for last item).
            
        Returns:
            The item that was removed from the list.
            
        Raises:
            IndexError: If the list is empty or index is out of range.
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
    
    def extend(self, items):
        """
        Extend the list by appending all items from an iterable and notify.
        
        Args:
            items: An iterable containing items to be added to the list.
        """
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")
    
    def clear(self):
        """
        Remove all items from the list and notify.
        """
        super().clear()
        print("Cleared the list.")
    
    def insert(self, index, item):
        """
        Insert an item at a given position and notify.
        
        Args:
            index: The index at which to insert the item.
            item: The item to be inserted.
        """
        super().insert(index, item)
        print(f"Inserted [{item}] at index {index}.")
        
if __name__ == "__main__":
    nlist = NotifiedList()
    nlist.append(1)
    nlist.append(2)
    nlist.append(3)
    nlist.extend([4, 5])
    nlist.remove(2)
    nlist.pop()
    print(f"Final list: {nlist}")
