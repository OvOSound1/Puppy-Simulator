from puppy_state import PuppyState

class StateEat(PuppyState):
    """
    Concrete state class representing the state of a puppy when it is eating.
    """

    def feed(self, puppy):
        """
        Method to feed the puppy.

        Args:
            puppy (Puppy): The puppy object to be fed.
        """
        if puppy._feeds < 1:
            print("\nThe puppy continues to eat as you add another scoop of kibble to its bowl.")
            puppy.inc_feeds()  # Increment the count of feeds given to the puppy
        else:
            from state_asleep import StateAsleep  # Importing StateAsleep to change the puppy's state
            print("\nThe puppy continues to eat as you add another scoop of kibble to its bowl.")
            print("The puppy ate so much it fell asleep!")
            puppy.change_state(StateAsleep())  # Change the state of the puppy to asleep
            puppy.reset()  # Reset the counts of feeds and plays for the puppy

    def play(self, puppy):
        """
        Method to simulate playing with the puppy while it is eating.

        Args:
            puppy (Puppy): The puppy object.
        """
        from state_play import StatePlay  # Importing StatePlay to change the puppy's state
        print("\nThe puppy looks up from its food and chases the ball you threw.")
        puppy.change_state(StatePlay())  # Change the state of the puppy to playing
        puppy.reset()  # Reset the counts of feeds and plays for the puppy
