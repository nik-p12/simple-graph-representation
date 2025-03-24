# **Implemetation des Graphes en Python**  

## **Description**  

Ce projet implémente une structure de **graphe non orienté** à l'aide d'une **matrice d'adjacence**. Il permet d'ajouter des arêtes entre des sommets, de déterminer les sommets ayant le **degré minimum et maximum**, et de visualiser le graphe sous forme **graphique** ou **matricielle**.  

## **Fonctionnalités**  

1. **Création d'un graphe** basé sur une matrice d'adjacence.  
2. **Ajout d'arêtes** entre les sommets via un menu interactif.  
3. **Détection des erreurs** :  
   - Vérification qu'il n'y a **pas plus d'une arête** entre deux sommets.  
   - Vérification qu'**aucune boucle** n'est présente (la diagonale de la matrice doit être nulle).  
4. **Détermination des sommets ayant le degré minimum et maximum**.  
5. **Affichage du graphe** sous deux formes :  
   - **Graphique** avec `networkx` et `matplotlib`.  
   - **Matrice d'adjacence** affichée dans la console.  
6. **Interface utilisateur interactive** avec un menu permettant d'interagir avec le graphe.  

---

## **1. Représentation du Graphe**  

Le graphe est représenté sous forme d'une **matrice d'adjacence** où :  
- `matrix[u][v] = 1` signifie qu'il existe une arête entre les sommets `u` et `v`.  
- Puisque le graphe est **non orienté**, nous avons aussi `matrix[v][u] = 1`.  

### **Vérification de la validité du graphe**  

Avant d'ajouter une arête, nous effectuons les vérifications suivantes :  

1. **Pas plus d'une arête entre deux sommets**  
   ```python
   if max(max(line) for line in g.matrix) > 1:
       print("Erreur : Il ne peut y avoir qu'une seule arête entre deux sommets.")
   ```  

2. **Aucune boucle (pas d'arêtes entre un sommet et lui-même)**  
   ```python
   if any(g.matrix[i][i] != 0 for i in range(g.size)):
       print("Erreur : Un sommet ne peut pas être connecté à lui-même.")
   ```  

---

## **2. Ajout d'Arêtes**  

L'utilisateur peut **ajouter des arêtes** via le menu interactif en répondant `1` (oui) ou `0` (non) lorsqu'on lui demande si deux sommets sont adjacents.

---

## **3. Détermination des Sommets de Degré Minimum et Maximum**  

Le **degré d'un sommet** correspond au nombre d'arêtes qui lui sont connectées.  
Nous **déterminons les sommets ayant le degré minimum et maximum** avec :  

```python
sums = [sum(row) for row in g.matrix]
min_deg_vertex, max_deg_vertex = sums.index(min(sums)), sums.index(max(sums))
print(f'Sommet avec degré minimum : {min_deg_vertex}, Sommet avec degré maximum : {max_deg_vertex}')
```  

---

## **4. Visualisation du Graphe**  

Le graphe peut être affiché sous deux formes :  

### **A. Représentation Graphique avec `networkx`**  

1. Extraction des arêtes depuis la matrice d'adjacence :  
   ```python
   edges = [(i, j) for i in range(g.size) for j in range(i+1, g.size) if g.matrix[i][j] > 0]
   ```  

2. Affichage avec `networkx` et `matplotlib` :  
   ```python
   import networkx as nx
   import matplotlib.pyplot as plt

   G = nx.Graph()
   G.add_edges_from(edges)
   nx.draw(G, with_labels=True, node_color='lightblue', edge_color='black', node_size=2000, font_size=15)
   plt.show()
   ```  

### **B. Représentation sous forme de Matrice**  

Affichage direct dans la console :  
```python
def display(self):
    for row in self.matrix:
        print(row)
```  

---

## **5. Trace de l'Algorithme**  

Une **trace d'algorithme** est une représentation détaillée de l'exécution du programme étape par étape. Elle permet de **comprendre le fonctionnement** et de **déboguer le code**.  

### **A. Trace Manuelle**  
On suit l'évolution des variables dans un tableau.  

#### **Exemple : Ajout d'une arête entre deux sommets**  

Si nous avons un graphe avec 4 sommets (`0, 1, 2, 3`) et ajoutons une arête entre `0` et `2`, la trace pourrait être :  

| Étape | Sommet `u` | Sommet `v` | Matrice d'adjacence mise à jour |
|-------|-----------|-----------|--------------------------------|
| 1     | 0         | 2         | `matrix[0][2] = 1` et `matrix[2][0] = 1` |
| 2     | 1         | 3         | `matrix[1][3] = 1` et `matrix[3][1] = 1` |  

### **B. Trace avec Affichage `print()`**  
On peut ajouter des `print()` dans le code pour suivre son exécution.  

#### **Exemple en Python :**  
```python
def add_edge(self, u, v, weight=1):
    print(f"Ajout d'une arête entre {u} et {v}")
    self.matrix[u][v] = weight
    self.matrix[v][u] = weight
    print(f"Matrice mise à jour : {self.matrix}")
```  

Sortie lors de l'exécution :  
```
Ajout d'une arête entre 0 et 2
Matrice mise à jour : [[0, 0, 1, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]
```  

### **C. Trace avec un Débogueur (`pdb`)**  
On peut utiliser **`pdb`** pour exécuter le programme ligne par ligne et observer les variables.  

```python
import pdb

def add_edge(self, u, v, weight=1):
    pdb.set_trace()  # Mettre un point d'arrêt
    self.matrix[u][v] = weight
    self.matrix[v][u] = weight
```  

Lors de l'exécution, on peut utiliser :  
- `n` pour exécuter l'instruction suivante.  
- `p self.matrix` pour voir l'état actuel de la matrice.  

---

## **6. Installation Automatique des Dépendances**  

Avant l'exécution, le programme vérifie et installe automatiquement les bibliothèques **`networkx`** et **`matplotlib`** si elles ne sont pas présentes.  

---

## **7. Lancement du Programme**  

Lancer le programme avec :  

```python
def main():
    size = int(input('Enter the number of vertices: '))
    g = Graph(size)
    menu(g)

install_missing_packages()
main()
```  

---

## **8. Fonctionnalités Futures**  

- Ajout d'algorithmes comme **BFS**, **DFS** et **Dijkstra**.  
- Support des **graphes dirigés**.  

---