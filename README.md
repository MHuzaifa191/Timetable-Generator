# Timetable Generator Using Genetic Algorithm

## Overview
This project is a **Timetable Generator** that uses a **Genetic Algorithm** to optimize and automatically generate feasible timetables for departments and courses. The algorithm efficiently schedules classes in available rooms, assigns instructors, and ensures that various constraints are satisfied, such as room capacities, instructor availability, and avoiding timetable clashes.

## Features
- Generates optimized timetables for multiple departments.
- Supports both **lab** and **theory** courses with different room capacities.
- Ensures instructors are not double-booked.
- Considers constraints like room capacity, course timing conflicts, and instructor availability.
- Flexible and scalable, suitable for different educational institutions.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/MHuzaifa191/Timetable-Generator.git
   ```

2. Run the program:
   ```bash
   python timetable-generator.py
   ```

## Usage
Once the program is run, it will:
1. Initialize classrooms, instructors, and courses.
2. Generate an initial population of timetables.
3. Apply genetic operations (selection, crossover, mutation) to evolve the population.
4. Output the final timetable with minimal conflicts after several generations.

### Constraints and Customization:
- **Room Capacity**: Labs hold 80 students; theory classes hold 60.
- **Meeting Times**: Courses are scheduled across multiple time slots, including mornings and afternoons.
- **Instructor Availability**: Ensures instructors are not scheduled for overlapping classes.



## Genetic Algorithm Details
- **Population Size**: 50 individuals
- **Mutation Probability**: 50%
- **Tournament Size**: 3
- **Elitism**: 1 best individual is always retained in the next generation.
- **Fitness Function**: The fitness score is based on the number of conflicts in a schedule. Lower conflict results in higher fitness.


## Requirements
- Python 3.x
- Required Python libraries (specified in `requirements.txt`):
  - random
  - numpy (optional, for performance optimization)

## How It Works
1. **Initialization**: Initializes rooms, instructors, courses, and time slots.
2. **Genetic Algorithm**: 
   - **Selection**: Tournament selection is used to select parents for crossover.
   - **Crossover**: Combines schedules of two parents to produce offspring.
   - **Mutation**: Randomly swaps meeting times or room assignments to introduce variation.
3. **Fitness Evaluation**: Timetables with fewer conflicts (e.g., no instructor or room conflicts) have higher fitness scores.
4. **Termination**: The algorithm terminates after a certain number of generations or when an optimal timetable is found.

## Future Improvements
- Incorporating soft constraints (e.g., preferred time slots for instructors).
- Supporting different course types (e.g., seminars, workshops).
- Enhancing the algorithm to speed up convergence.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or contributions, feel free to reach out at [m.huz4if4@gmail.com](mailto:m.huz4if4@gmail.com).

