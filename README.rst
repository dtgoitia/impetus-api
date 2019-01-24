To boot up the server from the shell:

.. code-block :: bash

  $ cd ./impetus_api
  $ python manage.py runserver

To debug from VSCode:

.. code-block :: json

  {
    "version": "0.2.0",
    "configurations": [
      {
        "name": "Python: Django",
        "type": "python",
        "request": "launch",
        "program": "${workspaceFolder}/impetus_api/manage.py",
        "console": "integratedTerminal",
        "args": [
          "runserver",
          "--noreload",
          "--nothreading"
        ],
        "django": true
      }
    ]
  }


Setup database:

.. code-block :: bash

  $ python manage.py migrate                 # Run migration steps
  $ python manage.py makemigrations presets  # Update our migration steps
  $ python manage.py migrate                 # Run migration steps once more

Build Docker image:

.. code-block :: bash

  $ docker build --tag impetus-api .

Run built image (``impetus-api``) and expose it on the port ``8080``:

.. code-block :: bash

  $ docker run -p 8080:8000 impetus-api

Navigate in your browser to localhost:8080_ to see the AgPI up and running!

.. _localhost:8080: http://localhost:8080

Remember to kill the container once you finish:

.. code-block :: bash

  $ docker container ls
  CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
  fcdadb5b64ff        impetus-api         "python manage.py ru…"   16 minutes ago      Up 16 minutes       0.0.0.0:8080->8000/tcp   compassionate_goodall

  $ docker container kill fcdadb5b64ff
  fcdadb5b64ff
