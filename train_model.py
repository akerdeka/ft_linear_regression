import csv
import matplotlib.pyplot as plt

class LinearRegression:

    def __init__(self) -> None:
        self.theta0 = 1
        self.theta1 = 1
        self.global_cost = 0
        self.Ratio = 0.1
        self.m = 0
        self.max_x, self.min_x = 0, 0
        self.max_y, self.min_y = 0, 0
        self.price = []
        self.mileage = []
        self.rows = []

    def PrixEstime(self, kilometrage):
        return self.theta0 + (self.theta1 * kilometrage)

    def Parse(self):
        file = open("data.csv")
        csvreader = csv.reader(file)

        for row in csvreader:
            if (row[0] != 'km'):
                self.rows.append([float(row[0]) / 100000, float(row[1]) / 100000])
                self.mileage.append(float(row[0]))
                self.price.append(float(row[1]))
                if float(row[0]) > self.max_x:
                    self.max_x = float(row[0])
                if float(row[1]) < self.max_y:
                    self.max_y = float(row[1])
            self.m += 1

    def GetMaxMin(self):
        self.min_x = self.max_x
        self.min_y = self.max_y
        for row in self.rows:
            if row[0] < self.min_x:
                self.min_x = float(row[0])
            if row[1] < self.min_y:
                self.min_y = float(row[1])
        self.min_x *= 100000

    def LinearReg(self):
        for j in range(1000):
            self.sum0 = 0
            self.sum1 = 0
            for i in range(self.m -1):
                self.sum0 += self.PrixEstime(self.rows[i][0]) - self.rows[i][1]
                self.sum1 += (self.PrixEstime(self.rows[i][0]) - self.rows[i][1]) * self.rows[i][0]
            self.theta0 -= self.Ratio * (1/(self.m)) * self.sum0
            self.theta1 -= self.Ratio * (1/(self.m)) * self.sum1
        self.theta0 *= 100000

    def Show(self):
        plt.plot(self.mileage , self.price, '+', [self.min_x, self.max_x], [self.PrixEstime(self.min_x), self.PrixEstime(self.max_x)])
        plt.ylabel('self.price')
        plt.xlabel('self.mileage')
        plt.savefig("linear_regression.png")

    def SaveDatas(self):
        data = open("data.txt", "w")
        data.write("{0} {1}".format(self.theta0, self.theta1))
        data.close()

LR = LinearRegression()
LR.Parse()
LR.GetMaxMin()
LR.LinearReg()
LR.Show()
LR.SaveDatas()