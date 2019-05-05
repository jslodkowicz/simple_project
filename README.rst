Simple Flask Weather App
========================

.. image:: https://travis-ci.org/jslodkowicz/simple_project.svg?branch=master
    :target: https://travis-ci.org/jslodkowicz/simple_project

.. image:: https://app.statuscake.com/button/index.php?Track=4007025&Days=1&Design=6
    :target: https://app.statuscake.com/

Prosta aplikacja wyświetlająca aktualną pogodę w podanym mieście

- Tworzymy, aktywujemy i konfigurujemy wirtualne środowisko:

  ::

    virtualenv venv
    source venv/bin/activate
    make deps

- Uruchamianie aplikacji:

  ::

    make run

- Uruchamianie testów

  ::

    make test
    make test_smoke

- Sprawdzanie pokrycia i code complexity

  ::

    make test_cov
    make test_xunit
    make test_code_complexity

- Uruchamianie / Zatrzymywanie Dockera

  ::

    make docker_run
    make docker_stop

- Deployment do Dockera

  ::

    make docker_push

Aplikacja jest automatycznie deployowana do `Heroku <https://dry-caverns-25266.herokuapp.com/>`_ z Travis-CI.

Aplikacja jest monitorowana w odstępach 5-minutowych przez Statuscake.
