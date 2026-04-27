# AI Car Simulation

A NEAT-based neuroevolution self-driving car simulation using pygame.


## Features

- NEAT neuroevolution training with a configurable population
- Replay mode — load and watch the best saved genome
- Manual mode — drive a car yourself using the keyboard
- Photo mode — screenshots, pause, cinematic letterbox, HUD toggle
- Simulation speed control (0.25x – 8x)
- Generation transition overlay
- Per-generation metrics saved as JSON and CSV
- 477 headless pytest tests across all layers

### Training
NEAT evolves a population of neural-network drivers over many generations.
Genomes and metrics are saved after training completes or
when you return to the menu with Q.




