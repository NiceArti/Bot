#'self' same as 'this' in c++


class Bot:

    # constructor
    def __init__(self):
        self._is_executed = False




    # if u want to start working this bot
    # run this command in your program
    def stop_execution(self):
        self._is_executed = False




    # if u want to end working this bot
    # run this command in your program
    def start_execution(self):
        self._is_executed = True


    def execute(self):
        if self._is_executed is True:
            print("bot starts execution")
        else:
            print("bot ends execution")