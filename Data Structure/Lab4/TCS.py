from queueADT import *
from random import randint

class passenger:
    def __init__(self, pID, ArrivalTime):
        self._pID = pID
        self._arrivalTime = ArrivalTime

    # Return id Number
    def getPID(self):
        return self._pID

    # Return Arrival Time
    def timeArrived(self):
        return self._arrivalTime


class TicketAgent:
    def __init__(self, aID):
        self._aID = aID
        self._passenger = None
        self._stopTime = -1

    # Return Id Number
    def getAID(self):
        return self._aID

    # Determine if Agent is Free
    def isFree(self):
        return self._passenger is None

    # Setermine if Agent has finished a Service
    def isFinished(self, CurTime):
        return self._passenger is not None and CurTime == self._stopTime

    # Start Attending to a Passenger
    def startService(self, passenger, stopTime):
        self._passenger = passenger
        self._stopTime = stopTime

    # Stop Service to a Passenger
    def stopService(self):
        thepassenger = self._passenger
        self._passenger = None
        return thepassenger


class TicketCounterSimulation:
    # Create a simulation object
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        # Parameters supplied by user
        self._arriveprob = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes
        self.served = 0

        # Siomulation components.
        self._passengers = CircularQueue()
        self._Agents = [None] * numAgents
        for i in range(numAgents):
            self._Agents[i] = TicketAgent(i+1)

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    #Run the simulation using the parameters supplied
    def run(self):
        for curTime in range(self._numMinutes + 1):
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)
        self.printResult()

    def printResult(self):
        numServed = self._numPassengers - len(self._passengers)
        avgwait = float(self._totalWaitTime) / numServed
        print("")
        print("Number of passengers served ={}".format(numServed))
        print("Number of passengers remaining in line = {}".format(len(self._passengers)))
        print("The average wait time was {:.2f} minutes.".format(avgwait))

    # Handle Customer Arrival
    def _handleArrival(self, curTime):
        prob = randint(0.0, 1.0)
        if (0.0 <= prob) and (prob <= self._arriveprob):
            person = passenger(self._numPassengers + 1, curTime)
            self._passengers.enqueue(person)
            self._numPassengers += 1
            print("Time {}: Passenger {} arrived".format(curTime, person.getPID()))

    def _handleBeginService(self, curTime):
        i = 0
        while i < len(self._Agents):
            if (self._Agents[i].isFree()) and not self._passengers.isEmpty() and (curTime != self._numMinutes):
                passenger = self._passengers.dequeue()
                self.served += 1
                stoptime = curTime + self._serviceTime
                self._Agents[i].startService(passenger, stoptime)
                self._totalWaitTime += (curTime - passenger.timeArrived())
                print("Time {}: Agent {} started serving passenger {}".format(curTime, self._Agents[i].getAID(), passenger.getPID()))
            i += 1

    # Stop Customer Service
    def _handleEndService(self, curTime):
        i = 0
        while i < len(self._Agents):
            if self._Agents[i].isFinished(curTime):
                passenger = self._Agents[i].stopService()
                print("Time {}: Agent {} stopped serving passenger {}".format(curTime, self._Agents[i].getAID(), passenger.getPID()))
            i += 1
