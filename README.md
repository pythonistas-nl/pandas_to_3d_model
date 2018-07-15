# README: Pandas to FBX #

Pandas to FBX is written in Python 3.x.

To avoid this: `Command "python setup.py egg_info" failed with error code 1 in`
Start with:
```bash
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```

* Python 3 and libraries:
     - Matplotlib binary dependencies
     - http://pyyaml.org/wiki/PyYAMLDocumentation `python3 -m pip install pyyaml`
     - http://pandas.pydata.org/ `python3 -m pip install pandas`

* Update all: `pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U`

*Usage:*
```shell
$ source env/bin/activate
$ python3 -m pip install '.'
$ python3 -m pip freeze >> requirements.txt
$ python -m unittest discover test/unit

```

Contribution guidelines
-----------------------

Contributions are welcome which add value and comply with a consistent set of standards. 

* Writing tests
* Code review
* Other guidelines

The standards are enforced by the build and these shall evolve just like the code. A commit which changes the standards shall be merged including only changes necessary to comply with the change in standards. A losening of standards would then only contain the change to losen the standards.

Further information
-------------------

See: https://polycode.co.uk/

Backlog
=======

A categorised set of enhancements from random thoughts with only the most brief filter
