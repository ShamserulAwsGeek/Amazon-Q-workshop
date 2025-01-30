class Folders:
    def __init__(self, name, parent=None):
        """
        Initialize a Folders object.
        
        Args:
            name (str): Name of the folder
            parent (Folders, optional): Parent folder object, defaults to None
        """
        self.name = name
        self.parent = parent
        self.children = set()  # Using set to prevent duplicate children
        
        # If parent is provided, add this folder as a child of the parent
        if parent:
            parent.add_child(self)
    
    def add_child(self, child):
        """
        Add a child folder to this folder.
        
        Args:
            child (Folders): Child folder object to add
            
        Returns:
            bool: True if child was added, False if child already exists
        """
        if child not in self.children:
            self.children.add(child)
            child.parent = self
            return True
        return False
    
    def remove_child(self, child):
        """
        Remove a child folder from this folder.
        
        Args:
            child (Folders): Child folder object to remove
            
        Returns:
            bool: True if child was removed, False if child wasn't found
        """
        if child in self.children:
            self.children.remove(child)
            child.parent = None
            return True
        return False
    
    def get_children(self):
        """
        Get all children of this folder.
        
        Returns:
            set: Set of child folder objects
        """
        return self.children
