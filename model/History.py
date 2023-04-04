# _*_ coding:Utf8 _*_


class History(object):
    # Creation of a History object
    def __init__(self, file_name, resolution_date, time_solve_labyrinth):
        self.file_name = file_name
        self.resolution_date = resolution_date
        self.time_solve_labyrinth = time_solve_labyrinth

    # Function that displays the attributes of history
    def __str__(self):
        data = f"{self.file_name}; "
        data += f"{self.resolution_date}; "
        data += f"{self.time_solve_labyrinth}"

        return data

    def __repr__(self):
        data = f"object = History(file_name={self.file_name}, "
        data += f"resolution_date={self.resolution_date}, "
        data += f"time_solve_labyrinth={self.time_solve_labyrinth})"

        return data
