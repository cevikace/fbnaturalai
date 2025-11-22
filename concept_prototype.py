"""
Meadow Glide prototype scaffolding using Pygame-style structures.
This file outlines the primary systems for a peaceful, nature-themed
Flappy-like game. It focuses on readability and separation of concerns.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Tuple


class TimeOfDay(Enum):
    DAWN = auto()
    DAY = auto()
    DUSK = auto()
    NIGHT = auto()


@dataclass
class PhysicsConfig:
    gravity: float = 900.0
    flap_impulse: float = -320.0
    max_fall_speed: float = 650.0


@dataclass
class GapCurve:
    start_gap: int = 220
    min_gap: int = 140
    shrink_rate: float = 0.15

    def gap_for_score(self, score: int) -> int:
        """Compute the current gap size based on score progression."""
        gap = self.start_gap - int(score * self.shrink_rate)
        return max(self.min_gap, gap)


@dataclass
class PlayerState:
    y: float
    y_velocity: float = 0.0
    alive: bool = True
    character: str = "butterfly"  # butterfly | bee | chickadee


@dataclass
class Obstacle:
    x: float
    gap_center: float
    gap_size: float
    style: str  # vine | branch | stem


class AmbientAudio:
    def __init__(self) -> None:
        self.music_volume = 0.4
        self.ambient_volume = 0.35
        self.channels = {"music": None, "wind": None, "birds": None}

    def update_mix(self, time_of_day: TimeOfDay) -> None:
        """Pseudo-logic for adapting ambience to time of day."""
        if time_of_day in {TimeOfDay.DUSK, TimeOfDay.NIGHT}:
            self.channels["birds"] = "crickets"
        else:
            self.channels["birds"] = "songbirds"


class MeadowGlideGame:
    """High-level game container for update/draw loops."""

    def __init__(self, physics: PhysicsConfig, gaps: GapCurve) -> None:
        self.physics = physics
        self.gaps = gaps
        self.time_of_day = TimeOfDay.DAWN
        self.player = PlayerState(y=320)
        self.obstacles: List[Obstacle] = []
        self.score = 0
        self.ambient = AmbientAudio()

    # --- Input & physics ---
    def flap(self) -> None:
        if self.player.alive:
            self.player.y_velocity = self.physics.flap_impulse

    def apply_gravity(self, dt: float) -> None:
        if not self.player.alive:
            return
        self.player.y_velocity = min(
            self.player.y_velocity + self.physics.gravity * dt,
            self.physics.max_fall_speed,
        )
        self.player.y += self.player.y_velocity * dt

    # --- Obstacles ---
    def spawn_obstacle(self, x: float) -> None:
        gap_size = self.gaps.gap_for_score(self.score)
        gap_center = 200 + (self.score * 3) % 180
        style = self._choose_obstacle_style()
        self.obstacles.append(Obstacle(x=x, gap_center=gap_center, gap_size=gap_size, style=style))

    def _choose_obstacle_style(self) -> str:
        # Rotate through natural styles for visual variety.
        styles = ["vine", "branch", "stem"]
        return styles[self.score % len(styles)]

    # --- Progression ---
    def advance_time_of_day(self) -> None:
        order = [TimeOfDay.DAWN, TimeOfDay.DAY, TimeOfDay.DUSK, TimeOfDay.NIGHT]
        idx = (order.index(self.time_of_day) + 1) % len(order)
        self.time_of_day = order[idx]
        self.ambient.update_mix(self.time_of_day)

    # --- Collision and scoring ---
    def check_collision(self, player_y: float, obstacle: Obstacle) -> bool:
        half_gap = obstacle.gap_size / 2
        return not (obstacle.gap_center - half_gap <= player_y <= obstacle.gap_center + half_gap)

    def update_score(self, passed: int) -> None:
        self.score += passed

    # --- Debug/utility ---
    def debug_state(self) -> Tuple[int, str, TimeOfDay]:
        return self.score, self.player.character, self.time_of_day


if __name__ == "__main__":
    physics = PhysicsConfig()
    gaps = GapCurve()
    game = MeadowGlideGame(physics, gaps)
    game.spawn_obstacle(x=600)
    game.flap()
    game.apply_gravity(dt=0.016)
    game.advance_time_of_day()
    print(game.debug_state())
