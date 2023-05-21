from ua.lviv.iot.manager.models.Dishwasher import Dishwasher


class IndustrialDishwasher(Dishwasher):
    def __init__(self, max_capacity=0, current_capacity=0, power=0, wash_duration=0):
        super().__init__(max_capacity, current_capacity)
        self._power = power
        self._wash_duration = wash_duration

    def getPowerConsumptionPerCycle(self):
        return self._power

    def __str__(self):
        return (
            f"IndustrialDishwasher(max_capacity={self._max_capacity}, current_capacity={self._current_capacity}, "
            f"power={self._power} kW/h, wash_duration={self._wash_duration} minutes)"
        )