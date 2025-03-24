import os

class Graph: 
    def __init__(self, size):
        self.size = size
        self.matrix = [[0]* size for _ in range(size)]

    def add_edge(self, u, v, weight = 1):
        self.matrix[u][v] = weight
        self.matrix[v][u] = weight

    def display(self):
        for row in self.matrix:
            print(row)

def dfs(g, u, v, path, visited):
    visited[u] = True 
    path.append(u)
    if u == v:
        return True
    for i in range(len(g.matrix[u])):
        if g.matrix[u][i] == 1 and not visited[i]:
            if dfs(g, i, v, path, visited):
                return True
    path.pop()
    visited[u] = False

def dfs_elementary_matrix(h, current, target, path):
    if current == target: 
        return True
    for neighbor in range(len(h.matrix[current])):
        if h.matrix[current][neighbor] > 0:
            h.matrix[current][neighbor] -=1
            h.matrix[neighbor][current] -=1
            path.append(neighbor)
            if dfs_elementary_matrix(h, neighbor, target, path):
                return True
        h.matrix[current][neighbor] +=1
        h.matrix[neighbor][current] +=1
        path.pop()
    return False

def exists_chain(g, u, v):
    path = list()
    visited = [False]*g.size
    return dfs(g, u, v, path, visited)

def is_simple_graph(g):
    if any(g.matrix[i][i] != 0 for i in range(g.size)):
        return False
    return max(max(line) for line in g.matrix) == 1
    
def exist_elementary_chain(g,u,v):
    if is_simple_graph(g):
        print(f"an elementary chain exists between the vertices {u} and {v} as a consequence of the fact that g is a simple graph and that a chain exists between these vertices "if exists_chain(g, u, v) else "there is no chain between the vertices {u} and {v}")
    else:
        h = g
        path = list()
        print(f"an elementary chain exists between the vertices {u} and {v}" if dfs_elementary_matrix(h, u, v, path) else "there is no chain between the vertices {u} and {v}")

def clear_screen():
    if os.name == 'nt': 
        os.system('cls')
    else:
        os.system('clear')

def menu(g):
    while True:
        clear_screen()
        global flag
        print('                               Menu                              ')
        print('1.) Add edge.....................................................')
        print('2.) vertex minimun and maximun degree............................')
        print('3.) Visualize....................................................')
        print("4.) Check if there's a elementary chain between two vertices.......")
        print('5.) Quit ........................................................')
        choice = int(input('Answer: '))
        if choice == 1:
            for i in range(g.size):
                for j in range(g.size):
                    n = int(input(f'please enter the number of aretes between {i} and {j}, 0 if not adjacent: '))
                    if n > 0:
                        g.add_edge(i,j)
                flag = True
            input('press any key to continue...')
        elif choice == 2:
            if not flag:
                print('please add edge first')
                for i in range(g.size):
                    for j in range(g.size):
                        n = int(input(f'please enter the number of aretes between {i} and {j}, 0 if not adjacent: '))
                        if n > 0:
                            g.add_edge(i,j)
            sums = [sum(ligne) for ligne in g.matrix]
            min_sum = min(sums)
            max_sum = max(sums)
            min_deg = sums.index(min_sum)
            max_deg = sums.index(max_sum)
            print(f'vertex with Min degree is vertex ({min_deg}) and vertex with max degree is ({max_deg})')
            input('press any key to continue')
        elif choice == 3:
            clear_screen()
            print(' 1.) Ui representatition .........')
            print(' 2.) Matrix representation .......')
            c = int(input('choice: '))
            if c == 1:
                import networkx as nx
                import matplotlib.pyplot as plt
                G = nx.Graph()
                edges = [(i, j) for i in range(g.size) for j in range(i+1, g.size) if g.matrix[i][j] > 0]
                G.add_edges_from(edges)
                nx.draw(G, with_labels=True, node_color='lightblue', edge_color='black', node_size=2000, font_size=15)
                plt.show()
            elif c == 2:
                g.display()
                input('press any key to continue ...')
            else:
                print('invalid input')
                input('press any key to continue ...')
        elif choice == 4:
            u,v = map(int, input("Enter the two vertices seperate by a space (eg: 1 2)").split())
            exists_elementary_chain(g, u, v)
        elif choice == 5:
            print("Exiting program...")
            break
        else:
            print('invalid choice, please retry ...')
            input('press any key to continue ...')

def main():
    size = int(input('please enter the number of verges: '))
    g = Graph(size)
    menu(g)

def install_missing_packages():
    import sys
    import subprocess
    import pkg_resources
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    missing_packages = [pkg for pkg in dependencies if pkg not in installed_packages]

    if missing_packages:
        print(f"installation of missing dependencies : {missing_packages}")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", *missing_packages])
            print("dependencies succesfull installed")
        except Exception as e:
            print(f"Error in installing dependencies : {e}")
            sys.exit(1)
dependencies = [ 
    "matplotlib",
    "networkx"
]
install_missing_packages()
flag = False
main()
