Run the API
===========

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


Run the API with Docker
=======================

First time instructions
-----------------------

1. Build Docker image from Dockerfile and tag the new image as ``impetus_api``:

    .. code-block :: bash

      $ docker build --tag impetus-api .

2. Create container called ``impetus-api`` from the ``impetus-api`` image, expose it on the port ``8080`` and run the container:

    .. code-block :: bash

      $ docker run -p 8080:8000 --name impetus-api impetus-api

3. Navigate in your browser to localhost:8080_ to see the API up and running!

.. _localhost:8080: http://localhost:8080


Stop your container
-------------------

Remember to stop the container once you finish. You can do it by its name ``impetus-api``:

.. code-block :: bash

  $ docker container stop impetus-api
  impetus-api


Start your container
--------------------

Once you have created (with ``docker run``) a container, is not necessary to create new containers. You can re-start your container by its name ``impetus-api``:

.. code-block :: bash

  $ docker container start impetus-api
  impetus-api