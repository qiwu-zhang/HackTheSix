class Financial_Data:
    def __init__(self, food=0, housing=0, misc=0, income=0):
        self.food=food
        self.housing = housing
        self.misc = misc
        self.income = income
        self.totalExpenses = self.food+self.housing+self.misc
        