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

def clear_screen():
    if os.name == 'nts': 
        os.system('cls')
    else:
        os.system('clear')

def menu(g):
    while True:
        clear_screen()
        global flag
        print('                          Menu                      ')
        print('1.) Add edge........................................')
        print('2.) vertex minimun and maximun degree......................')
        print('3.) Visualize.......................................')
        print('4.) Quit ...........................................')
        choice = int(input('Answer: '))
        if choice == 1:
            for i in range(g.size):
                for j in range(g.size):
                    n = int(input(f'Do vertices {i} and {j} are adjacents? 1/0 '))
                    if n == 1:
                        g.add_edge(i,j)
                flag = True
            input('press any key to continue...')
        elif choice == 2:
            if not flag:
                print('please add edge first')
                for i in range(g.size):
                    for j in range(g.size):
                        n = int(input(f'Do vertices {i} and {j} are adjacents? 1/0 '))
                        if n == 1:
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
            import sys
            sys.exit()
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