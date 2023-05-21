from models import ConsumerDishwasher, ClinicalDishwasher, IndustrialDishwasher, CompactDishwasher


class DishwasherManager:
    def __init__(self):
        self.dishwashers = []

    def addDishwasher(self, dishwasher):
        self.dishwashers.append(dishwasher)

    def findAllWithPowerGreaterThan(self, power):
        return list(filter(lambda d: d.getPowerConsumptionPerCycle() > power, self.dishwashers))

    def findIndustrialDishwashers(self):
        return list(filter(lambda d: isinstance(d, IndustrialDishwasher.IndustrialDishwasher), self.dishwashers))

    def findCompactDishwashers(self):
        return list(filter(lambda d: isinstance(d, CompactDishwasher.CompactDishwasher), self.dishwashers))


def main():
    dishwasher_manager = DishwasherManager()

    consumer_dishwasher1 = ConsumerDishwasher.ConsumerDishwasher(max_capacity=10, current_capacity=5, volume=2, power=1, sterilization_duration=30)
    consumer_dishwasher2 = ConsumerDishwasher.ConsumerDishwasher(max_capacity=8, current_capacity=4, volume=1.5, power=1.2, sterilization_duration=25)

    clinical_dishwasher1 = ClinicalDishwasher.ClinicalDishwasher(max_capacity=20, current_capacity=10, max_temperature=80, volume=4, power=2, sterilization_duration=40)
    clinical_dishwasher2 = ClinicalDishwasher.ClinicalDishwasher(max_capacity=15, current_capacity=7, max_temperature=85, volume=3.5, power=2.5, sterilization_duration=35)

    industrial_dishwasher1 = IndustrialDishwasher.IndustrialDishwasher(max_capacity=100, current_capacity=50, power=10, wash_duration=60)
    industrial_dishwasher2 = IndustrialDishwasher.IndustrialDishwasher(max_capacity=150, current_capacity=75, power=12, wash_duration=75)

    compact_dishwasher1 = CompactDishwasher.CompactDishwasher(max_capacity=30, current_capacity=15, power=6, wash_duration=30)
    compact_dishwasher2 = CompactDishwasher.CompactDishwasher(max_capacity=40, current_capacity=20, power=8, wash_duration=40)

    dishwasher_manager.addDishwasher(consumer_dishwasher1)
    dishwasher_manager.addDishwasher(consumer_dishwasher2)
    dishwasher_manager.addDishwasher(clinical_dishwasher1)
    dishwasher_manager.addDishwasher(clinical_dishwasher2)
    dishwasher_manager.addDishwasher(industrial_dishwasher1)
    dishwasher_manager.addDishwasher(industrial_dishwasher2)
    dishwasher_manager.addDishwasher(compact_dishwasher1)
    dishwasher_manager.addDishwasher(compact_dishwasher2)

    print("All dishwashers:")
    for dishwasher in dishwasher_manager.dishwashers:
        print(dishwasher)

    print("\nIndustrial dishwashers:")
    for dishwasher in dishwasher_manager.findIndustrialDishwashers():
        print(dishwasher)

    print("\nCompact dishwashers:")
    for dishwasher in dishwasher_manager.findCompactDishwashers():
        print(dishwasher)

    print("\nDishwashers with power consumption per cycle greater than 2 kW/h:")
    for dishwasher in dishwasher_manager.findAllWithPowerGreaterThan(2):
        print(dishwasher)


if __name__ == "__main__":
    main()







