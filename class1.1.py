class Computer:
    def __init__(self, processor, ram, storage):
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def conf(self):
        print(f"Processor: {self.processor}, RAM: {self.ram}, Storage: {self.storage}")

print("Configuration of com1:")
com1 = Computer("i5", "16GB", "1TB")
com1.conf()

print("\nConfiguration of com2:")
com2 = Computer("i7", "32GB", "2TB")
com2.conf()

class Lap:
    def __init__(self, processor, ram, storage):
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def conf(self):
        print(f"Processor: {self.processor}, RAM: {self.ram}, Storage: {self.storage}")

print("\nConfiguration of lap1:")
lap1 = Lap("i7", "16GB", "1TB")
lap1.conf()

print("\nConfiguration of lap2:")
lap2 = Lap("i9", "64GB", "4TB")
lap2.conf()