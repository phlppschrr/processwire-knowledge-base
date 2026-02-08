# ProcessWire file system structure

Source: https://processwire.com/docs/start/structure/files/

# ProcessWire’s file and directory structure 

An outline of ProcessWire’s file and directory structure, highlighting the locations where your site’s files go, where the core files live, where to place modules, and more.

ProcessWire follows a simple directory structure which aims to do the following:
- 

Keep your site's files and assets completely separate from ProcessWire's, so that you can upgrade your site simply by replacing ProcessWire's core.
- 

Minimizes the impact to your root installation directory, so that everything is clean and doesn't create confusion with other applications you may have installed.

ProcessWire may be installed anywhere on your web server. While it's most common to install it in your web root (/) the software will run just as well under any directory structure.

ProcessWire only creates two directories from your root. This includes /wire and /site. The /wire directory contains the ProcessWire installation and modules, while the /site directory contains everything unique to a given site, including templates, your configuration, stylesheets, scripts, cache files and other assets. This structure is outlined in more detail below.

### Root installation directory (/)

| /.htaccess | Required directives to Apache |
| --- | --- |
| /index.php | Bootstrap index file |
| /install.php | Installation script (you should delete this after installation) |

### Core and modules (/wire/)

| /wire/core/ | ProcessWire core |
| --- | --- |
| /wire/modules/ | Default plugin modules |
| /wire/templates-admin/ | Templates, stylesheets and scripts for the admin control panel |

Note: To upgrade ProcessWire, you simply replace the entire /wire/ directory with that of the new version.

### All files unique to a given site (/site/)

| /site/config.php | Your site's configuration file |
| --- | --- |
| /site/assets/ | All writable assets including files, images, cache files, logs and temporary files created by ProcessWire. |
| /site/install/ | Installation profile. You should delete this directory after installation. |
| /site/modules/ | Any plugin modules unique to a given site (optional). |
| /site/templates/ | Template files specific to your site |
| /site/templates/styles/ | CSS files specific to your site. You may locate this directory elsewhere, and/or rename it, if you prefer. |
| /site/templates/scripts/ | Javascript files specific to your site. You may locate this directory elsewhere, and/or rename it, if you prefer. |

Note: The /site/templates/ directory is the most used directory in developing a site.
- [Structure](/docs/start/structure/)
- [Pages](/docs/start/structure/pages/)
- [Templates](/docs/start/structure/templates/)
- [Fields](/docs/start/structure/fields/)
- [File system](/docs/start/structure/files/)

- [Docs](/docs/)
- [API reference](/api/ref/)
- [Getting started](/docs/start/)
- [Front-end](/docs/front-end/)
- [Tutorials](/docs/tutorials/)
- [Selectors](/docs/selectors/)
- [Modules & hooks](/docs/modules/)
- [Fields, types, input](/docs/fields/)
- [Access control](/docs/user-access/)
- [Security](/docs/security/)
- [Multi-language](/docs/multi-language-support/)
- [More topics](/docs/more/)

- [Getting started](/docs/start/)
- [Installation](/docs/start/install/)
- [Structure](/docs/start/structure/)
- [About the API](/docs/start/api/)
- [Template files](/docs/start/templates/)
- [API variables](/docs/start/variables/)
- [API access](/docs/start/api-access/)
- [Output strategies](/docs/front-end/output/)
