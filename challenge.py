import copy

class Tensor:
    def __init__(self, data=None, shape=None):
        if data is None:
            data = []
        if shape is None:
            shape = []
        self.__data = data
        self.__shape = shape
        self.__tensor = self.__shape_data()

    def __str__(self):
        return str(self.__tensor)

    def __repr__(self):
        return "Tensor(" + self.__str__() + ")"

    def __shape_data(self):
        if not self.__shape:
            return []

        # create tensor with zeros of appropriate dimension
        zero_tensor = []
        for index in range(len(self.__shape) - 1, -1, -1):
            # if last element of shape then add shape[index] amount of zeros to list
            if index + 1 == len(self.__shape):
                for i in range(self.__shape[index]):
                    zero_tensor.append(0)
            else:  # else duplicate the tensor self.__shape amount of times
                zero_tensor = [copy.deepcopy(zero_tensor) for _ in range(self.__shape[index])]

        self.__traverse_tensor(zero_tensor, 0, len(self.__data))
        return zero_tensor

    def __traverse_tensor(self, ls, nr_data_points, data_length):
        if not isinstance(ls, list):
            if nr_data_points < data_length:
                return self.__data[nr_data_points], nr_data_points + 1
            else:
                return 0, nr_data_points
        else:
            for i in range(len(ls)):
                ls[i], nr_data_points = self.__traverse_tensor(ls[i], nr_data_points, data_length)
            return ls, nr_data_points

def main():
    data0 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
    shape0 = [2, 3, 2]
    tensor0 = Tensor(data0, shape0)
    print("t0")
    print(tensor0)

    data1 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1]
    shape1 = [5, 2]
    tensor1 = Tensor(data1, shape1)
    print("\nt1")
    print(tensor1)

    tensor2 = Tensor([], [7, 1])
    print("\nt2")
    print(tensor2)

    t3 = Tensor(data1, [5])
    print("\nt3")
    print(t3)

    t4 = Tensor(data1, [])
    print("\nt4")
    print(t4)

    shape2 = [2, 2, 2, 2]
    tensor5 = Tensor(data0, shape2)
    print("\nt5")
    print(tensor5)


if __name__ == '__main__':
    main()
