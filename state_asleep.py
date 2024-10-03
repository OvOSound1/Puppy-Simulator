from puppy_state import PuppyState

class StateAsleep(PuppyState):
    """
    Concrete state class representing the state of a puppy when it is asleep.
    """

    def feed(self, puppy):
        """
        Method to feed the puppy when it is asleep.

        Args:
            puppy (Puppy): The puppy object to be fed.
        """
        from state_eat import StateEat  # Importing StateEat to change the puppy's state
        print("\nThe puppy wakes up and comes running to eat.")
        puppy.change_state(StateEat())  # Change the state of the puppy to eating
        puppy.reset()  # Reset the counts of feeds and plays for the puppy

    def play(self, puppy):
        """
        Method to simulate playing with the puppy when it is asleep.

        Args:
            puppy (Puppy): The puppy object.
        """
        print("\nThe puppy is asleep. It doesn't want to play right now.")
