# How to install ProcessWire CMS

Source: https://processwire.com/docs/start/install/new/

# Installing ProcessWire 

Information on how to download and install a new copy of ProcessWire from a ZIP file, from GitHub, or with Composer.
- [Installing ProcessWire](#installing-processwire)
  - [Requirements](#requirements)
  - [Installation from ZIP file](#installation-from-zip-file)
  - [Installation from GitHub](#installation-from-github)
  - [Installation with Composer and Packagist](#installation-with-composer-and-packagist)
  - [Other installation options](#other-installation-options)

---
[](#)

## Installing ProcessWire

[](#)

### Requirements

Before installing, please double check that your server meets the following minimum requirements:
- A Unix or Windows-based web server running Apache or 100% compatible.
- PHP 8.x is recommended. PHP 7.1 and newer versions are also supported.
- PDO database support in PHP.
- MySQL 5.6+ or newer (equivalent MariaDB versions also supported).
- Apache must have `mod_rewrite` enabled and must support `.htaccess` files.
- PHP's bundled GD 2 library or ImageMagick library

---
[](#)

### Installation from ZIP file

[Download](/download/core/) the latest version of ProcessWire (ZIP file).

Unzip the ProcessWire installation file to the location where you want it installed on your web server.

Load the location that you unzipped (or uploaded) the files to in your web browser. This will initiate the ProcessWire installer. The installer will guide you through the rest of the installation.

---
[](#)

### Installation from GitHub

Git clone ProcessWire to the place where you want to install it (from the command line):

`git clone https://github.com/processwire/processwire.git`

Load the location where you installed ProcessWire into your browser. This will initiate the ProcessWire installer. The installer will guide you through the rest of the installation.

---
[](#)

### Installation with Composer and Packagist

ProcessWire is available from Packagist and can be installed using Composer by typing the following from the command line:

`composer create-project processwire/processwire`

If you prefer, you can pull ProcessWire into an existing project (which will place it into the /vendor/ directory):

`composer require processwire/processwire`

---
[](#)

### Other installation options

See our [download](/download/core/) page for additional download and installation options.

## 

- [Installation](/docs/start/install/)
- [Install](/docs/start/install/new/)
- [Upgrade](/docs/start/install/upgrade/)
- [Troubleshoot](/docs/start/install/troubleshooting/)

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
