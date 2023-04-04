# _*_ coding:Utf8 _*_


class History(object):
    # Creation of a History object
    def __init__(self, file_name, resolution_date, time_solve_labyrinth):
        self.file_name = file_name
        self.resolution_date = resolution_date
        self.time_solve_labyrinth = time_solve_labyrinth

    # Function that displays the history
    def read_history(self):
        data = f"{self.file_name}; "
        data += f"{self.resolution_date}; "
        data += f"{self.time_solve_labyrinth}"
        return data
