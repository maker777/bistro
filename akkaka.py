class Computer:
    def __init__(self, cpu, ram, storage, gpu, components):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu
        self.components = components

    def __str__(self):
        return (f"Computer Specifications:\n"
                f"CPU: {self.cpu}\n"
                f"RAM: {self.ram}\n"
                f"Storage: {self.storage}\n"
                f"GPU: {self.gpu}\n"
                f"Components: {', '.join(self.components)}")


class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None
        self.components = []

    def set_cpu(self, cpu):
        self.cpu = cpu
        return self

    def set_ram(self, ram):
        self.ram = ram
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def set_gpu(self, gpu):
        self.gpu = gpu
        return self

    def add_component(self, component):
        self.components.append(component)
        return self

    def build(self):
        return Computer(self.cpu, self.ram, self.storage, self.gpu, self.components)


# Пример использования
if __name__ == "__main__":
    builder = ComputerBuilder()
    computer = (builder
                .set_cpu("Ryzen 2600")
                .set_ram("256GB")
                .set_storage("9TB SSD")
                .set_gpu("NVIDIA GeForce RTX 2060")
                .add_component("Motherboard")
                .add_component("Power Supply")
                .add_component("Cooling System")
                .add_component("Case")
                .build())

    print(computer)
