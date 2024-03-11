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