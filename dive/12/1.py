import csv

class Subjects:
    def __init__(self, file):
        self.data = {}
        try:
            with open(file) as _file:
                reader = csv.reader(_file)
                for row in reader:
                    subjects = [x.strip() for x in row]
                    for s in subjects:
                        if s:
                            self.data[s] = {'grades' : [], 'scores' : []}
        except Exception as ex: raise ex

    def add_grade(self, subj, grade : int):
        if grade >= 2 and grade < 6:
            self.data[subj]['grades'].append(grade)

    def add_ts(self, subj, score : int):
        if score >= 0 and score <= 100:
            self.data[subj]['scores'].append(score)

class Student:
    def __init__(self, name, subjs : Subjects):
        self.__setattr__('name', name)
        self.subjects = subjs

    def __setattr__(self, name, value):
        if name == "name":
            if value[0].isupper() and value.is_alpha(): pass
            else: raise ValueError

        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name in self.subjects: return self.subjects[name]

        raise AttributeError
    
    def __str__(self):
        return f"{self.name} : {', '.join(self.subjects.keys())}"
    
    def avg_score(self, subj):
        scores = self.subjects[subj]['scores']

        return sum(scores) / len(scores)
    
    def avg_grade(self):
        grades = [grade for x in self.subjects.values() for grade in x['grades']]

        return sum(grades) / len(grades)
    
