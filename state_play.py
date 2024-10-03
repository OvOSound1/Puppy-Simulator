from puppy_state import PuppyState

class StatePlay(PuppyState):
    """
    Concrete state class representing the state of a puppy when it is playing.
    """

    def feed(self, puppy):
        """
        Method to simulate feeding the puppy while it is playing.

        Args:
            puppy (Puppy): The puppy object.
        """
        print("\nThe puppy is too busy playing with the ball to eat right now.")

    def play(self, puppy):
        """
        Method to simulate playing with the puppy.

        Args:
            puppy (Puppy): The puppy object.
        """
        if puppy._plays < 1:
            print("\nYou throw the ball again and the puppy excitedly chases it.")
            puppy.inc_plays()  # Increment the count of times the puppy has played
        else:
            from state_asleep import StateAsleep  # Importing StateAsleep to change the puppy's state
            print("\nYou throw the ball again and the puppy excitedly chases it.")
            print("The puppy played so much it fell asleep!")
            puppy.change_state(StateAsleep())  # Change the state of the puppy to asleep
            puppy.reset()  # Reset the counts of feeds and plays for the puppy
