class Dishwasher:
    _instance = None

    def __init__(self, model=None, max_capacity=0, current_capacity=0, is_on=False):
        self.__model = model
        self.__max_capacity = max_capacity
        self.__current_capacity = current_capacity
        self.__is_on = is_on

    @staticmethod
    def get_instance():
        if Dishwasher._instance is None:
            Dishwasher._instance = Dishwasher()
        return Dishwasher._instance

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    def load_dishes(self, count):
        if self.__current_capacity + count <= self.__max_capacity:
            self.__current_capacity += count

    def clean_dishes(self):
        self.__current_capacity = 0

    def __str__(self):
        return (
            f"Dishwasher(model={self.__model}, max_capacity={self.__max_capacity}, "
            f"current_capacity={self.__current_capacity}, is_on={self.__is_on})"
        )


# main method
if __name__ == "__main__":
    dishwashers = [
        Dishwasher(),
        Dishwasher("Model1", 50, 20, True),
        Dishwasher.get_instance(),
        Dishwasher.get_instance(),
    ]

    for dishwasher in dishwashers:
        print(dishwasher)