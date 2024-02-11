# AgarPYo

AgarPYo is a revisited version of the famous Agar.io game, built entirely using Python's Pygame library. In this solo adaptation, the main objective is to accumulate as many points as possible in 60 seconds while avoiding traps.

## Prerequisites

Make sure you have the specified versions of the following packages installed on your system, as well as Python if you don't use Anaconda.

- Python (version : 3.10.13)
- Pygame (version 2.5.2)
- ...

## Environnement Anaconda

To run this project, make sure you have configured your Anaconda environment with the following specifications.

```yaml
name: AgarPYo
channels:
  - defaults
dependencies:
  - anyio=4.2.0=py310haa95532_0
  - argon2-cffi=21.3.0=pyhd3eb1b0_0
  - argon2-cffi-bindings=21.2.0=py310h2bbff1b_0
  - asttokens=2.0.5=pyhd3eb1b0_0
  - async-lru=2.0.4=py310haa95532_0
  - attrs=23.1.0=py310haa95532_0
  - babel=2.11.0=py310haa95532_0
  - beautifulsoup4=4.12.2=py310haa95532_0
  - bleach=4.1.0=pyhd3eb1b0_0
  - brotli-python=1.0.9=py310hd77b12b_7
  - bzip2=1.0.8=he774522_0
  - ca-certificates=2023.12.12=haa95532_0
  - certifi=2023.11.17=py310haa95532_0
  - cffi=1.16.0=py310h2bbff1b_0
  - charset-normalizer=2.0.4=pyhd3eb1b0_0
  - colorama=0.4.6=py310haa95532_0
  - comm=0.1.2=py310haa95532_0
  - cryptography=41.0.7=py310h89fc84f_0
  - debugpy=1.6.7=py310hd77b12b_0
  - decorator=5.1.1=pyhd3eb1b0_0
  - defusedxml=0.7.1=pyhd3eb1b0_0
  - exceptiongroup=1.2.0=py310haa95532_0
  - executing=0.8.3=pyhd3eb1b0_0
  - idna=3.4=py310haa95532_0
  - ipykernel=6.28.0=py310haa95532_0
  - ipython=8.20.0=py310haa95532_0
  - jedi=0.18.1=py310haa95532_1
  - jinja2=3.1.2=py310haa95532_0
  - json5=0.9.6=pyhd3eb1b0_0
  - jsonschema=4.19.2=py310haa95532_0
  - jsonschema-specifications=2023.7.1=py310haa95532_0
  - jupyter-lsp=2.2.0=py310haa95532_0
  - jupyter_client=8.6.0=py310haa95532_0
  - jupyter_core=5.5.0=py310haa95532_0
  - jupyter_events=0.8.0=py310haa95532_0
  - jupyter_server=2.10.0=py310haa95532_0
  - jupyter_server_terminals=0.4.4=py310haa95532_1
  - jupyterlab=4.0.8=py310haa95532_0
  - jupyterlab_pygments=0.1.2=py_0
  - jupyterlab_server=2.25.1=py310haa95532_0
  - libffi=3.4.4=hd77b12b_0
  - libsodium=1.0.18=h62dcd97_0
  - markupsafe=2.1.3=py310h2bbff1b_0
  - matplotlib-inline=0.1.6=py310haa95532_0
  - mistune=2.0.4=py310haa95532_0
  - nbclient=0.8.0=py310haa95532_0
  - nbconvert=7.10.0=py310haa95532_0
  - nbformat=5.9.2=py310haa95532_0
  - nest-asyncio=1.5.6=py310haa95532_0
  - notebook=7.0.6=py310haa95532_0
  - notebook-shim=0.2.3=py310haa95532_0
  - openssl=3.0.12=h2bbff1b_0
  - overrides=7.4.0=py310haa95532_0
  - packaging=23.1=py310haa95532_0
  - pandocfilters=1.5.0=pyhd3eb1b0_0
  - parso=0.8.3=pyhd3eb1b0_0
  - pip=23.3.1=py310haa95532_0
  - platformdirs=3.10.0=py310haa95532_0
  - powershell_shortcut=0.0.1=3
  - prometheus_client=0.14.1=py310haa95532_0
  - prompt-toolkit=3.0.43=py310haa95532_0
  - prompt_toolkit=3.0.43=hd3eb1b0_0
  - psutil=5.9.0=py310h2bbff1b_0
  - pure_eval=0.2.2=pyhd3eb1b0_0
  - pycparser=2.21=pyhd3eb1b0_0
  - pygments=2.15.1=py310haa95532_1
  - pyopenssl=23.2.0=py310haa95532_0
  - pysocks=1.7.1=py310haa95532_0
  - python=3.10.13=he1021f5_0
  - python-dateutil=2.8.2=pyhd3eb1b0_0
  - python-fastjsonschema=2.16.2=py310haa95532_0
  - python-json-logger=2.0.7=py310haa95532_0
  - pywin32=305=py310h2bbff1b_0
  - pywinpty=2.0.10=py310h5da7b33_0
  - pyyaml=6.0.1=py310h2bbff1b_0
  - pyzmq=25.1.2=py310hd77b12b_0
  - referencing=0.30.2=py310haa95532_0
  - requests=2.31.0=py310haa95532_0
  - rfc3339-validator=0.1.4=py310haa95532_0
  - rfc3986-validator=0.1.1=py310haa95532_0
  - rpds-py=0.10.6=py310h062c2fa_0
  - send2trash=1.8.2=py310haa95532_0
  - setuptools=68.2.2=py310haa95532_0
  - six=1.16.0=pyhd3eb1b0_1
  - sniffio=1.3.0=py310haa95532_0
  - soupsieve=2.5=py310haa95532_0
  - sqlite=3.41.2=h2bbff1b_0
  - stack_data=0.2.0=pyhd3eb1b0_0
  - terminado=0.17.1=py310haa95532_0
  - tinycss2=1.2.1=py310haa95532_0
  - tk=8.6.12=h2bbff1b_0
  - tomli=2.0.1=py310haa95532_0
  - tornado=6.3.3=py310h2bbff1b_0
  - traitlets=5.7.1=py310haa95532_0
  - typing-extensions=4.9.0=py310haa95532_1
  - typing_extensions=4.9.0=py310haa95532_1
  - urllib3=1.26.18=py310haa95532_0
  - vc=14.2=h21ff451_1
  - vs2015_runtime=14.27.29016=h5e58377_2
  - wcwidth=0.2.5=pyhd3eb1b0_0
  - webencodings=0.5.1=py310haa95532_1
  - websocket-client=0.58.0=py310haa95532_4
  - wheel=0.41.2=py310haa95532_0
  - win_inet_pton=1.1.0=py310haa95532_0
  - winpty=0.4.3=4
  - xz=5.4.5=h8cc25b3_0
  - yaml=0.2.5=he774522_0
  - zeromq=4.3.5=hd77b12b_0
  - zlib=1.2.13=h8cc25b3_0
  - pip:
      - numpy==1.26.3
      - pygame==2.5.2
      - pytz==2023.4
      - tzdata==2023.4
```

To configure your Anaconda environment with these specifications, you can create a new environment with conda using the provided environment.yml file.

```bash
conda env create -f environment.yml
```

Make sure to enable this environment before running the project.
```bash
conda activate AgarPYo
```

## Installation

Clone the repository to your local machine.

```bash
git clone https://github.com/B2-Info-23-24/agarpyo-b2-b-quentinmel.git
```

Create a virtual environment (optional, but recommended).

```bash
python -m venv venv
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
```
pip install -r requirements.txt
```

## Use

## Licence
This project is licensed under [MIT](LICENSE).

## Contact
Quentin MELEO

Mail : qmeleo@gmail.com
