# Asteroids Game

<video src="https://github.com/user-attachments/assets/f0d81675-124d-40ff-b7c4-941f72f8d1c5" controls autoplay muted loop ></video>

## Prerequisites

As per [boot.dev](https://www.boot.dev/lessons/5be3e3bd-efb5-4664-a9e9-7111be783271), install these:
* Python 3.10+ installed
* The [uv](https://docs.astral.sh/uv/getting-started/installation/) project manager

## Setup

1. Download files:
    ``` bash 
    git clone https://github.com/TQafko/Asteroids-Game.git
    ```

2. Run these commands:
    ```bash
    uv venv --python 3.12
    source .venv/bin/activate
    uv pip install pygame
    ```

3. Run the game:
    ```bash
    uv run main.py
    ```