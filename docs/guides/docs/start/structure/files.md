# Unknown

Source: https://processwire.com/docs/start/structure/files/

An outline of ProcessWire’s file and directory structure, highlighting the locations where your site’s files go, where the core files live, where to place modules, and more.

ProcessWire follows a simple directory structure which aims to do the following:

- 

Keep your site's files and assets completely separate from ProcessWire's, so that you can upgrade your site simply by replacing ProcessWire's core.

- 

Minimizes the impact to your root installation directory, so that everything is clean and doesn't create confusion with other applications you may have installed.

ProcessWire may be installed anywhere on your web server. While it's most common to install it in your web root (/) the software will run just as well under any directory structure.

ProcessWire only creates two directories from your root. This includes /wire and /site. The /wire directory contains the ProcessWire installation and modules, while the /site directory contains everything unique to a given site, including templates, your configuration, stylesheets, scripts, cache files and other assets. This structure is outlined in more detail below.

### Root installation directory (/)

### ### - [/docs/start/structure/](/docs/start/structure/)- [/docs/start/structure/pages/](/docs/start/structure/pages/)- [/docs/start/structure/templates/](/docs/start/structure/templates/)- [/docs/start/structure/fields/](/docs/start/structure/fields/)- [/docs/start/structure/files/](/docs/start/structure/files/)- [/docs/](/docs/)- [/api/ref/](/api/ref/)- [/docs/start/](/docs/start/)- [/docs/front-end/](/docs/front-end/)- [/docs/tutorials/](/docs/tutorials/)- [/docs/selectors/](/docs/selectors/)- [/docs/modules/](/docs/modules/)- [/docs/fields/](/docs/fields/)- [/docs/user-access/](/docs/user-access/)- [/docs/security/](/docs/security/)- [/docs/multi-language-support/](/docs/multi-language-support/)- [/docs/more/](/docs/more/)- [/docs/start/](/docs/start/)- [/docs/start/install/](/docs/start/install/)- [/docs/start/structure/](/docs/start/structure/)- [/docs/start/api/](/docs/start/api/)- [/docs/start/templates/](/docs/start/templates/)- [/docs/start/variables/](/docs/start/variables/)- [/docs/start/api-access/](/docs/start/api-access/)- [/docs/front-end/output/](/docs/front-end/output/)
