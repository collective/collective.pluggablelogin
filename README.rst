Introduction
============

``collective.pluggablelogin`` overrides the standard Plone login form
with a template using a portlet manager, so that various login
components can be configured.

.. image:: https://github.com/davisagli/collective.pluggablelogin/raw/master/screenshot.png

Configuration
-------------

Go to the Addons control panel and activate "Pluggable Login Page."

Now if you go to /login while logged in as a Manager, you'll see a
"Manage portlets" link which you can use to manage the available
login portlets. By default the standard login portlet and a
registration form portlet are enabled (the latter is only shown
if self registration is enabled for the site).

Credits
=======

Developed by David Glick and `Groundwire Consulting <http://groundwireconsulting.com>`_. Sponsored by the `Innocence Project <http://www.innocenceproject.org/>`_.