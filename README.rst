To boot up the server from the shell:

.. code-block:: BASH

  cd ./impetus_api
  python manage.py runserver

To debug from VSCode:

.. code-block::JSON

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
