# AgarPYo

AgarPYo is a revisited version of the famous Agar.io game, built entirely using Python's Pygame library. In this solo adaptation, the main objective is to accumulate as many points as possible in 60 seconds while avoiding traps.

## Prerequisites

Make sure you have installed the following software and package versions.

- Python (version : 3.10.13)
- Pygame (version 2.5.2)

## Installation (without Anaconda)

Clone the repository to your local machine.

```bash
git clone https://github.com/B2-Info-23-24/agarpyo-b2-b-quentinmel.git
```

Go to the project.

```bash
cd agarpyo-b2-b-quentinmel
```

Create a file named requirements.txt whith this following content.

```txt
pygame==2.5.2
```

Create a virtual environment (optional, but recommended).

```bash
py -m venv venv
```

Enable the virtual environment.

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

Install the dependencies with pip from the requirements.txt file.

```bash
pip install -r requirements.txt
```

## Environnement Anaconda

If you want to launch with [Anaconda](https://www.anaconda.com/products/distribution), make sure you have configured your Anaconda environment with the following specifications.

Clone the repository to your local machine.

```bash
git clone https://github.com/B2-Info-23-24/agarpyo-b2-b-quentinmel.git
```

Go to the project.

```bash
cd agarpyo-b2-b-quentinmel
```

Create a file named environment.yaml whith this following content.

```yaml
name: AgarPYo
channels:
  - defaults
dependencies:
  - bzip2=1.0.8=he774522_0
  - ca-certificates=2023.12.12=haa95532_0
  - libffi=3.4.4=hd77b12b_0
  - openssl=3.0.13=h2bbff1b_0
  - pip=23.3.1=py310haa95532_0
  - python=3.10.13=he1021f5_0
  - setuptools=68.2.2=py310haa95532_0
  - sqlite=3.41.2=h2bbff1b_0
  - tk=8.6.12=h2bbff1b_0
  - tzdata=2023d=h04d1e81_0
  - vc=14.2=h21ff451_1
  - vs2015_runtime=14.27.29016=h5e58377_2
  - wheel=0.41.2=py310haa95532_0
  - xz=5.4.5=h8cc25b3_0
  - zlib=1.2.13=h8cc25b3_0
  - pip:
      - pygame==2.5.2
```

To configure your Anaconda environment with these specifications, you can create a new environment with conda using the provided environment.yaml file.

```bash
conda env create -f environment.yaml
```

Make sure to enable this environment before running the project.
```bash
conda activate AgarPYo
```

## Use

To launch the application without Anaconda, enter the command.

```bash
py main.py
```

To launch the application with Anaconda, enter the command.

```bash
python main.py
```

## Features

You have three difficulty choices.

  - ### Easy
    2 traps and 5 foods
  - ### Normal
    3 traps and 3 foods
  - ### Hard
    4 traps and 2 foods


You can choose to play with the keyboard (ZQSD : z keys to go up, q to go left, s to go down and d to go right) or play with the cursor.

If the player's height is smaller than the size of the trap, then the player will be able to hide under the trap and nothing will happen. If the player's size is greater than the size of the trap, then the player will have their size and speed divided by the number corresponding to the selected difficulty: 2 for easy, 3 for normal and 4 for hard.

You have 60 seconds to amass as many scores as possible which increases by 1 for each food eaten.

At the end of its 60 seconds, a page appears with your score and your difficulty then you will have the choice between leaving the application or returning to the menu.

If the player reaches the edge of the map, he is automatically teleported in the same direction to the other side of the map.

In the menu, if you press the P key this will make you launch the game with the keyboard and if you press the Q key this will exit the application.

In the middle of the game, the Escape button allows you to return to the main menu

## Licence
This project is licensed under [MIT](LICENSE).

## Contact
Quentin MELEO

Mail : qmeleo@gmail.com
