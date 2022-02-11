"""epuck_controller controller."""

# You may need to import some classes of the controller module. Ex
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, Camera, DistanceSensor,LED, Keyboard


class RobotMotor(Motor):
    def __init__(self, name):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)

    

class RobotCamera(Camera):
    def __init__(self, name):
        super().__init__(name)
        self.enable(samplingPeriod=50)
        self.recognitionEnable(samplingPeriod=100)
    
        

class SeatechRobot(Robot):
    def __init__(self):
        super().__init__()
        self.__leftMotor = RobotMotor('left wheel motor')
        self.__rightMotor = RobotMotor('right wheel motor')
        self.__camera = RobotCamera('camera')
        self.__lst_obj_seen = []
        self.role = "flee"


    def run_straight(self, rate = 1):
        self.__leftMotor.setVelocity(rate * MAX_SPEED)
        self.__rightMotor.setVelocity(rate * MAX_SPEED)
    
    def stop(self):
        self.__leftMotor.setVelocity(0)
        self.__rightMotor.setVelocity(0)
    
    def turn_right_stopped(self, rate = 1):
        self.stop()
        self.__leftMotor.setVelocity(rate * MAX_SPEED)
        self.__rightMotor.setVelocity(-rate * MAX_SPEED)

    def turn_left(self, rate = 1):
        self.__leftMotor.setVelocity(rate * 0.5 * MAX_SPEED)
        self.__rightMotor.setVelocity(rate * 0.6 * MAX_SPEED)

    def turn_right(self, rate = 1):
        self.__leftMotor.setVelocity(rate * 0.6 * MAX_SPEED)
        self.__rightMotor.setVelocity(rate * 0.5 * MAX_SPEED)

    def __find_nearest_goat(self):
        lst_dist = []
        self.__lst_obj_seen = self.__camera.getRecognitionObjects()
        if len(self.__lst_obj_seen)>0:
            for obj in self.__lst_obj_seen:
                if obj.get_colors() == [0,1,0]:
                    self.__lst_obj_seen.remove(obj)
        if len(self.__lst_obj_seen) == 0:
            return 'No Object found'
        else:
            for obj in self.__lst_obj_seen:
                lst_dist.append((obj.get_position()[0]**2 + obj.get_position()[1]**2)**0.5)
            min_dist = 1000
            index_min = 0
            for i in range(len(lst_dist)):
                if lst_dist[i] < min_dist:
                    min_dist = lst_dist[i]
                    index_min = i

            return self.__lst_obj_seen[index_min]


    def center_to_nearest_catch(self):
        target = self.__find_nearest_goat()
        if target == 'No Object found':
            self.run_straight()
            self.turn_right_stopped()
        else:
            middle = self.__camera.getWidth()/2
            #print(self.__camera.getWidth())
            #print(middle)
            print(target.get_position_on_image()[0])
            if target.get_position_on_image()[0] > middle + 4:
                self.turn_left(1)
            elif target.get_position_on_image()[0] < middle - 4:
                self.turn_right(1)
            elif (target.get_position_on_image()[0] <= middle + 4 
                and 
                target.get_position_on_image()[0] >= middle - 4):
                self.run_straight(1)
            
    def __find_nearest_catcher(self):
        lst_dist = []
        self.__lst_obj_seen = self.__camera.getRecognitionObjects()
        if len(self.__lst_obj_seen)>0:
            for obj in self.__lst_obj_seen:
                if obj.get_colors() == [1,0,0]:
                    self.__lst_obj_seen.remove(obj)
        if len(self.__lst_obj_seen) == 0:
            return 'No Object found'
        else:
            for obj in self.__lst_obj_seen:
                lst_dist.append((obj.get_position()[0]**2 + obj.get_position()[1]**2)**0.5)
            min_dist = 1000
            index_min = 0
            for i in range(len(lst_dist)):
                if lst_dist[i] < min_dist:
                    min_dist = lst_dist[i]
                    index_min = i

            return self.__lst_obj_seen[index_min]


    def center_to_nearest_flee(self):
        target = self.__find_nearest_catcher()
        if target == 'No Object found':
            self.run_straight()
            self.turn_right_stopped()
        else:
            middle = self.__camera.getWidth()/2
            #print(self.__camera.getWidth())
            #print(middle)
            print(target.get_position_on_image()[0])
            if target.get_position_on_image()[0] > middle + 4:
                self.turn_left(-1)
            elif target.get_position_on_image()[0] < middle - 4:
                self.turn_right(-1)
            elif (target.get_position_on_image()[0] <= middle + 4 
                and 
                target.get_position_on_image()[0] >= middle - 4):
                self.run_straight(-1)
                self.turn_right(-1)

    
    def play(self):
        if robot.role == 'catcher' : 
            robot.center_to_nearest_catch()
        if robot.role == 'flee':
             robot.center_to_nearest_flee()



if __name__ == '__main__':
    TIME_STEP = 64
    MAX_SPEED = 6.28
    robot = SeatechRobot()

    # get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())
    
    
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  motor = robot.getDevice('motorname')
    #  ds = robot.getDevice('dsname')
    #  ds.enable(timestep)
    
  
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    robot.run_straight(1)
    while robot.step(timestep) != -1:
        robot.play()
    #    robot.run_straight()  

    # Enter here exit cleanup code.
