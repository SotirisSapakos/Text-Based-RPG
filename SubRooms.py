import Items


class GenericSubroom:

    """ Generic class for subrooms """

    items = []

    def __init__(self):
        # nothing special to initialize!
        pass


class Subroom1(GenericSubroom):

    def __init__(self):
        super().__init__()

        self.items = [Items.HEALTH_POT,
                      Items.HEALTH_POT]


class Subroom2(GenericSubroom):

    def __init__(self):
        super().__init__()

        self.items = [Items.HEALTH_POT,
                      Items.RECOVERY]


class Subroom3(GenericSubroom):

    def __init__(self):
        super().__init__()

        self.items = [Items.IRON_SWORD,
                      Items.LEATHER_SHIELD]


class Subroom4(GenericSubroom):

    def __init__(self):
        super().__init__()

        self.items = [Items.GRAND_AXE,
                      Items.LONG_BOW]


class Subroom5(GenericSubroom):

    def __init__(self):
        super().__init__()

        self.items = [Items.RECOVERY,
                      Items.SCALE_SHIELD]


class Subroom6(GenericSubroom):

    def __init__(self):
        super().__init__()

        self.items = [Items.HOLY_WATER,
                      Items.HEALTH_POT]
