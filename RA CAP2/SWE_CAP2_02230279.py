################################
# Your Name : Chimi Gyeltshen
# Your Section : SWE
# Your Student ID Number : 02230279
################################
# REFERENCES
#https://www.youtube.com/watch?v=LpZmZs2_BC4
#https://www.freecodecamp.org/news/python-split-string-how-to-split-a-string-into-a-list-or-array-in-python/#:~:text=split()%20%3A%20This%20is%20the,space%2C%20comma%2C%20or%20tab.
#
################################
# SOLUTION
# Your Solution Score:
# Task 1: There were 20000 people assigned and there are 6445 of overlapping space assignments.
# Task 2: There were 2334 assignments that overlap completely.
################################

# Read the input.txt file

# def read_input():
#     with open('RA CAP2/input_9_cap2.txt', 'r') as file:
        
#         file_contents = file.read()
#     print(file_contents)

# read_input()


# solution
def task_1():
    def process_line(line):
       
        # Split the line based on the comma delimiter
        parts = line.split(',')
        
        #list to store assigned space sections for each person
        assigned_sections = []
        
        for part in parts:
            # Split the part based on the hyphen delimiter to get start and end points
            start, end = part.split('-')
            # Convert start and end points to integers
            start = int(start.strip())
            end = int(end.strip())
            # Add the assigned space section to the list
            assigned_sections.append((start, end))
        
        # Checking for overlaps
        overlapping_sections = 0
        for i in range(len(assigned_sections)):
            for j in range(i+1, len(assigned_sections)):
                person1_start, person1_end = assigned_sections[i]
                person2_start, person2_end = assigned_sections[j]
                # Check if there is an overlap between two assigned space sections
                if person1_end >= person2_start and person2_end >= person1_start:
                    overlapping_sections += 1
        
        #list of assigned space sections for each person and the number of overlapping sections
        return assigned_sections, overlapping_sections

    def read_input():

        total_overlapping_sections = 0  # Initialize total overlapping sections counter
        total_people_assigned = 0  # Initialize total number of people assigned spaces counter
        with open('RA CAP2/input_9_cap2.txt', 'r') as file:
            # Read each line of the file
            for line in file:
                # Process each line
                assigned_sections, overlapping_sections = process_line(line.strip())
                # Accumulate the number of overlapping sections
                total_overlapping_sections += overlapping_sections
                # Count the number of people assigned spaces in this line
                total_people_assigned += len(assigned_sections)
        
        print("Task_1 solution is:")
        print(f"There were {total_people_assigned} people assigned and there are {total_overlapping_sections} of overlapping space assignments.")

    
    read_input()


task_1()



def task_2():

    def total_overlapping(file_path):
        total = 0
        
        with open(file_path, 'r') as file:
            for line in file:
                for part in line.strip().split(','):
                    start, end = map(int, part.strip().split('-'))
                    if start <= 3 and end >= 7:
                        total += 1
        
        return total

    file_path = 'RA CAP2/input_9_cap2.txt'
    total_overlapping_assignments = total_overlapping(file_path)
    print("Task_2 solution is :")
    print(f"There were {total_overlapping_assignments} assignments that overlap completely." )

task_2()
   

