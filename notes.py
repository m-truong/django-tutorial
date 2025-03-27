# VS Code activates the environment automatically when you use the shortcut to activeate the virtual python environment Terminal: Create New Terminal (⌃⇧`).

# In Django terminology, a "Django project" is composed of several site-level configuration files, along with one or more "apps" that you deploy to a web host to create a full web application.

#  A Django project can contain multiple apps, each of which typically has an independent function in the project, and the same app can be in multiple Django projects.

# An app, for its part, is just a Python package that follows certain conventions that Django expects.

# You’ll need to avoid naming projects after built-in Python or Django components. In particular, this means you should avoid using names like django (which will conflict with Django itself) or test (which conflicts with a built-in Python package).

# A subfolder named web_project, which contains the following files:

# __init__.py: an empty file that tells Python that this folder is a Python package.

# asgi.py: an entry point for ASGI-compatible web servers to serve your project. You typically leave this file as-is as it provides the hooks for production web servers.

# settings.py: contains settings for Django project, which you modify in the course of developing a web app.

# urls.py: contains a table of contents for the Django project, which you also modify in the course of development.

# wsgi.py: an entry point for WSGI-compatible web servers to serve your project. You typically leave this file as-is as it provides the hooks for production web servers.

# Note: production-level data store such as PostgreSQL, MySQL, and SQL Server.

#