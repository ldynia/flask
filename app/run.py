import os

from app import create_app


app = create_app()

# Prevent circular dependency
from app.modules.demo.hello import *

# link: https://stackoverflow.com/questions/34615743/unable-to-load-configuration-from-uwsgi#answer-37175998
if __name__ == "__main__":
    PORT = os.getenv('PORT', 80)
    HOST = os.getenv('HOST', '0.0.0.0')

    app.run(host=HOST, port=PORT, threaded=True)
