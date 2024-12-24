from abc import ABC, abstractmethod
import random


class SortAlgorithm(ABC):
    @abstractmethod
    def sort(self, data: list[int]) -> list[int]:
        pass


class BubbleSortAlgorithm(SortAlgorithm):
    def sort(self, data: list[int]) -> list[int]:
        length = len(data)
        for i in range(length):
            for j in range(0, length - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data


class QuickSortAlgorithm(SortAlgorithm):
    def sort(self, data: list[int]) -> list[int]:
        if len(data) <= 1:
            return data
        else:
            pivot = data[-1]
            smaller = [item for item in data[:-1] if item <= pivot]
            greater = [item for item in data[:-1] if item > pivot]

            return self.sort(smaller) + [pivot] + self.sort(greater)


class SelectionSortAlgorithm(SortAlgorithm):
    def sort(self, data: list[int]) -> list[int]:
        length = len(data)
        for i in range(length - 1):
            min_index = i
            for j in range(i + 1, length):
                if data[j] < data[min_index]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
        return data


class InsertionSortAlgorithm(SortAlgorithm):
    def sort(self, data):
        length = len(data)
        for i in range(1, length):
            insert_index = i
            current_value = data[i]
            for j in range(i-1, -1, -1):
                if data[j] > current_value:
                    data[j+1] = data[j]
                    insert_index = j
                else:
                    break
            data[insert_index] = current_value
        return data


class Context:
    def execute(self, data: list[int], algorithm: SortAlgorithm) -> list[int]:
        data = [(item * 2) + random.randint(-10, 10) for item in data]

        return algorithm.sort(data)


# Example of usage
def main() -> None:
    context = Context()
    print('Sorted by (Bubble algorithm): ',
          context.execute(
              [1, 5, 3, 4, 2], BubbleSortAlgorithm()))
    print('Sorted by (Quick algorithm): ', context.execute(
        [1, 5, 3, 4, 2], QuickSortAlgorithm()))
    print('Sorted by (Selection algorithm): ', context.execute(
        [1, 5, 3, 4, 2], SelectionSortAlgorithm()))
    print('Sorted by (Insertion algorithm): ', context.execute(
        [1, 5, 3, 4, 2], InsertionSortAlgorithm()))


if __name__ == "__main__":
    main()
