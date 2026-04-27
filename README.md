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


### Replay
Loads the best saved genome  and runs it on the selected track. 

### Manual
Drive a car yourself using the arrow keys. 

## Project Goals

- Refactor the monolithic prototype into a clean, modular Python package
- Separate concerns across domain, core, AI, UI, simulation, analytics, and persistence layers
- Establish a comprehensive test suite (477 tests, all headless)
- Support training, replay, and manual-drive modes via a shared `DriverInterface`
- Provide photo mode and presentation tools for academic demos and reports