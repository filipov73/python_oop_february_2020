class Lion:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    @staticmethod
    def get_needs():
        return 50

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Tiger:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def get_needs(self):
        return 45

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Cheetah:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def get_needs(self):
        return 60

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Keeper:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Caretaker:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Vet:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def __sum_all_salary(self):
        all_sum = sum([s.salary for s in self.workers])
        return all_sum

    def __sum_tend_animals(self):
        sum_tend = 0
        for obj in self.animals:
            sum_tend += obj.get_needs()
        return sum_tend

    # def __check_worker_in_list(self, worker_name):
    #     for worker in self.workers:
    #         if worker.name == worker_name:
    #             return True
    #     return False

    def __filter_animals(self, kind):
        animals_ = list(filter(lambda x: x.__class__.__name__ == kind, self.animals))
        return animals_

    def __filter_workers(self, worker):
        workers_ = list(filter(lambda x: x.__class__.__name__ == worker, self.workers))
        return workers_


    # @property
    # def budget(self):
    #     return self.__budget
    #
    # @budget.setter
    # def budget(self, value):
    #     self.__budget = value
    #
    # @property
    # def animal_capacity(self):
    #     return self.__animal_capacity
    #
    # @animal_capacity.setter
    # def animal_capacity(self, value):
    #     self.__animal_capacity = value
    #
    # @property
    # def workers_capacity(self):
    #     return self.__workers_capacity
    #
    # @workers_capacity.setter
    # def workers_capacity(self, value):
    #     self.__workers_capacity = value

    def add_animal(self, animal, price):
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"

        if self.__budget - price < 0:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        # self.__animal_capacity -= 1
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, w):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(w)
        # self.__workers_capacity -= 1
        return f"{w.name} the {w.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

        # check_worker = self.__check_worker_in_list(worker_name)
        # if not check_worker:
        #     return f"There is no {worker_name} in the zoo"
        #
        # del_worker = list(filter(lambda x: x.name == worker_name, self.workers))[0]
        # self.workers.remove(del_worker)
        # return f"{worker_name} fired successfully"

    def pay_workers(self):
        sum_salary = self.__sum_all_salary()
        if self.__budget < sum_salary:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= sum_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        sum_tend_animals = self.__sum_tend_animals()
        if self.__budget < sum_tend_animals:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= sum_tend_animals
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = ""
        count = len(self.animals)
        result += f"You have {count} animals\n"

        filtred_lions = self.__filter_animals("Lion")
        length_lions = len(filtred_lions)
        result += f"----- {length_lions} Lions:\n"
        for obj in filtred_lions:
            result += f"{obj}\n"

        filtred_tigers = self.__filter_animals("Tiger")
        length_tigers = len(filtred_tigers)
        result += f"----- {length_tigers} Tigers:\n"
        for obj in filtred_tigers:
            result += f"{obj}\n"

        filtred_cheetahs = self.__filter_animals("Cheetah")
        length_cheetahs = len(filtred_cheetahs)
        result += f"----- {length_cheetahs} Cheetahs:\n"
        for obj in filtred_cheetahs:
            result += f"{obj}\n"
        return result

    def workers_status(self):
        result = ""
        count = len(self.workers)
        result += f"You have {count} workers\n"

        filtred_keepers = self.__filter_workers("Keeper")
        length_keepers = len(filtred_keepers)
        result += f"----- {length_keepers} Keepers:\n"
        for obj in filtred_keepers:
            result += f"{obj}\n"

        filtred_caretaker = self.__filter_workers("Caretaker")
        length_caretaker = len(filtred_caretaker)
        result += f"----- {length_caretaker} Caretakers:\n"
        for obj in filtred_caretaker:
            result += f"{obj}\n"

        filtred_vetes = self.__filter_workers("Vet")
        length_vetes = len(filtred_vetes)
        result += f"----- {length_vetes} Vets:\n"
        for obj in filtred_vetes:
            result += f"{obj}\n"
        return result


zoo = Zoo("Zootopia", 3000, 5, 8)


animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())


"""
Cheeto the Cheetah added to the zoo
Cheetia the Cheetah added to the zoo
Simba the Lion added to the zoo
Zuba the Tiger added to the zoo
Tigeria the Tiger added to the zoo
Not enough space for animal
John the Keeper hired successfully
Adam the Keeper hired successfully
Anna the Keeper hired successfully
Bill the Caretaker hired successfully
Marie the Caretaker hired successfully
Stacy the Caretaker hired successfully
Peter the Vet hired successfully
Kasey the Vet hired successfully
Not enough space for worker
You tended all the animals. They are happy. Budget left: 1779
You payed your workers. They are happy. Budget left: 611
Adam fired successfully
You have 5 animals
----- 1 Lions:
Name: Simba, Age: 4, Gender: Male
----- 2 Tigers:
Name: Zuba, Age: 3, Gender: Male
Name: Tigeria, Age: 1, Gender: Female
----- 2 Cheetahs:
Name: Cheeto, Age: 2, Gender: Male
Name: Cheetia, Age: 1, Gender: Female

You have 7 workers
----- 2 Keepers:
Name: John, Age: 26, Salary: 100
Name: Anna, Age: 31, Salary: 95
----- 3 Caretakers:
Name: Bill, Age: 21, Salary: 68
Name: Marie, Age: 32, Salary: 105
Name: Stacy, Age: 35, Salary: 140
----- 2 Vets:
Name: Peter, Age: 40, Salary: 300
Name: Kasey, Age: 37, Salary: 280
"""
