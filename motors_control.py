class RobotMotor:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed):
        self.speed = max(0, min(100, speed))
        print("Speed:", self.speed)

    def stop(self):
        self.speed = 0
        print("Stopped")


def smooth_speed_change(current, target):
    while current != target:
        if current < target:
            current += 5
        else:
            current -= 5
        print("Speed:", current)


robot = RobotMotor()
robot.set_speed(50)
robot.stop()