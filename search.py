# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import random
import math

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    #inicializando
    initialstate=problem.getStartState()
    state=util.PriorityQueue()
    visitedstates=[]
    state.push((initialstate,[]),0)
    while not state.isEmpty():
        presentstate,actions=state.pop()

        if problem.isGoalState(presentstate):
            return actions
        
        visitedstates.append(presentstate)
        for successor, action, step_cost in problem.getSuccessors(presentstate):
            if successor not in visitedstates:
                new_action = actions + [action] 
                state.push((successor, new_action), problem.getCostOfActions(new_action))
			
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    queue = util.PriorityQueue() # inicia a fila
    startNode = problem.getStartState() # no inicial
    visitedNodes = [] # inicia array de nos ja visitados vazio
    queue.push((startNode, []), heuristic(startNode,problem)) # insere na fila o no inicial
    
    while not queue.isEmpty():
        state, steps = queue.pop()  # retira da fila Estado atual e Array com Movimentos
        
        if problem.isGoalState(state): # Se chegou no objetivo, retorna array com caminho
            return steps

        visitedNodes.append(state)    
        for successor, step, step_cost in problem.getSuccessors(state): # Todos os sucessores
            if successor not in visitedNodes:
                queue.push((successor, steps + [step]), step_cost + heuristic(successor, problem))
    
    return []

def simulatedAnnealingSearch(problem, heuristic=nullHeuristic):
    iterations = 1000 # numero maximo de iteracoes que o algoritmo ira realizar.
    visitedNodes = [] # nodos ja visitados.
    steps = [] # solucao.
    minimalTemperature = 1
   
    currentNode = (problem.getStartState(),"Stop",0xFFFF) # nodo inicial, caracterizando o estado inicial do sistema.

    for i in range(iterations):

        visitedNodes.append(currentNode) # adiciona o nodo atual a lista de nodos visitados.

        temperature = float(iterations) / float(i+1) # variacao da temperatura.

        if(problem.isGoalState(currentNode)): # se o nodo atual e o estado destino (estado no qual queremos chegar) o algoritmo retorna a solucao.
            return steps

        if(temperature < minimalTemperature): # se a temperatura atual for menor que a temperatura minima o algoritmo para.
            return steps

        neighbors = problem.getSuccessors(currentNode[0]) # lista contendo os vizinhos do nodo atual.

        randomPosition = (random.random()*1000) % len(neighbors) # escolhe um vizinho do nodo atual de forma aleatoria.
        chosenNeighbor = neighbors[int(randomPosition)]

        chosenNeighborCost = heuristic(chosenNeighbor[0], problem) # obtem o custo do nodo vizinho.

        if ((chosenNeighborCost - heuristic(currentNode[0], problem) <= 0) or math.exp(((chosenNeighborCost - heuristic(currentNode[0], problem)) / temperature) >= random.random())): # funcao de aceitacao do nodo para a solucao:
            steps.append(chosenNeighbor[1])                                                                                                                                            # se a variacao entre o nodo atual e o nodo vizinho menor ou igual a zero o nodo e aceito ou,
            currentNode = chosenNeighbor     
                                                                                                                                         # utilizamos a equacao para calcular a probabilidade de aceitacao.
    return steps 

	


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
sas = simulatedAnnealingSearch
