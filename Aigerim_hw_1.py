class Animals:
    def __init__(self, name, color, gender, subsistence):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("name should be string")
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError("color should be string")
        if isinstance(gender, str):
            self.gender = gender
        else:
            raise ValueError("gender should be string")
        if isinstance(subsistence, str):
            self.subsistence = subsistence
        else:
            raise ValueError("subsistence should be string")


class Mammals(Animals):  # млекопитающие
    def __init__(self, name, color, gender, subsistence, speed, country):
        super().__init__(name, color, gender, subsistence)
        if isinstance(speed, int):
            self.speed = speed
        else:
            raise ValueError("speed should be integer")
        if isinstance(country, str):
            self.country = country
        else:
            raise ValueError("country should be string")

    def live_at_the_zoo(self):
        return f'This {self.name} is live at the {self.country}s zoo'

    def __str__(self):
        return f'name: {self.name}\n' \
               f'color : {self.color}\n' \
               f'gender : {self.gender}\n' \
               f'subsistence : {self.subsistence}\n' \
               f'speed : {self.speed}\n' \
               f'country : {self.country}'


class Birds(Animals):  # птицы
    def __init__(self, name, color, gender, subsistence, age, wing_flap):
        super().__init__(name, color, gender, subsistence)
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError("age should be integer")
        if isinstance(wing_flap, int):
            self.wing_flap = wing_flap
        else:
            raise ValueError("wing flap should be integer")

    def bird_wing_flap(self):
        return f'{self.name}s wing flip {self.wing_flap}cm'

    def __str__(self):
        return f'name: {self.name}\n' \
               f'color : {self.color}\n' \
               f'gender : {self.gender}\n' \
               f'subsistence : {self.subsistence}\n' \
               f'age : {self.age}\n' \
               f'wing flap : {self.wing_flap}'


class Fishes(Animals):  # рыбы
    def __init__(self, name, color, gender, subsistence, size, environment):  # среда обитания
        super().__init__(name, color, gender, subsistence)
        if isinstance(size, float):
            self.size = size
        else:
            raise ValueError('size should be float')
        if isinstance(environment, str):
            self.environment = environment
        else:
            raise ValueError('environment should be string')

    def __str__(self):
        return f'name: {self.name}\n' \
                f'color : {self.color}\n' \
                f'gender : {self.gender}\n' \
                f'subsistence : {self.subsistence}\n' \
                f'size : {self.size}m\n' \
                f'environment : {self.environment}'

    def fishes_environment(self):
        return f'{self.name} is inhabits in {self.environment}'


animal_1 = Mammals(name='Giraffe', color="yellow", gender="male", subsistence="leaves", speed=24, country='Germany')

animal_2 = Birds(name='Eagle', color='Brown,white', gender='female',subsistence='fish', age=10, wing_flap=74)

animal_3 = Fishes(name="shark", color="white", gender="female", subsistence="meat and fish", size=6.4, environment="Ocean")
print(animal_3)
print(animal_3.fishes_environment())

print(animal_2)
print(animal_2.bird_wing_flap())

print(animal_1)
print(animal_1.live_at_the_zoo())
