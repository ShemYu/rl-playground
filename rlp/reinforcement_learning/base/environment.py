import abc


class BaseEnvironment(abc.ABC):
    """BaseEnvironment defines the basic functionality of an environment in reinforcement learning.

    This abstract base class should be implemented with methods that simulate the environment's dynamics,
    providing a way for an agent (actor) to interact with the environment using actions and to receive
    feedback in the form of observations and rewards.

    The environment is responsible for tracking the current state and providing the next state and reward
    given an action. It also indicates when an episode (or trial) has ended.

    Methods to be implemented by any subclass:
    - reset(self): Resets the environment to an initial state and returns the initial observation.
    - step(self, action): Applies an action to the environment, returns the next state, reward, done (whether
      the episode has ended), and optional additional information."""
    pass
