from datetime import datetime
from project import Project


def load_projects(filename):
    """Load projects from a tab-delimited file."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header
        for line in file:
            name, start_date, priority, cost_estimate, completion = line.strip().split('\t')
            start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
            projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion)))
    return projects


def save_projects(filename, projects):
    """Save projects to a tab-delimited file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete = sorted([p for p in projects if p.completion_percentage < 100])
    completed = sorted([p for p in projects if p.completion_percentage == 100])
    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed:
        print(f"  {project}")


def filter_by_date(projects):
    """Filter projects by start date."""
    date_str = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.strptime(date_str, "%d/%m/%y").date()
    filtered = sorted([p for p in projects if p.start_date > filter_date], key=lambda x: x.start_date)
    for project in filtered:
        print(f"  {project}")


def add_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = datetime.strptime(input("Start date (dd/mm/yy): "), "%d/%m/%y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion))


def update_project(projects):
    """Update a project's completion percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    print(projects[choice])
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_percentage:
        projects[choice].completion_percentage = int(new_percentage)
    if new_priority:
        projects[choice].priority = int(new_priority)


def main():
    """Main program for project management."""
    filename = "projects.txt"
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")

    is_running = True
    while is_running:
        print("\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
              "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")
        choice = input(">>> ").lower()
        if choice == 'l':
            new_file = input("Enter filename to load: ")
            projects = load_projects(new_file)
        elif choice == 's':
            new_file = input("Enter filename to save: ")
            save_projects(new_file, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_by_date(projects)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save = input(f"Would you like to save to {filename}? ").lower()
            if save.startswith('y'):
                save_projects(filename, projects)
            print("Thank you for using custom-built project management software.")
            is_running = False

main()