import pandas as pd

class EmployeeDatabase:
    def __init__(self):
        self.data = pd.DataFrame(columns=["Employee ID", "Name", "Age", "Salary(PM)"])

    def add_employee(self, employee_id, name, age, salary):
        new_row = {"Employee ID": employee_id, "Name": name, "Age": age, "Salary(PM)": salary}
        self.data = self.data._append(new_row, ignore_index=True)

    def search_by_criteria(self, criteria, query, salary_option=None):
        if criteria in self.data.columns:
            if salary_option == 1:
                return self.data[self.data[criteria] > query].sort_values("Salary(PM)").head(1)
            elif salary_option == 2:
                result = self.data[self.data[criteria] == query]
                if result.empty:
                    return "No results found."
                return result
            elif salary_option == 3:
                return self.data[self.data[criteria] < query].sort_values("Salary(PM)", ascending=False).head(1)
            else:
                return None
        else:
            return None

def main():
    database = EmployeeDatabase()

    database.add_employee("161E90", "Raman", 41, 56000)
    database.add_employee("161F91", "Himadri", 38, 67500)
    database.add_employee("161F99", "Jaya", 51, 82100)
    database.add_employee("171E20", "Tejas", 30, 55000)
    database.add_employee("171G30", "Ajay", 45, 44000)

    print("Enter the choice:")
    print("1. Employee ID")
    print("2. Name")
    print("3. Age")
    print("4. Salary")
    choice = int(input())

    if choice in [1, 2, 3, 4]:
        criteria = "Employee ID" if choice == 1 else "Name" if choice == 2 else "Age" if choice == 3 else "Salary(PM)"
        query = input(f"Enter the query criteria to be {criteria}: ")

        if choice == 4:
            print("Select option for Salary:")
            print("1. Immediately higher")
            print("2. Equal to")
            print("3. Immediately less")
            salary_option = int(input())
            result = database.search_by_criteria(criteria, float(query), salary_option)
        else:
            result = database.search_by_criteria(criteria, query)

        if isinstance(result, pd.DataFrame):
            print(result)
        elif isinstance(result, str):
            print(result)
        else:
            print("No results found.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()