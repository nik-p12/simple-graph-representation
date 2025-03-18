# Graphes en Python

## Description

Ce projet implémente une structure de données de **graphe non orienté** à l'aide d'une matrice d'adjacence. L'objectif est de permettre à l'utilisateur de créer un graphe, d'ajouter des arêtes entre des sommets, et d'obtenir diverses informations sur le graphe, telles que les degrés des sommets, ainsi que de visualiser le graphe sous forme graphique ou matricielle.

## Logique de Manipulation des Graphes

### 1. **Représentation du Graphe avec une Matrice d'Adjacence**

Le graphe est **représenté à l'aide d'une matrice d'adjacence**. Une matrice d'adjacence est une matrice carrée où chaque ligne et chaque colonne correspond à un sommet du graphe. Si une arête existe entre les sommets `u` et `v`, la valeur à la position `matrix[u][v]` est différente de zéro (par défaut `1` dans ce projet). Comme le graphe est **non orienté**, une arête entre `u` et `v` implique également que `matrix[v][u]` est égal à `1`.

### 2. **Ajout d'Arêtes**

Lors de l'ajout d'une arête entre deux sommets `u` et `v`, la fonction `add_edge()` met à jour la matrice d'adjacence aux positions appropriées. Pour un graphe non orienté, l'arête est ajoutée à la fois à `matrix[u][v]` et `matrix[v][u]`.

```python
def add_edge(self, u, v, weight=1):
    self.matrix[u][v] = weight
    self.matrix[v][u] = weight
```

Cela garantit que la relation entre les sommets est symétrique, ce qui est caractéristique d'un graphe non orienté.

### 3. **Calcul des Degrés des Sommets**

Un **degré** d'un sommet est défini comme le nombre d'arêtes qui y sont connectées. Pour calculer les degrés minimum et maximum dans le graphe, nous parcourons chaque ligne de la matrice d'adjacence et calculons la somme des éléments dans chaque ligne. Cette somme représente le degré d'un sommet donné.

```python
min_deg = min(sum(row) for row in self.matrix)
max_deg = max(sum(row) for row in self.matrix)
```

Cette logique permet de calculer efficacement les degrés des sommets et de trouver le **degré minimum et maximum** dans le graphe.

### 4. **Visualisation du Graphe**

Le projet permet de visualiser le graphe sous deux formes :

- **Représentation graphique** : Utilisation de `networkx` et `matplotlib` pour afficher le graphe de manière visuelle. Les arêtes sont tracées entre les sommets, et les sommets sont étiquetés pour permettre une identification facile.
  
- **Représentation matricielle** : Affichage de la matrice d'adjacence sous forme de tableau dans la console, permettant à l'utilisateur de voir les connexions entre les sommets sous une forme plus brute.

Voici comment la logique fonctionne pour la visualisation graphique :
  
1. **Extraire les arêtes** : Nous parcourons la matrice d'adjacence et extrayons les paires de sommets qui sont connectés par une arête (c'est-à-dire lorsque la valeur dans la matrice est différente de zéro).
  
```python
edges = [(i, j) for i in range(self.size) for j in range(i + 1, self.size) if self.matrix[i][j] > 0]
```

2. **Affichage avec `networkx`** : Les arêtes extraites sont ajoutées à un objet `Graph` de `networkx`, qui génère ensuite le graphe et l'affiche.

```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from(edges)
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='black', node_size=2000, font_size=15)
plt.show()
```

### 5. **Interface Utilisateur (Menu Interactif)**

L'utilisateur interagit avec le programme via un **menu interactif** qui permet :

1. D'ajouter des arêtes au graphe en précisant si deux sommets sont adjacents.
2. D'obtenir les degrés minimum et maximum des sommets.
3. De visualiser le graphe soit sous forme graphique soit sous forme de matrice d'adjacence.
4. De quitter l'application.

Chaque option du menu est implémentée dans une fonction distincte, et l'utilisateur peut effectuer plusieurs actions avant de quitter.

---

## Dépendances

Le projet utilise les bibliothèques suivantes pour fonctionner :

- **`networkx`** : Pour la création et la manipulation de graphes.
- **`matplotlib`** : Pour la visualisation graphique du graphe.
- **`numpy`** : Pour la manipulation de tableaux et matrices.

## Fonctionnalités à venir

- **Ajout d'autres algorithmes de graphes** : Recherche de chemin, algorithmes de traversal, etc.
- **Support des graphes dirigés** : Actuellement, le projet ne prend en charge que les graphes non orientés, mais des extensions pourraient être ajoutées pour inclure des graphes dirigés.

 