from abc import ABC, abstractmethod
import random


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list[int]) -> list[int]:
        pass


class BubbleSortStrategy(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        length = len(data)
        # Outer loop: Repeat the process for each element in the list
        for i in range(length):
            # Inner loop: Compare adjacent elements
            for j in range(0, length - i - 1):
                # If the current element is greater than the next:
                if data[j] > data[j + 1]:
                    # then, swap them.
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data


class QuickSortStrategy(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        # If the list has 1 or no elements, it's already sorted.
        if len(data) <= 1:
            return data
        else:
            pivot = data[-1]
            smaller = [item for item in data[:-1] if item <= pivot]
            greater = [item for item in data[:-1] if item > pivot]

            return self.sort(smaller) + [pivot] + self.sort(greater)


class Context:
    def execute(self, data: list[int], strategy: SortStrategy) -> list[int]:
        data = [(item * 2) + random.randint(-10, 10) for item in data]

        return strategy.sort(data)

# Example of usage
def main() -> None:
    context = Context()
    print(context.execute([1, 5, 3, 4, 2], BubbleSortStrategy()))
    print(context.execute([1, 5, 3, 4, 2], QuickSortStrategy()))


if __name__ == "__main__":
    main()
