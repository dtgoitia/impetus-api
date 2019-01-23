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

  $ docker run -p 8080:8000

In your browser, navigate to ``localhost:8080`` to see the API up and running!