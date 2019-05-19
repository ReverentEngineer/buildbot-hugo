buildbot-hugo: A Hugo build step for Buildbot
==================================================

.. image:: https://travis-ci.org/ReverentEngineer/buildbot-hugo.svg?branch=master
    :target: https://travis-ci.org/ReverentEngineer/buildbot-hugo

:Site:  https://github.com/ReverentEngineer/buildbot-hugo
:Original author: Jeff Hill <jeff@reverentengineer.com>


.. contents::
   :local:


buildbot-hugo is a build step plugin to support Hugo for Buildbot.


Requirements
------------

Required packages include: buildbot

How to run
-------------

.. code-block:: python

    from buildbot.plugins import steps
    ...
    factory.addStep(steps.Hugo())
