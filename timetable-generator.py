from random import randrange as rr
import random

NUM_INDIVIDUALS = 50
NUM_ELITES = 1
TOURNEY_SIZE = 3
MUTATE_PROB = 0.5

class ScheduleInfo:
    # Labs have 80 capacity while theory classes have 60
    ROOMS = [
        ["C-301", 60, 3],
        ["C-302", 60, 3],
        ["C-303", 60, 3],
        ["C-304", 60, 3],
        ["Margalla 1", 80, 2],
        ["Margalla 2", 80, 2],
        ["Margalla 3", 80, 2],
        ["Margalla 4", 80, 2],
        ["Margalla 5", 80, 2],
        ["B-101", 60, 1],
        ["B-102", 60, 1],
        ["B-103", 60, 1],
        ["B-104", 60, 1],
        ["A-201", 60, 2],
        ["A-202", 60, 2],
        ["A-203", 60, 2],
        ["A-204", 60, 2]
    ]
    
    CLASS_TIMES = [
        ["MT1", "MW 08:30 - 09:50", 1.5],
        ["MT2", "MW 10:00 - 11:20", 1.5],
        ["MT3", "MW 11:30 - 12:50", 1.5],
        ["MT4", "MW 01:00 - 02:20", 1.5],
        ["MT5", "MW 02:30 - 03:50", 1.5],
        ["MT6", "MW 04:00 - 05:20", 1.5],
        ["MT7", "TTH 08:30 - 09:50", 1.5],
        ["MT8", "TTH 10:00 - 11:20", 1.5],
        ["MT3", "TTH 11:30 - 12:50", 1.5],
        ["MT9", "TTH 01:00 - 02:20", 1.5],
        ["MT10", "TTH 02:30 - 03:50", 1.5],
        ["MT11", "TTH 04:00 - 05:20", 1.5],
        ["LT1", "M 08:30 - 11:30", 3.0],
        ["LT2", "W 14:30 - 17:30", 3.0],
        ["LT3", "T 08:30 - 11:30", 3.0],
        ["LT4", "TH 14:30 - 17:30", 3.0]
    ]

    TEACHERS = [
        ["1", "Omer Beg"],
        ["2", "Saad Salman"],
        ["3", "A. R. Shahid"],
        ["4", "Behjat Zuhaira"],
        ["5", "Akhtar Jamil"],
        ["6", "Shams Farooq"],
        ["7", "Ahmad Din"],
        ["8", "Arhsad Islam"],
        ["9", "Bilal K. Dar"],
        ["10", "Mehreen Alam"],
        ["11", "Kashif Munir"],
        ["12", "IrfanUllah"]
    ]
    

    def __init__(self):
        self.rooms = []
        self.meeting_times = []
        self.teachers = []
        
        for i in range(0, len(self.ROOMS)):
            self.rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1], self.ROOMS[i][2]))
        
        for i in range(0, len(self.CLASS_TIMES)):
            self.meeting_times.append(MeetingTime(self.CLASS_TIMES[i][0], self.CLASS_TIMES[i][1], self.CLASS_TIMES[i][2]))
        
        for i in range(0, len(self.TEACHERS)):
            self.teachers.append(Instructor(self.TEACHERS[i][0], self.TEACHERS[i][1]))
                

                        
        courses = [
            Course("C1", "Theory1", random.sample(self.teachers, 2), 60, "Theory"),
            Course("C2", "Theory2", random.sample(self.teachers, 3), 60, "Theory"),
            Course("C3", "Theory3", random.sample(self.teachers, 2), 60, "Theory"),
            Course("C4", "Theory4", random.sample(self.teachers, 2), 60, "Theory"),
            Course("C5", "Theory5", random.sample(self.teachers, 1), 60, "Theory"),
            Course("C6", "Theory6", random.sample(self.teachers, 2), 60, "Theory"),
            Course("C7", "Theory7", random.sample(self.teachers, 2), 60, "Theory"),
            Course("C8", "Theory8", random.sample(self.teachers, 3), 60, "Theory"),
            Course("C9", "Theory9", random.sample(self.teachers, 2), 60, "Theory"),
            Course("C10", "Theory10", random.sample(self.teachers, 2), 60, "Theory"),
            Course("C11", "Theory11", random.sample(self.teachers, 1), 60, "Theory"),
            Course("C12", "Theory12", random.sample(self.teachers, 2), 60, "Theory"),
            Course("C13", "Theory13", random.sample(self.teachers, 2), 60, "Theory"),
            Course("C14", "Theory14", random.sample(self.teachers, 2), 60, "Theory"),
            Course("C15", "Theory15", random.sample(self.teachers, 2), 60, "Theory"),
            Course("C16", "LabCourse1", random.sample(self.teachers, 2), 80, "Lab"),
            Course("C17", "LabCourse2", random.sample(self.teachers, 2), 80, "Lab"),
            Course("C18", "LabCourse3", random.sample(self.teachers, 2), 80, "Lab"),
            Course("C19", "LabCourse4", random.sample(self.teachers, 2), 80, "Lab"),
            Course("C20", "LabCourse5", random.sample(self.teachers, 2), 80, "Lab"),
            Course("C21", "LabCourse6", random.sample(self.teachers, 2), 80, "Lab")
        ]

        # Create departments with the selected courses
        dept1 = Department("CS", [courses[0], courses[1], courses[2], courses[3], courses[4], courses[15], courses[16]])
        dept2 = Department("EE", [courses[5], courses[6], courses[7], courses[8], courses[9], courses[17], courses[18]])
        dept3 = Department("BBA", [courses[10], courses[11], courses[12], courses[13], courses[14], courses[19], courses[20]])
        
        self.depts = [dept1, dept2, dept3]
        
        self.num_of_classes = 0
        for i in range(0, len(self.depts)):
            self.num_of_classes += len(self.depts[i].get_courses())
    
    def get_rooms(self): return self.rooms
    def get_meeting_times(self): return self.meeting_times
    def get_teachers(self): return self.teachers
    def get_depts(self): return self.depts
    def get_num_of_classes(self): return self.num_of_classes

# Chromosome: ClassSchedule object

class ClassSchedule:
    def __init__(self, info):
        self.info = info
        self.classes = []
        self.num_of_conflicts = 0
        self.fitness = -1
        self.class_num = 0
        self.is_fitness_changed = True
        self.initialize()
    
    def get_classes(self): 
        self.is_fitness_changed = True
        return self.classes
    
    def get_num_of_conflicts(self): return self.num_of_conflicts
    def get_fitness(self):
        if self.is_fitness_changed:
            self.fitness = self.calculate_fitness()
            self.is_fitness_changed = False
        return self.fitness
        
    def initialize(self):
        depts = self.info.get_depts()
        for i in range(0, len(depts)):
            courses = depts[i].get_courses()
            for j in range(0, len(courses)):
                new_class = Class(self.class_num, depts[i], courses[j])
                self.class_num += 1
                # lab course constraint
                if "Lab" in courses[j].get_name():
                    # Select a lab meeting time and corresponding room
                    # labs = [room for room in self.info.get_rooms() if room.get_seatingCapacity() == 80]
                    # new_class.set_meetingTime([time for time in self.info.get_meeting_times() if time.get_length() == 3.0][0])
                    # new_class.set_room(labs[rr(0, len(labs))])
                    # Select a random lab meeting time and corresponding room
                    lab_times = [time for time in self.info.get_meeting_times() if time.get_length() == 3.0 and "LT" in time.get_id()]
                    lab_time = random.choice(lab_times)
                    labs = [room for room in self.info.get_rooms() if room.get_seatingCapacity() == 80]
                    lab_room = random.choice(labs)
                    new_class.set_meetingTime(lab_time)

                    new_class.set_room(lab_room)
                else:
                    # Select a regular meeting time
                    meeting_time = random.choice([time for time in self.info.get_meeting_times() if time.get_length() == 1.5])
                    new_class.set_meetingTime(meeting_time)
                    # Assign room based on department
                    if depts[i].get_name() == "BBA":
                        rooms = [room for room in self.info.get_rooms() if room.get_number().startswith("A")]
                    elif depts[i].get_name() == "CS":
                        rooms = [room for room in self.info.get_rooms() if room.get_number().startswith("C")]
                    elif depts[i].get_name() == "EE":
                        rooms = [room for room in self.info.get_rooms() if room.get_number().startswith("B")]
                    else:
                        rooms = self.info.get_rooms()
                    new_class.set_room(rooms[rr(0, len(rooms))])
                new_class.set_instructor(courses[j].get_instructors()[rr(0, len(courses[j].get_instructors()))])
                self.classes.append(new_class)
        return self


    
    def calculate_fitness(self):
        self.numOfConflicts = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            # room capacity constraint
            if (classes[i].get_room().get_seatingCapacity() < classes[i].get_course().get_maxStudents()):
                self.numOfConflicts += 1
            for j in range(0, len(classes)):
                if (j >= 1):
                    # room and time slot clash constraint
                    if (classes[i].get_meetingTime() == classes[j].get_meetingTime() and classes[i].get_id() != classes[j].get_id()):
                        if (classes[i].get_room() == classes[j].get_room()): self.numOfConflicts += 1
                        if (classes[i].get_instructor() == classes[j].get_instructor()): self.numOfConflicts += 1
                    if (classes[i].get_instructor() == classes[j].get_instructor() and
                        classes[i].get_meetingTime() == classes[j].get_meetingTime() and
                        classes[i].get_id() != classes[j].get_id()): self.numOfConflicts += 1
                    if (classes[i].get_dept() == classes[j].get_dept() and
                        classes[i].get_meetingTime() == classes[j].get_meetingTime() and
                        classes[i].get_id() != classes[j].get_id()): self.numOfConflicts += 1
                    
        # maximum number of courses per instructor constraint
        for instructor in self.info.get_teachers():
            coursesCount = 0
            for cls in classes:
                if cls.get_instructor().get_id() == instructor.get_id():
                    coursesCount += 1
                if coursesCount > 1:  # Ensuring no instructor is teaching two classes at the same time
                    self.numOfConflicts += 1

        # maximum number of courses p`er department constraint 
        for dept in self.info.get_depts():
            if len(dept.get_courses()) > 5: self.numOfConflicts += 1
        for cls in classes:
            if "Lab" in cls.get_course().get_name():
                if not any(x.get_id() == cls.get_id() + 1 for x in classes): self.numOfConflicts += 1

        # return fitness        
        return 1 / (1.0 * self.numOfConflicts + 1)


class Generation:
    def __init__(self, size):
        self.size = size
        self.info = info
        self.schedules = []
        for i in range(0, size): self.schedules.append(ClassSchedule(info))
    def get_schedules(self): return self.schedules
    

class GeneticAlgo:
    
    def crossover_population(self, pop):
        crossover_pop = Generation(0)
        for i in range(NUM_ELITES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUM_ELITES
        while (i < NUM_INDIVIDUALS):
            schedule1 = self.select_tournament_population(pop).get_schedules()[0]
            schedule2 = self.select_tournament_population(pop).get_schedules()[0]
            crossover_pop.get_schedules().append(self.crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop
    
    def mutate_population(self, population):
        for i in range(NUM_ELITES, NUM_INDIVIDUALS):
            self.mutate_schedule(population.get_schedules()[i])
        return population
    
    def evolve(self, population):
        return self.mutate_population(self.crossover_population(population))    
    
    def crossover_schedule(self, schedule1, schedule2):
        crossover_schedule = ClassSchedule(schedule1.info)  # Get info from one of the schedules
        crossover_point = random.choice(["course", "timeslot"])

        if crossover_point == "course":
            courses1 = set([c.get_course().get_number() for c in schedule1.get_classes()])
            courses2 = set([c.get_course().get_number() for c in schedule2.get_classes()])
            crossover_course = random.choice(list(courses1.union(courses2)))
            for i in range(0, len(crossover_schedule.get_classes())):
                if crossover_schedule.get_classes()[i].get_course().get_number() == crossover_course:
                    crossover_schedule.get_classes()[i] = schedule1.get_classes()[i]
                else:
                    crossover_schedule.get_classes()[i] = schedule2.get_classes()[i]

        elif crossover_point == "timeslot":
            timeslots = len(schedule1.info.get_meeting_times()) // 2  # Access info from schedule1
            for i in range(0, len(crossover_schedule.get_classes())):
                if i < timeslots:
                    crossover_schedule.get_classes()[i] = schedule1.get_classes()[i]
                else:
                    crossover_schedule.get_classes()[i] = schedule2.get_classes()[i]

        return crossover_schedule

        
    def mutate_schedule(self, mutate_schedule):
        for i in range(0, len(mutate_schedule.get_classes())):
            if MUTATE_PROB > rr(0, 100) / 100:
                for j in range(i + 1, len(mutate_schedule.get_classes())):
                    class1 = mutate_schedule.get_classes()[i]
                    class2 = mutate_schedule.get_classes()[j]
                    if class1.get_room() == class2.get_room() and class1.get_meetingTime() == class2.get_meetingTime():
                        # Swap rooms if capacities are suitable
                        if class1.get_course().get_maxStudents() <= class2.get_room().get_seatingCapacity() and \
                        class2.get_course().get_maxStudents() <= class1.get_room().get_seatingCapacity():
                            class1.set_room(class2.get_room())
                            class2.set_room(class1.get_room()) 
                            break  # Stop after swapping

        return mutate_schedule
    
    def select_tournament_population(self, pop):
        tournament_pop = Generation(0)
        i = 0
        while (i < TOURNEY_SIZE):
            tournament_pop.get_schedules().append(pop.get_schedules()[rr(0, NUM_INDIVIDUALS)])
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop

class Course:
    def __init__(self, number, name, instructors, maxStudents, type):
        self.number = number
        self.name = name
        self.instructors = instructors
        self.maxStudents = maxStudents
        self.type = type
        self.type = type
        if self.type == "Lab":
            self.number = "L" + self.number 
    
    def get_number(self): return self.number
    def get_name(self): return self.name
    def get_instructors(self): return self.instructors
    def get_maxStudents(self): return self.maxStudents
    def get_type(self): return self.type
    
    def __str__(self): return self.name

class Room:
    def __init__(self, number, seatingCapacity, floor):
        self.number = number
        self.seatingCapacity = seatingCapacity
        self.floor = floor
    
    def get_number(self): return self.number
    def get_seatingCapacity(self): return self.seatingCapacity
    def get_floor(self): return self.floor

class MeetingTime:
    def __init__(self, id, time, length):
        self.id = id
        self.time = time
        self.length = length
    
    def get_id(self): return self.id
    def get_time(self): return self.time
    def get_length(self): return self.length

class Instructor:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def get_id(self): return self.id
    def get_name(self): return self.name

class Department:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def get_name(self): return self.name
    def get_courses(self): return self.courses

class Class:
    def __init__(self, id, dept, course):
        self.id = id
        self.dept = dept
        self.course = course
        self.instructor = None
        self.meetingTime = None
        self.room = None
        self.floor = None
    
    def get_id(self): return self.id
    def get_dept(self): return self.dept
    def get_course(self): return self.course
    def get_instructor(self): return self.instructor
    def get_meetingTime(self): return self.meetingTime
    def get_room(self): return self.room
    def get_floor(self): return self.floor

    def set_instructor(self, instructor): self.instructor = instructor
    def set_meetingTime(self, meetingTime): self.meetingTime = meetingTime
    def set_room(self, room): self.room = room
    def set_floor(self, floor): self.floor = floor

    def __str__(self):
        return str(self.dept.get_name()) + "," + str(self.course.get_number()) + ", " + \
            str(self.room.get_number()) + ", " + str(self.instructor.get_id()) + ", " + str(self.meetingTime.get_id()) + ", " + str(self.floor)
    
class DisplayManagerClass:
    def print_available_info(self):
        print("> All available Data")
        self.print_dept()
        self.print_course()
        self.print_room()
        self.print_instructor()
        self.print_meeting_times()

    def print_room(self):
        print("> Rooms:")
        for room in info.get_rooms():
            print(room.get_number(), room.get_seatingCapacity(), room.get_floor())

    def print_dept(self):
        print("> Departments:")
        for dept in info.get_depts():
            print(dept.get_name())

    def print_course(self):
        print("> Courses:")
        for dept in info.get_depts():
            for course in dept.get_courses():
                print(course.get_number(), course.get_name())

    def print_instructor(self):
        print("> Instructors:")
        for instructor in info.get_teachers():
            print(instructor.get_id(), instructor.get_name())

    def print_meeting_times(self):
        print("> Meeting Times:")
        for time in info.get_meeting_times():
            print(time.get_id(), time.get_time())

    def print_generation(self, population):
        print("> Population:")
        for i, schedule in enumerate(population.get_schedules()):
            print(f"Schedule {i + 1}: Fitness={schedule.get_fitness()}")

    def print_schedule_as_table(self, schedule):
        print("\t\tSchedule")
        classes = schedule.get_classes()
        print("{:<10} {:<15} {:<20} {:<25} {:<15} {:<10}".format("Course", "Room", "Instructor", "Time", "Department", "Floor"))
        for class_obj in classes:
            print("{:<10} {:<15} {:<20} {:<25} {:<15} {:<10}".format(class_obj.get_course().get_number(),
                                                                       class_obj.get_room().get_number(),
                                                                       class_obj.get_instructor().get_name(),
                                                                       class_obj.get_meetingTime().get_time(),
                                                                       class_obj.get_dept().get_name(),
                                                                       class_obj.get_room().get_floor()))


info = ScheduleInfo()
display_mgr = DisplayManagerClass()
display_mgr.print_available_info()
generation_number = 0
print("\n> Generation # " + str(generation_number))
population = Generation(NUM_INDIVIDUALS)
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
display_mgr.print_generation(population)
genetic_algorithm = GeneticAlgo()

MAX_GENERATIONS_WITHOUT_IMPROVEMENT = 50  # Define the maximum number of generations without improvement
generations_without_improvement = 0  # Counter to track generations without improvement
best_fitness = population.get_schedules()[0].get_fitness()  # Initialize best fitness

while (population.get_schedules()[0].get_fitness() != 1.0):
    generation_number += 1
    print("\n> Generation # " + str(generation_number))
    population = genetic_algorithm.evolve(population)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    display_mgr.print_generation(population)
    
    # Check if the best schedule has improved
    if population.get_schedules()[0].get_fitness() > best_fitness:
        best_fitness = population.get_schedules()[0].get_fitness()
        generations_without_improvement = 0
    else:
        generations_without_improvement += 1
    
    # Check if the maximum generations without improvement is reached
    if generations_without_improvement >= MAX_GENERATIONS_WITHOUT_IMPROVEMENT:
        print("\nNo improvement for", MAX_GENERATIONS_WITHOUT_IMPROVEMENT, "generations. Stopping...")
        break

# Print the final best schedule
print("\n\n")
display_mgr.print_schedule_as_table(population.get_schedules()[0])