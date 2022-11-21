

from steering_character import BeakBall
from fsm import FSM

class FSMBeakBall (BeakBall):

    def __init__ (self, x, y, r, m, color, xv, yv):

        BeakBall.__init__(self, x, y, r, m, color, xv, yv)

        self.fsm = FSM()

        # green - wander; red - run
        self.fsm.add_states ([('wandering', lambda:self.wander(1.0/30)), \
                              ('looping', lambda:self.loop(15.0/30)), \
                                ('freezing',lambda:self.freeze())])


        self.fsm.add_transitions ('wandering', [(self.test_on_corner, 'freezing')])

        self.fsm.add_transitions ('wandering', [(self.test_on_red, 'looping')])

        self.fsm.add_transitions ('looping', [(self.test_on_green, 'wandering')])

        #self.fsm.add_transitions ('looping', [(self.test_on_corner, 'freezing')])

        #self.fsm.add_transitions ('wandering', [(self.test_on_corner, 'freezing')])




        #self.fsm.add_transitions ('wandering', [(self.test_on_corner, 'freezing')])



    def execute_actions (self):

        self.steering = []

        action = self.fsm.states[self.fsm.current_state]
        print("current state:",self.fsm.current_state)
        action()

        self.apply_steering ()


    def test_on_red (self, world):
        print("hello red")

        if self.p.x > world.width/2:
            print("red")
            return True
        else:
            return False

    def test_on_green (self, world):

        if self.p.x < world.width/2:
            print("green")
            return True
        else:
            return False

    def test_on_corner (self, world):

          if self.p.x + self.r > world.width and self.p.y + self.r > world.height:
            return True
          if self.p.x - self.r < world.width and self.p.y - self.r < world.height:
            return True 
          if self.p.x - self.r < world.width and self.p.y + self.r > world.height:
            return True
          if self.p.x + self.r < world.width and self.p.y - self.r < world.height:
            return True
          else:
            return False

            


