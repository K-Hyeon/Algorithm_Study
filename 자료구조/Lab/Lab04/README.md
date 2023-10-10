<h1 align="center">Queue Abstract Data Type</h1>

## Task1. Implement Deque Data Structure
#### Deque or Double Ended Queue is a generalized version of Queue data structure that allows insert and delete at both ends. Write code for Deque abstract data type and test it.
- addFront(): Adds an item at the front of Deque. 
- addRear(): Adds an item at the rear of Deque. 
- deleteFront(): Deletes an item from front of Deque. 
- deleteRear(): Deletes an item from rear of Deque. 
- getFront(): Gets the front item from queue. 
- getRear(): Gets the last item from queue. 
- isEmpty(): Checks whether Deque is empty or not. 
- isFull(): Checks whether Deque is full or not.
<div align="center">
  <img src="https://github.com/K-Hyeon/Algorithm_Study/assets/63723227/8c197137-6262-4766-8e6b-301c99cf27b6" alt="image">
</div>

## Task2. Ticketing Counter system (Simulation)
#### A computer simulation can be developed to model this Ticketing Counter system using the Queue data structure. 
- CircularQueue : Data structure to hold the passengers.
- Passenger : store info related to a passenger.
- TicketAgent : store info related to an agent.
- TicketCounterSimulation : manages the actual simulation.

## Task3. Solve the Maze problem through DFS and BFS using different data structures
#### A Maze is given as N×N binary matrix of blocks where source block is maze[0][0] and destination block is maze[N-1][N-1].
- DFS1() : It searches maze using stack from CircularDeque (front end operations)
- DFS2() : It searches maze using Stack
- DFS1() : It searches maze using stack from CircularDeque (rear end operation)
- BFS1() : It searches maze using Queue from CircularDeque
- BFS2() : It searches maze using Queue from CircularQueue
<div align="center">
  <img src="https://github.com/K-Hyeon/Algorithm_Study/assets/63723227/a0867c20-059a-48ca-a184-c4bf6f2d7aba" alt="image">
  <img src="https://github.com/K-Hyeon/Algorithm_Study/assets/63723227/a8913bcb-b8b7-4425-ad34-3365cedbfdbe" alt="image">
</div>
