# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = '/'
        self.child = {}
        self.handler = None

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        curr = self.child
        split_path = path.split('/')
        for page in split_path:
            curr.insert(RouteTrieNode(page))
            curr = curr.child[page]
        curr.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if path == '/': return self.handler
        split_path = path.split('/')

        for path in split_path:
            curr = self
            for sub_path in path:
                curr = curr.child
                curr = curr[sub_path]
            handler = curr.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, value=''):
        # Initialize the node with children as before, plus a handler
        self.child = {}
        self.value = value
        self.handler = None

    def insert(self, child_path, handler = None):
        # Insert the node as before
        self.child[child_path] = self.child.get(child_path, RouteTrieNode(child_path))
        self.child[child_path].handler = handler

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = '/'
        self.child = {}
        self.handler = root_handler
        self.not_found = not_found_handler

    def add_handler(self, path, path_handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if path == self.root: self.handler = path_handler
        else:
            curr_sub_path = True
            split_path = self.split_path(path)
            curr = self.child
            for sub_path in split_path:
                if not sub_path:
                    continue
                if curr_sub_path:
                    curr_sub_path = False
                    curr[sub_path] = curr.get(sub_path, RouteTrieNode(sub_path))
                    curr = curr[sub_path]
                else:
                    curr.insert(sub_path, path_handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == '/': return self.handler
        split_path = self.split_path(path)
        curr = self

        for sub_path in split_path:
            if sub_path:
                if sub_path in curr.child:
                    curr = curr.child
                    curr = curr[sub_path]
                else: return self.not_found

        return curr.handler if curr.handler else None


    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.split('/')

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/secret", "secret handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup(''))
print(router.lookup("//"))
print(router.lookup("/home123"))
print(router.lookup("home123/"))
print(router.lookup("home/secret/"))
print(router.lookup("/home/secret/"))
print(router.lookup("/home/secret"))
