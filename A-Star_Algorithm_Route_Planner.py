#!/usr/bin/env python
# coding: utf-8

# # Implementing a Route Planner
# In this project you will use A\* search to implement a "Google-maps" style route planning algorithm.

# ## The Map

# In[1]:


# Run this cell first!

from helpers import Map, load_map_10, load_map_40, show_map
import math

get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# ### Map Basics

# In[2]:


map_10 = load_map_10()
show_map(map_10)


# The map above (run the code cell if you don't see it) shows a disconnected network of 10 intersections. The two intersections on the left are connected to each other but they are not connected to the rest of the road network. This map is quite literal in its expression of distance and connectivity. On the graph above, the edge between 2 nodes(intersections) represents a literal straight road not just an abstract connection of 2 cities.
# 
# These `Map` objects have two properties you will want to use to implement A\* search: `intersections` and `roads`
# 
# **Intersections**
# 
# The `intersections` are represented as a dictionary. 
# 
# In this example, there are 10 intersections, each identified by an x,y coordinate. The coordinates are listed below. You can hover over each dot in the map above to see the intersection number.

# In[3]:


map_10.intersections


# **Roads**
# 
# The `roads` property is a list where `roads[i]` contains a list of the intersections that intersection `i` connects to.

# In[4]:


# this shows that intersection 0 connects to intersections 7, 6, and 5
map_10.roads[0] 


# In[5]:


# This shows the full connectivity of the map
map_10.roads


# In[6]:


# map_40 is a bigger map than map_10
map_40 = load_map_40()
show_map(map_40)


# ### Advanced Visualizations
# 
# The map above shows a network of roads which spans 40 different intersections (labeled 0 through 39). 
# 
# The `show_map` function which generated this map also takes a few optional parameters which might be useful for visualizaing the output of the search algorithm you will write.
# 
# * `start` - The "start" node for the search algorithm.
# * `goal`  - The "goal" node.
# * `path`  - An array of integers which corresponds to a valid sequence of intersection visits on the map.

# In[ ]:





# In[7]:


# run this code, note the effect of including the optional
# parameters in the function call.
show_map(map_40, start=5, goal=34, path=[5,16,37,12,34])


# ## The Algorithm
# ### Writing your algorithm
# The algorithm written will be responsible for generating a `path` like the one passed into `show_map` above. In fact, when called with the same map, start and goal, as above you algorithm should produce the path `[5, 16, 37, 12, 34]`. However you must complete several methods before it will work.
# 
# ```bash
# > PathPlanner(map_40, 5, 34).path
# [5, 16, 37, 12, 34]
# ```

# In[8]:


# Do not change this cell
# When you write your methods correctly this cell will execute
# without problems
class PathPlanner():
    """Construct a PathPlanner Object"""
    def __init__(self, M, start=None, goal=None):
        """ """
        self.map = M
        self.start= start
        self.goal = goal
        self.closedSet = self.create_closedSet() if goal != None and start != None else None
        self.openSet = self.create_openSet() if goal != None and start != None else None
        self.cameFrom = self.create_cameFrom() if goal != None and start != None else None
        self.gScore = self.create_gScore() if goal != None and start != None else None
        self.fScore = self.create_fScore() if goal != None and start != None else None
        self.path = self.run_search() if self.map and self.start != None and self.goal != None else None
        
    def get_path(self):
        """ Reconstructs path after search """
        if self.path:
            return self.path 
        else :
            self.run_search()
            return self.path
    
    def reconstruct_path(self, current):
        """ Reconstructs path after search """
        total_path = [current]
        while current in self.cameFrom.keys():
            current = self.cameFrom[current]
            total_path.append(current)
        return total_path
    
    def _reset(self):
        """Private method used to reset the closedSet, openSet, cameFrom, gScore, fScore, and path attributes"""
        self.closedSet = None
        self.openSet = None
        self.cameFrom = None
        self.gScore = None
        self.fScore = None
        self.path = self.run_search() if self.map and self.start and self.goal else None

    def run_search(self):
        """ """
        if self.map == None:
            raise(ValueError, "Must create map before running search. Try running PathPlanner.set_map(start_node)")
        if self.goal == None:
            raise(ValueError, "Must create goal node before running search. Try running PathPlanner.set_goal(start_node)")
        if self.start == None:
            raise(ValueError, "Must create start node before running search. Try running PathPlanner.set_start(start_node)")

        self.closedSet = self.closedSet if self.closedSet != None else self.create_closedSet()
        self.openSet = self.openSet if self.openSet != None else  self.create_openSet()
        self.cameFrom = self.cameFrom if self.cameFrom != None else  self.create_cameFrom()
        self.gScore = self.gScore if self.gScore != None else  self.create_gScore()
        self.fScore = self.fScore if self.fScore != None else  self.create_fScore()

        while not self.is_open_empty():
            current = self.get_current_node()

            if current == self.goal:
                self.path = [x for x in reversed(self.reconstruct_path(current))]
                return self.path
            else:
                self.openSet.remove(current)
                self.closedSet.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor in self.closedSet:
                    continue    # Ignore the neighbor which is already evaluated.

                if not neighbor in self.openSet:    # Discover a new node
                    self.openSet.add(neighbor)
                
                # The distance from start to a neighbor
                #the "dist_between" function may vary as per the solution requirements.
                if self.get_tenative_gScore(current, neighbor) >= self.get_gScore(neighbor):
                    continue        # This is not a better path.

                # This path is the best until now. Record it!
                self.record_best_path_to(current, neighbor)
        print("No Path Found")
        self.path = None
        return False


# Create the following methods:

# In[9]:


def create_closedSet(self):
    """ Creates and returns a data structure suitable to hold the set of nodes already evaluated"""
    # TODO: return a data structure suitable to hold the set of nodes already evaluated   
    return set()


# In[10]:


def create_openSet(self):
    """ Creates and returns a data structure suitable to hold the set of currently discovered nodes 
    that are not evaluated yet. Initially, only the start node is known."""
    if self.start != None:
        # TODO: return a data structure suitable to hold the set of currently discovered nodes 
        # that are not evaluated yet. Make sure to include the start node.      
        openSet = set()        
        openSet.add(self.start)
                
        return openSet
    
    raise(ValueError, "Must create start node before creating an open set. Try running PathPlanner.set_start(start_node)")


# In[11]:


def create_cameFrom(self):
    """Creates and returns a data structure that shows which node can most efficiently be reached from another,
    for each node."""
    # TODO: return a data structure that shows which node can most efficiently be reached from another,
    # for each node. 
    return {}


# In[12]:


def create_gScore(self):
    """Creates and returns a data structure that holds the cost of getting from the start node to that node, for each node.
    The cost of going from start to start is zero."""
    # TODO:  a data structure that holds the cost of getting from the start node to that node, for each node.
    # for each node. The cost of going from start to start is zero. The rest of the node's values should be set to infinity.
    gscore = {}
    for i in range(len(self.map.intersections)):
        #Outside References:https://stackoverflow.com/questions/7781260/how-can-i-represent-an-infinite-number-in-python
        #Outside References:https://stackoverflow.com/questions/5438745/is-it-possible-to-set-a-number-to-nan-or-infinity?rq=1
        #Outside References:https://medium.com/@sanatinia/how-to-work-with-infinity-in-python-337fb3987f06        
        #gscore[i]=float('inf')
        gscore[i]=math.inf
    gscore[self.start]=0    
    return gscore
        


# In[13]:


def create_fScore(self):
    """Creates and returns a data structure that holds the total cost of getting from the start node to the goal
    by passing by that node, for each node. That value is partly known, partly heuristic.
    For the first node, that value is completely heuristic."""
    # TODO:  a data structure that holds the total cost of getting from the start node to the goal
    # by passing by that node, for each node. That value is partly known, partly heuristic.
    # For the first node, that value is completely heuristic. The rest of the node's value should be 
    # set to infinity.
    fscore={}
    for i in range(len(self.map.intersections)):
        #Outside References:https://stackoverflow.com/questions/7781260/how-can-i-represent-an-infinite-number-in-python
        #Outside References:https://stackoverflow.com/questions/5438745/is-it-possible-to-set-a-number-to-nan-or-infinity?rq=1
        #Outside References:https://medium.com/@sanatinia/how-to-work-with-infinity-in-python-337fb3987f06
        fscore[i]=math.inf
        #fcore[i]=float('inf')
    fscore[self.start]=self.heuristic_cost_estimate(self.start)
    return fscore


# In[14]:


def set_map(self, M):
    """Method used to set map attribute """
    self._reset(self)
    self.start = None
    self.goal = None
    # TODO: Set map to new value. 
    self.map = M


# In[15]:


def set_start(self, start):
    """Method used to set start attribute """
    self._reset(self)
    # TODO: Set start value. Remember to remove goal, closedSet, openSet, cameFrom, gScore, fScore, 
    # and path attributes' values.
    self.start = start
    self.goal = None
    self.closedSet= None
    self.openSet= None
    self.cameFrom= None
    self.gScore= None
    self.fScore= None
    self.path= None
    
    


# In[16]:


def set_goal(self, goal):
    """Method used to set goal attribute """
    self._reset(self)
    # TODO: Set goal value. 
    self.goal = goal


# In[17]:


def get_current_node(self):
    """ Returns the node in the open set with the lowest value of f(node)."""
    # TODO: Return the node in the open set with the lowest value of f(node).
    intersections_fscores ={}
    for node in self.openSet:
        intersections_fscores[node]=self.calculate_fscore(node)
        
    #Outside References:https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-15.php
    #Outside References:http://www.aroseartist.com/python-dictionary-max-min/
    #return min(intersections_fscores.keys(), key=(lambda k: intersections_fscores[k]))
    
    #Outside References : https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary
    return min(intersections_fscores,key=intersections_fscores.get)
        


# In[18]:


def get_neighbors(self, node):
    """Returns the neighbors of a node"""
    # TODO: Return the neighbors of a node
    return set(self.map.roads[node])


# In[19]:


def get_gScore(self, node):
    """Returns the g Score of a node"""
    # TODO: Return the g Score of a node
    return self.gScore[node]


# In[20]:


def get_tenative_gScore(self, current, neighbor):
    """Returns the tenative g Score of a node"""
    # TODO: Return the g Score of the current node 
    # plus distance from the current node to it's neighbors
    return (self.get_gScore(current)+ self.distance(current,neighbor))


# In[21]:


def is_open_empty(self):
    """returns True if the open set is empty. False otherwise. """
    # TODO: Return True if the open set is empty. False otherwise.
    if len(self.openSet)==0:
        return True
    else:
        return False
    


# In[22]:


def distance(self, node_1, node_2):
    """ Computes the Euclidean L2 Distance"""
    # TODO: Compute and return the Euclidean L2 Distance
    #outside references: https://brilliant.org/wiki/a-star-search/ [(the Euclidean Distance Heuristic Section)]
    return math.sqrt(math.pow(self.map.intersections[node_1][0]-self.map.intersections[node_2][0],2) + math.pow(self.map.intersections[node_1][1]-self.map.intersections[node_2][1],2))


# In[23]:


def heuristic_cost_estimate(self, node):
    """ Returns the heuristic cost estimate of a node """
    # TODO: Return the heuristic cost estimate of a node
    return self.distance(node,self.goal)


# In[24]:


def calculate_fscore(self, node):
    """Calculate the f score of a node. """
    # TODO: Calculate and returns the f score of a node. 
    # REMEMBER F = G + H
    return (self.get_gScore(node) + self.heuristic_cost_estimate(node))


# In[25]:


def record_best_path_to(self, current, neighbor):
    """Record the best path to a node """
    # TODO: Record the best path to a node, by updating cameFrom, gScore, and fScore
    self.cameFrom[neighbor]=current
    self.gScore[neighbor]=self.get_tenative_gScore(current,neighbor)
    self.fScore[current]=self.calculate_fscore(current)


# In[26]:


def _reset(self):
        """Private method used to reset the closedSet, openSet, cameFrom, gScore, fScore, and path attributes"""
        self.closedSet = None
        self.openSet = None
        self.cameFrom = None
        self.gScore = None
        self.fScore = None
        self.path = self.run_search() if self.map and self.start and self.goal else None


# In[27]:


PathPlanner.create_closedSet = create_closedSet
PathPlanner.create_openSet = create_openSet
PathPlanner.create_cameFrom = create_cameFrom
PathPlanner.create_gScore = create_gScore
PathPlanner.create_fScore = create_fScore
PathPlanner._reset = _reset
PathPlanner.set_map = set_map
PathPlanner.set_start = set_start
PathPlanner.set_goal = set_goal
PathPlanner.get_current_node = get_current_node
PathPlanner.get_neighbors = get_neighbors
PathPlanner.get_gScore = get_gScore
PathPlanner.get_tenative_gScore = get_tenative_gScore
PathPlanner.is_open_empty = is_open_empty
PathPlanner.distance = distance
PathPlanner.heuristic_cost_estimate = heuristic_cost_estimate
PathPlanner.calculate_fscore = calculate_fscore
PathPlanner.record_best_path_to = record_best_path_to


# In[28]:


planner = PathPlanner(map_40, 5, 34)
path = planner.path
if path == [5, 16, 37, 12, 34]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)


# In[29]:


show_map(map_40, start=5, goal=34, path=[5,16,37,12,34])


# ### Testing your Code
# If the code below produces no errors, your algorithm is behaving correctly. You are almost ready to submit! Before you submit, go through the following submission checklist:
# 
# **Submission Checklist**
# 
# 1. Does my code pass all tests?
# 2. Does my code implement `A*` search and not some other search algorithm?
# 3. Do I use an **admissible heuristic** to direct search efforts towards the goal?
# 4. Do I use data structures which avoid unnecessarily slow lookups?
# 
# When you can answer "yes" to all of these questions, submit by pressing the Submit button in the lower right!

# In[30]:


from test import test

test(PathPlanner)


# ## Questions
# 
# **Instructions**  Answer the following questions in your own words. We do not you expect you to know all of this knowledge on the top of your head. We expect you to do research and ask question. However do not merely copy and paste the answer from a google or stackoverflow. Read the information and understand it first. Then use your own words to explain the answer.

# - How would you explain A-Star to a family member(layman)?
# 
# ** ANSWER **:Lets Suppose a person has to catch a flight and hence needs to reach airport as soon as possible from his/her place of residence.Due to construction work going on , some areas directly between the residence and airport are facing heavy traffic.Even though a cab navigating the roads in these areas would have to travel the shortest distance to reach airport, due to heavy traffic the said person would never be able to reach in time to catch flight. However there are adjacent areas which are very less congested with traffic and hence navigating the cab through these localities would amount to taking a longer route but significantly less time to reach the airport. 
# The A-Star Algorithm is a path-finding algorithm between 2 points(from start point to Destination) which helps the navigator to take the shortest possible route to reach the destination in least amount of time 

# - How does A-Star search algorithm differ from Uniform cost search? What about Best First search?
# 
# ** ANSWER **:Uniform Cost search algorithm such as Dijkstra Algorithm always expands nodes with least cost in all directions without taking into consideration whether the new nodes getting expanded are closer to the final destination/goal. Best First Search algorithms expand nodes which are at shortest distance from the final goal. A-Star alogrithm while exploring new frontier nodes takes into account both the conditions of the new nodes in frontier section having minimum cost and also that the new nodes are closer to the goal to be reached thus doing away with the need to exploring new nodes which are away/ not in direction of the final destination as is the case in Uniform Cost Search(Dijkstra's) algorithm . A-Star implements this by taking into consideration a Heuristic function along with the Cost function to calculate the total cost function at each state in course of exploring new nodes during algorithm implementation .

# - What is a heuristic?
# 
# ** ANSWER **: A heuristic or a heuristic function is used to calculate the estimated cost of a function based on which decisions can be made to follow a branch with least estimated cost . The Estimated cost is not accurately the true cost but serves an intuitive compass to make the most appropriate decision based on available information when there are many alternatives/branches to consider at a given time.

# - What is a consistent heuristic?
# 
# ** ANSWER **:A heuristic is consistent if the summation of cost from current node to a successor node(neighbour) and the estimated cost from the successor node(neighbour) to goal is less than or equal to the estimated cost from the current node to the goal .
# 
# hScore(current,goal) <= gScore(current,neighbour) + hScore(neighbour,goal) 
# 
# where =>
# 
# a) gScore:Cost
# b) hScore:Estimated Cost/Heuristic (Euclidean distance)
# 

# - What is a admissible heuristic? 
# 
# ** ANSWER **:A Heuristic is admissible if the estimated cost from Current Node to Goal is never more than the Actual Cost from Current Node to Goal. An admissible Heuristic never overestimates the cost of reaching the goal.
# 
# For e.g. suppose there is a map with 2 routes connected in the form of the two non-hypotenuse edges of a right-angled triangle.
# 
# With the extreme Vertices A and C being the Start and Goal locations respectively.
# 
# Here the Estimated Cost (A->C) i.e. the length of Hypotenuse would always be less than the acutal cost (A->B->C) i.e. the sum of the lengths of other 2 sides of the right-angled triangle

# - ___ admissible heuristic are consistent.
# *CHOOSE ONE*
#     - All
#     - Some
#     - None
#     
# ** ANSWER **:Some

# - ___ Consistent heuristic are admissible.
# *CHOOSE ONE*
#     - All
#     - Some
#     - None
#     
# ** ANSWER **:All

# In[ ]:




