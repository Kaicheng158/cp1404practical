from project import Project


def main(incomplete_project=None):
        MENU = "Menu: \n(L)oad projects" \
               "\n(S)ave projects" \
               "\n(D)isplay projects" \
               "\n(F)ilter projects by date" \
               "\n(A)dd new project" \
               "\n(U)padete project" \
               "\n(Q)uit"

        projects = get_file('project.txt')
        print(MENU)
        choice = input(">>> ").upper()
        while choice != "Q":
            if choice == "L":
                filename = input('Enter filename: ')
                if filename != '':
                    try:
                        projects = get_file(filename)
                        print(projects)
                    except FileNotFoundError:
                        print("Invalid Filename")
            elif choice == "s":
                filename = input('Enter filename to be save: ')
                save_file(projects, filename)

            elif choice == "D":
                complete_project, incomeplete = check_project(projects)
                print('Incomplete projects')
                incomplete_project.sort()
                display_project(incomeplete_project)
                print("")
                print("Completed projects: ")
                complete_project.sort()
                display_project(complete_project)

            elif choice == "F":
                date = input('Show projects that start after date (dd/mm/yy): ')
                filtered_date_projects = filtered_projects(date, projects)
                projects = sort_projects(filtered_date_projects)
                display_project(projects)

            elif choice == "A":
                print('Lets add a new project')
                try:
                    name = input('Name: ')
                    start_date = input('Start date (dd/mm/yy): ')
                    priority = int(input('Prionity: '))
                    cost = input('Cost estimate: ')
                    cost = cost.replace('$', '')
                    cost = int(cost)
                    completion = input('Percent complete: ')
                    project = Project(str(name), str(start_date), int(priority), int(cost), int(completion))
                    project.append(project)
                except ValueError:
                    print('Invalid Input')

            elif choice == "U":
                projects = sort_projects(projects)
                display_project(projects)
                projects_number = {}

                for number, project in enumerate(projects):
                    projects_number[str(number + 1)] = project
                try:
                    choice = input('Project choice: ')
                    chosen_project = projects_number[choice]
                    print(chosen_project)
                    new_percentage = input('New Percentage: ')
                    new_priority = input('New Priority: ')

                    if new_percentage != '':
                        chosen_project.update_percentage(int(new_percentage))

                    if new_priority != '':
                        chosen_project.update_priority(int(new_priority))

                except KeyError:
                    print('Invalid Choice')

            else:
                print("Invalid choice")
            print(MENU)
            choice = input(">>> ").upper()
        print('Thank you for using custom project management software.')

    def filtered_projects(date, projects):
        filtered_projects_date = []
        for project in projects:
            if project.compare_date(date):
                filtered_projects_date.append(project)
        return filtered_projects_date

    def sort_projects(projects):
        date_list = []
        for project in projects:
            if project.start_date not in date_list:
                date_list.append(project.start_date)
        date_list.sort()
        sort_project = []
        for date in date_list:
            for number, project in enumerate(projects):
                if project.start_date == date:
                    sort_project.append(project)
        return sorted_project

    def get_file(filename):
        projects = []
        in_file = open(filename, 'r')
        in_file.readline()
        for line in in_file:
            parts = line.strip().replace("\t", ',')
            parts = parts.split(',')
            projects = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(projects)
        in_file.close()
        return projects

def save_file(projects, filename):
    with open(filename, 'w') as out_file:
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost}\t{project.completion}", file=)


def display_project(projects):
    for number, project in enumerate(projects):
        print(f"{number + 1} {project}")

def check_project(projects):
    complete_project = []
    incomplete_projects = []
    for project in projects:
        if project.is_complete():
            complete_project.append(project)
            complete_project.sort()
        else:
            incomplete_projects.append(project)
            incomplete_projects.sort()
        return complete_project, incomplete_projects

main()
