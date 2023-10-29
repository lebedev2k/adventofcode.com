class Node:
    def __init__(self, parent=None, name='', filesize=0) -> None:
        self.parent = parent
        self.childs = {}
        # self.name = name
        self.size = filesize
        
    def __repr__(self) -> str:
        return f'{self.name}, {self.size}'
        
    def __str__(self) -> str:
        return self.__repr__()

found_nodes = []
found_nodes2 = []

def walk_tree_task1(root: Node, level):
    # print('\t'*level, root.name, root.size)
    for node in root.childs.values():
        walk_tree_task1(node, level+1)
        root.size += node.size
    if root.childs and root.size<100000:
        found_nodes.append(root)

def walk_tree_task2(root: Node, space_need):
    # print('\t'*level, root.name, root.size)
    for node in root.childs.values():
        walk_tree_task2(node, space_need)
    if root.childs and root.size>=space_need:
        found_nodes2.append(root)
        
        
current_node = root = Node()

with open('day 07\input.txt') as f:
    lines = f.read().split('\n')
    for line in lines[1:]:
        parsed_line = line.split()
        if parsed_line[0] == '$':
            if  parsed_line[1] == 'cd':
                if parsed_line[2] == '/':
                    current_node = root
                elif parsed_line[2] == '..':
                    current_node = current_node.parent
                else:
                    current_node = current_node.childs[parsed_line[2]]
        else:
            new_node = Node(parent=current_node, name=parsed_line[1], filesize=0 if parsed_line[0] == 'dir' else int(parsed_line[0]))
            current_node.childs[parsed_line[1]] = new_node

walk_tree_task1(root,0)

total = 0
for node in found_nodes:
    total += node.size
print('Task 1 answer:', total)

#Task 2
space_need = 30000000-(70000000-root.size)
if space_need>0:
    walk_tree_task2(root, space_need)
    print('Task 2 answer:', min(found_nodes2, key=lambda item: item.size).size)
