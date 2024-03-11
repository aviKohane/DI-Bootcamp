# As you work on a exercise, you should add and commit your work every 30mins.
# When you are done with your work, push all the modifications to your github repository.
# git push origin main

class Door:
    def __init__(self , is_opened):
        self.is_opened = is_opened
    def open_door(self):
        self.is_opened=True
        print("Door is opened")
    def close_door(self):
        self.is_opened=False
        print("Door is cloded")
        
class BlockedDoor(Door):
    def open_door(self):
        raise Exception('Cannot open a blocked door!')
    def close_door(self):
        raise Exception('Cannot close a blocked door!')

door1=Door(True)
print("hello")