class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self._power = power          # Protected attribute (encapsulation)
        self.origin = origin

    def display_info(self):
        print(f"🦸 Superhero: {self.name}")
        print(f"🌟 Power: {self._power}")
        print(f"🌍 Origin: {self.origin}")

    def use_power(self):
        print(f"{self.name} uses {self._power}!")