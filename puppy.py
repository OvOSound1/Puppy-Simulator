from state_asleep import StateAsleep

class Puppy:
    """
    Class representing a virtual puppy and its behavior.
    """

    def __init__(self):
        """
        Constructor method for creating a new Puppy instance.
        """
        self._state = StateAsleep()  # Set the initial state of the puppy to asleep
        self._feeds = 0  # Initialize the number of times the puppy has been fed
        self._plays = 0  # Initialize the number of times the puppy has played

    def change_state(self, new_state):
        """
        Method to change the state of the puppy.

        Args:
            new_state (PuppyState): The new state to set for the puppy.
        """
        self._state = new_state

    def throw_ball(self):
        """
        Method to simulate playing with the puppy by throwing a ball.
        """
        self._state.play(self)

    def give_food(self):
        """
        Method to simulate feeding the puppy.
        """
        self._state.feed(self)

    def inc_feeds(self):
        """
        Method to increment the count of feeds given to the puppy.
        """
        self._feeds += 1

    def inc_plays(self):
        """
        Method to increment the count of times the puppy has played.
        """
        self._plays += 1

    def reset(self):
        """
        Method to reset the counts of feeds and plays for the puppy.
        """
        self._feeds = 0
        self._plays = 0
