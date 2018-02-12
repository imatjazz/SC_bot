#!/usr/bin/env python
from project import views
from project import config

# Return an App
if __name__ == "__main__":
	app = views.create_app(debug = config.DEBUG)
	app.run(host=config.HOST, port=config.PORT, threaded=True)
