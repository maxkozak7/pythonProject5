from abc import ABC, abstractmethod


class Dishwasher(ABC):
    def __init__(self, max_capacity=0, current_capacity=0, power_consumption_per_cycle=0):
        self._max_capacity = max_capacity
        self._current_capacity = current_capacity
        self._power_consumption_per_cycle = power_consumption_per_cycle

    @abstractmethod
    def getPowerConsumptionPerCycle(self):
        pass

    def __str__(self):
        return f"Dishwasher(max_capacity={self._max_capacity}, current_capacity={self._current_capacity}, power_consumption_per_cycle={self._power_consumption_per_cycle})"