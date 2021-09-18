###############################################
#                                             #
#                   Image bot                 #
#    Project refactory Cravcenco Nichita(c)   #
# This part of bot was made by Cheban Michael #
#       Time start: 09/18/2021: 1:32AM        #
#                                             #
###############################################
from Bot import Bot








# constructor ImageBot:
#
#       @params:
#           __is_executed : bool
#           '__' means that this is a private variable
#           you have an access to it with two functions
#           that are inherit from 'super' class Bot
#           stop_execution() and run_execution()


class ImageBot(Bot):


    #constructor with default parameters
    def __init__(self):
        super().__init__()
        self.__path = None




    # u can use this function to check
    # if your path was written right
    def get_image_path(self: str) -> str:
        return self.__path




    # this functions let u to add image
    # from folder using path written
    # as a string.
    #
    # Note:
    # this method can set only string
    # value
    def set_image_path(self, path = ''):
        if self.__path is None:
            self.__path = "not a path"
        else:
            self.__path = path


    # execute
    def execute(self):
        if self._is_executed is True:
            print("imagebot starts execution")

            '''
            try:
                pos = imgsearch.imagesearch_region_loop("img/buy-button.png", 0, 0, 0, 550, 1000)
                pyautogui.click(pos[0], pos[1])
                time.sleep(0.2)
                pos = imgsearch.imagesearch_region_loop("img/wallet-balance.png", 0, 0, 0, 550, 1000)
                time.sleep(0.5)
                pyautogui.click(pos[0] + 200, pos[1] + 85)
            except:
                print("The folder or image was not found!")
            '''
        else:
            print("imagebot ends execution!")