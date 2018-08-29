SpectrumOne Movie List
======================

Setting up
----------------------

#### Install git and clone this repo
```bash
$ git clone git@github.com:Jomari-Macaraig/SpectrumOneMovieList.git movielist
```

#### Setup keys.json
##### This is where your configuration is placed
```bash
$ cd movielist/config/settings
$ cp keys.json.sample keys.json
$ vim keys.json
```

#### Install virtualenv, and create and activate virtualenv
```bash
$ sudo pip install virtualenv
$ cd # omit this if you already have a folder for your virtualenv
$ mkdir venv # omit this if you already have a folder for your virtualenv
$ virtualenv venv/spectrumone # change venv to the location of your virtualenv folder if present
$ source venv/spectrumone/bin/active
```

#### Note:
For development you need to copy the `git-pre-commit` file from `movielist/scripts/conf/` folder to
`.git/hooks/pre-commit`
```bash
$ cd movielist
$ cp scripts/conf/git-pre-commit .git/hooks/pre-commit
$ chmod 775 .git/hooks/pre-commit
```

### Running runserver
```bash
$ cd movielist
$ make deploy_dev
```
#### Note:
This only run at port 8000 for the meantime. You can update the Makefile if you want or just run
manually the management command.
