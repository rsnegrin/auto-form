# auto-form
Script que completa automaticamente el form de CV19 UC

## Drivers
En settings -> buildpacks de heroku agregar:

- heroku/python

- https://github.com/heroku/heroku-buildpack-chromedriver

- https://github.com/heroku/heroku-buildpack-google-chrome

## Variables de entorno

- campus:  3
- lugar: Ingeniería
- username: _usuario uc_
- password: _password uc_

- CHROMEDRIVER_PATH: /app/.chromedriver/bin/chromedriver
- GOOGLE_CHROME_BIN: /app/.apt/usr/bin/google-chrome

Campus 3 corresponde a SJ
## Scheduler
Agregar el add-on **Advanced Scheduler**: https://elements.heroku.com/addons/advanced-scheduler 

Setear la task con corn syntax.
