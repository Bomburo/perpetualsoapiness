heroku buildpacks:clear
heroku buildpacks:add --index heroku/python
heroku ps:scale web=1

web: python server.py
worker: python get-soaps.py