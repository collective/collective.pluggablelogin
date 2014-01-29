Introduction
============

``collective.pluggablelogin`` overrides the standard Plone login form
with a template using a portlet manager, so that various login
components can be configured.

.. image:: https://github.com/collective/collective.pluggablelogin/raw/master/screenshot.png


Configuration
-------------

Go to the Addons control panel and activate "Pluggable Login Page."

Now if you go to ``/login`` while logged in as a Manager, you'll see a
"Manage portlets" link which you can use to manage the available
login portlets. By default, the standard login portlet and a
registration form portlet are enabled (the latter is only shown
if self registration is enabled for the site).

As well as manual assignment via the web interface, the pluggable login
page can also be assigned portlets via GenericSetup, in the same way
as Plone's other portlet managers can. For example, to register a custom
porlet on the pluggable login page, use this an example within ``portlets.xml``
inside a GenericSetup profile:

.. code:: xml

    <portlets
        xmlns:i18n="http://xml.zope.org/namespaces/i18n"
        i18n:domain="plone">
     <assignment 
        name="navigation"
        category="context"
        key="/"
        manager="collective.pluggablelogin"
        type="my.product.portlets.CustomLoginPortlet"
        insert-before="*"
        visible="True">
        <property name="title">string:Login portlet title</property>
        <property name="description">string:Example property</property>
     </assignment>
    </portlets>


Credits
=======

Developed by David Glick and `Groundwire Consulting
<http://groundwireconsulting.com>`_. Sponsored by the `Innocence Project
<http://www.innocenceproject.org/>`_.


To-do
=====

* Refactor inline styles on the logged in or out views.
