from abc import ABC, abstractmethod

class PuppyState(ABC):
    """
    Abstract base class defining the interface for different states of a puppy.
    """

    @abstractmethod
    def feed(self, puppy):
        """
        Abstract method to feed the puppy.

        Args:
            puppy (Puppy): The puppy object to be fed.
        """
        pass

    @abstractmethod
    def play(self, puppy):
        """
        Abstract method to play with the puppy.

        Args:
            puppy (Puppy): The puppy object to play with.
        """
        pass
