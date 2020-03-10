class Language:
    def __init__(self, name):
        self.name = name
        self.dbase = {}
        self.counter = 0

    def add_student(self, username, points):
        if username not in self.dbase:
            self.dbase[username] = []
        self.dbase[username].append(points)
        self.counter += 1


data = input()
obj_list = []
language_list = []

while data != "exam finished":
    token = data.split("-")
    if len(token) == 3:
        username, language, points = token
        if language not in language_list:
            obj = Language(language)
            obj_list.append(obj)
            obj.add_student(username, int(points))
            language_list.append(obj.name)
        else:
            obj1 = list(filter(lambda x: x.name == language, obj_list))[0]
            obj1.add_student(username, int(points))
    elif token[1] == "banned":
        username = token[0]
        for obj in obj_list:
            if username in obj.dbase:
                del obj.dbase[username]
    data = input()

results_list = []
results_list_2 = []
for obj in obj_list:
    for k, v in obj.dbase.items():
        results_list.append((k, max(v)))
    results_list_2.append((obj.name, obj.counter))
sorted_results_list = sorted(results_list, key=lambda x: (-x[1], x[0]))
sorted_results_lis_2 = sorted(results_list_2, key=lambda x: (-x[1], x[0]))
print("Results:")
for username, points in sorted_results_list:
    print(f"{username} | {points}")
print("Submissions:")
for language, count in sorted_results_lis_2:
    print(f"{language} - {count}")
