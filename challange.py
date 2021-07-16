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
                zero_tensor = [zero_tensor for _ in range(self.__shape[index])]

        # create tensor with values from self.__data; same dimension as zero_tensor
        tensor = []
        data_in_tensor = 0
        data_length = len(self.__data)
        for i in range(self.__shape[0]):  # number of elements/lists in tensor (depth 1)
            if isinstance(zero_tensor[i], list):  # check if the element is list
                # create a smaller dimension tensor - divide and conquer
                t = Tensor(data=self.__data[data_in_tensor:], shape=self.__shape[1:]).__tensor
                data_in_tensor += Tensor.get_number_of_elements(t, 0)
                tensor.append(t)
            else:  # element is not a list therefore append data value
                # check if there is data to append
                if data_in_tensor < data_length:
                    tensor.append(self.__data[data_in_tensor])
                    data_in_tensor += 1
                else:
                    tensor.append(0)
        return tensor

    # recursively traverses the tensor and counts the number of non-list values
    @classmethod
    def get_number_of_elements(cls, ls, total):
        if not isinstance(ls, list):
            try:
                total += 1
                return total
            except TypeError:
                pass
        else:
            for element in ls:
                total = Tensor.get_number_of_elements(element, total)
            return total


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
