
def towers_of_hanoi(
    n,
    source,
    destination,
    auxiliary,
):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    towers_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    towers_of_hanoi(n - 1, auxiliary, destination, source)

if __name__ == "__main__":
    n = 3
    towers_of_hanoi(n, "A", "C", "B")

def get_average(numbers):
   total = sum(numbers)
    average = total / len(numbers)
    return average



#Single Line comment:

# function to print a message
    def print_message(message):
        print(message)

