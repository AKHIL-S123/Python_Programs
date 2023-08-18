class MyValues:
    def __init__(self):
        self.values_dict = {}

    def add_value(self, key, value):
        self.values_dict[key] = value
        print(f"Value {value} added with key {key}")

    def get_value(self, key):
        if key in self.values_dict:
            return self.values_dict[key]
        else:
            print(f"Key {key} not found.")
            return None

my_values = MyValues()

while True:
    print("1. Add Value")
    print("2. Get Value")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = input("Enter key: ")
        value = input("Enter value: ")
        my_values.add_value(key, value)
    elif choice == 2:
        key = input("Enter key: ")
        retrieved_value = my_values.get_value(key)
        if retrieved_value is not None:
            print(f"Value for key {key}: {retrieved_value}")
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please select again.")
