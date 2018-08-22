# [brain&middot;f](https://github.com/bzaczynski/brainf)

Yet another [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) interpreter written in Python.

For sample programs navigate to [esolangs wiki](https://esolangs.org/wiki/Brainfuck) or [here](http://www.hevanet.com/cristofd/brainfuck/).

## Usage

Run directly as a shell script:
```shell
$ cat > file.b
#!/usr/bin/env brainfuck.py
++++++++++[>++++++<-]>+++++.
^D
$ chmod +x file.b
$ ./file.b
A
```

Run as a Python script:
```shell
$ brainfuck.py /path/to/file.b
```

Run as a Python module:
```shell
$ python -m brainf /path/to/file.b
```

Run as a Python Executable (PEX):
```shell
$ python brainf-linux.pex /path/to/file.b
```

Run as a platform-specific native executable:
```shell
$ ./brainfuck /path/to/file.b
```

See technical [documentation](http://brainf.readthedocs.io/en/latest/) for more details.

## Download

Source code:

```shell
$ git clone https://github.com/bzaczynski/brainf.git
```

## Installation

In a new virtual environment:

```shell
$ pip install .
```

To uninstall:

```shell
$ pip uninstall brainf
```

## Building

### Executable

Using [PyInstaller](https://www.pyinstaller.org/) will create a platform-specific executable file which bundles Python interpreter as well as all the required libraries.

```shell
$ mkvirtualenv brainf
$ pip install . pyinstaller
$ pyinstaller --onefile --additional-hooks-dir src/brainf bin/brainfuck.py
```

Usage:

```shell
$ dist/brainfuck samples/hello.b
Hello World!
```

### Binary Distribution

To build a binary distribution with [Docker](https://www.docker.com/) and [PEX](https://pypi.org/project/pex/) follow the steps below.

1. Create a new Docker image.
```shell
$ docker build -t brainf:linux -f Dockerfile.linux .
```

2. Run interim container to extract .pex file from the image.
```shell
$ docker run --rm brainf:linux cat /root/brainf-1.0.0-linux.pex > brainf-linux.pex
```

### Documentation

To build Sphinx documentation:

```shell
$ cd docs/
$ make clean html
```

## Publishing

The recommended way to publish a project on [PyPI](https://pypi.org/) is with [twine](https://github.com/pypa/twine) since it uses SSL by default.

1. Install twine:
```shell
$ pip install twine
```

2. Create source and binary distributions:
```shell
$ python setup.py sdist bdist_wheel
```

3. Upload to Python Package Index.

    Test PyPI:
    ```shell
    $ twine upload --repository-url https://test.pypi.org/legacy/ dist/*
    ```
    PyPI:
    ```shell
    $ twine upload dist/*
    ```

## License

This project is licensed under the [MIT License](https://raw.githubusercontent.com/bzaczynski/brainf/master/LICENSE).
