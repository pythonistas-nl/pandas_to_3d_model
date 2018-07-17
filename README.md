# README: Pandas to 3D Model #

Pandas to 3D Model is written in Python 3.x.

* Python 3 and libraries

Matplotlib binary dependencies:
https://matplotlib.org/users/installing.html#macos
```shell
$ xcode-select --install
$ # (for subprocess32)
$ python3 -m pip install matplotlib
$ # Docs say...
$ python3 -mpip install -U pip
$ python3 -mpip install -U matplotlib

```

Pandas:
http://pandas.pydata.org/
```shell
$ python3 -m pip install pandas

```

* Usage

```shell
$ source env/bin/activate
$ python3 -m pip install --user '.'
$ python3 -m unittest discover '.'
```

To avoid this:
`Command "python setup.py egg_info" failed with error code 1 in`
Start with:
```bash
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```

* Dependencies

Update local:
```shell
$ # Update
$ pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U

```

Publish into requirements: ``
```shell
$ python3 -m pip freeze >> requirements.txt

```

Backlog
=======

A categorised set of enhancements from random thoughts with only the most brief filter

[x] - Output to Text
[x] - Output to MatPlotLib 3d scatter
[ ] - Output to Wavefront .obj
