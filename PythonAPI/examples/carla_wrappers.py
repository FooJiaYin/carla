import gym
import numpy as np
from gym import spaces
import cv2


class WarpFrame(gym.ObservationWrapper):
    def __init__(self, env: gym.Env, width: int = 160, height: int = 90):
        gym.ObservationWrapper.__init__(self, env)
        self.width = width
        self.height = height
        self.observation_space = spaces.Box(
            low=0, high=255, shape=(self.height, self.width, 3), dtype=env.observation_space.dtype
        )

    def observation(self, frame: np.ndarray) -> np.ndarray:
        if frame is not None:
            frame = cv2.resize(frame, (self.width, self.height), interpolation=cv2.INTER_AREA)
        else:
            frame = np.zeros((self.height, self.width, 3))
        return frame

class CarlaWrapper(gym.Wrapper):
    def __init__(
        self,
        env: gym.Env,
        screen_width: int = 160,
        screen_height: int = 90,
    ):
        env = WarpFrame(env, width=screen_width, height=screen_height)

        super(CarlaWrapper, self).__init__(env)