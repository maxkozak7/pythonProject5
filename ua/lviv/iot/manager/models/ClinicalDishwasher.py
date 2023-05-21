from ua.lviv.iot.manager.models.Dishwasher import Dishwasher


class ClinicalDishwasher(Dishwasher):
    def __init__(self, max_capacity=0, current_capacity=0, max_temperature=0, volume=0, power=0, sterilization_duration=0):
        super().__init__(max_capacity, current_capacity)
        self._max_temperature = max_temperature
        self._volume = volume
        self._power = power
        self._sterilization_duration = sterilization_duration

    def getPowerConsumptionPerCycle(self):
        return self._power

    def __str__(self):
        return (
            f"ClinicalDishwasher(max_capacity={self._max_capacity}, current_capacity={self._current_capacity}, "
            f"max_temperature={self._max_temperature}, volume={self._volume}, power={self._power}, "
            f"sterilization_duration={self._sterilization_duration})"
        )