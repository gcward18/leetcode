'''
🗃️ Problem 2: In-Memory File System (Design + Trie/Dict)
Scenario:
Design a simple in-memory file system that supports basic Unix-style file operations.

✅ Required Methods:
python
Copy
Edit
class FileSystem:
    def ls(path: str) -> List[str]
    def mkdir(path: str) -> None
    def addContentToFile(filePath: str, content: str) -> None
    def readContentFromFile(filePath: str) -> str
🧾 Behavior:
ls(path)
Returns a list of files and directories at the given path (sorted lexicographically).
If path is a file, return just that file name.

mkdir(path)
Creates directories recursively like mkdir -p.

addContentToFile(filePath, content)
Appends to an existing file or creates it if it doesn't exist.

readContentFromFile(filePath)
Returns the content of the given file.

🧠 Example:
python
Copy
Edit
fs = FileSystem()
fs.mkdir("/a/b/c")
fs.addContentToFile("/a/b/c/d", "hello")
print(fs.ls("/"))         # ["a"]
print(fs.ls("/a/b/c"))    # ["d"]
print(fs.readContentFromFile("/a/b/c/d"))  # "hello"
Constraints:
Path format: /a/b/c (components separated by /)

You may use nested dictionaries or custom Trie nodes.

File vs directory detection is required.


'''
from abc import ABC, abstractmethod

class Parentable(ABC):
    @abstractmethod
    def get_children(self):
        pass

class Assignable(ABC):
    @abstractmethod
    def get_name(self):
        pass

class File(Assignable):
    def __init__(self, name: str, contents: str, parent: Parentable):
        self.name = name
        self.contents = contents
        self.parent = parent
    
    def get_name(self):
        return self.name
    
    def get_content(self):
        return self.contents
        
class Directory(Parentable, Assignable):
    def __init__(self, name: str, parent: Parentable= None):
        self.name = name
        self.parent = parent
        self.children = {}
    
    def get_children(self):
        return self.children
    
    def get_name(self):
        return self.name
    
class FileSystem:
    def __init__(self):
        self.root = Directory("home")
    
    def _parse_path(self, path: str):
        return [p for p in path.split('/') if p]
    
    def _traverse(self, root: Parentable, path: list[str]) -> Assignable:
        if not root and path:
            return None
        
        if not path:
            return root
        
        if path[0] in root.get_children():
            return self._traverse(root.get_children()[path[0]], path[1:])
        
    def ls(self, path: str) -> list[str]:
        item = self._traverse(self.root, path=self._parse_path(path))
        
        # check if instance of a parentable item       
        if isinstance(item, Parentable):
            return sorted([child for child in item.get_children().keys()] )
        elif isinstance(item, Assignable):
            return [item.name]
        else:
            return []

    def mkdir(self, path: str) -> None:
        head = self.root
        items = self._parse_path(path)
        
        for item in items:
            if item not in head.get_children():
                head.get_children()[item] = Directory(item, head)
            head = head.get_children()[item]

    def addContentToFile(self, filePath: str, content: str) -> None:
        head = self.root
        items = self._parse_path(filePath)
        
        for item in items[:-1]:
            if item not in head.get_children():
                head.get_children()[item] = Directory(item, head)
            head = head.get_children()[item]
        
        if items[-1] not in head.get_children():
            head.get_children()[items[-1]] = File(items[-1], content, head)
        else:
            head.get_children()[items[-1]].contents += content

    def readContentFromFile(self, filePath: str) -> str:
        item = self._traverse(self.root, self._parse_path(filePath))
        if item:
            return item.get_content()
        else:
            return ""

    
if __name__ == "__main__":
    fs = FileSystem()
    fs.mkdir("/a/b/c")
    fs.addContentToFile("/a/b/c/d", "hello")
    print(fs.ls("/"))         # ["a"]
    print(fs.ls("/a/b/c"))    # ["d"]
    print(fs.readContentFromFile("/a/b/c/d"))  # "hello"
