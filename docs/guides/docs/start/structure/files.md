# ProcessWire’s file and directory structure

Source: https://processwire.com/docs/start/structure/files/

## Summary

An outline of ProcessWire’s file and directory structure, highlighting the locations where your site’s files go, where the core files live, where to place modules, and more.

## Key Points

- An outline of ProcessWire’s file and directory structure, highlighting the locations where your site’s files go, where the core files live, where to place modules, and more.
- ProcessWire follows a simple directory structure which aims to do the following:
- Keep your site's files and assets completely separate from ProcessWire's, so that you can upgrade your site simply by replacing ProcessWire's core.

## Sections


### Root installation directory (/)

- /.htaccess — Required directives to Apache
- /index.php — Bootstrap index file
- /install.php — Installation script (you should delete this after installation)


### Core and modules (/wire/)

- /wire/core/ — ProcessWire core
- /wire/modules/ — Default plugin modules
- /wire/templates-admin/ — Templates, stylesheets and scripts for the admin control panel

Note: To upgrade ProcessWire, you simply replace the entire /wire/ directory with that of the new version.


### All files unique to a given site (/site/)

- /site/config.php — Your site's configuration file
- /site/assets/ — All writable assets including files, images, cache files, logs and temporary files created by ProcessWire.
- /site/install/ — Installation profile. You should delete this directory after installation.
- /site/modules/ — Any plugin modules unique to a given site (optional).
- /site/templates/ — Template files specific to your site
- /site/templates/styles/ — CSS files specific to your site. You may locate this directory elsewhere, and/or rename it, if you prefer.
- /site/templates/scripts/ — Javascript files specific to your site. You may locate this directory elsewhere, and/or rename it, if you prefer.
