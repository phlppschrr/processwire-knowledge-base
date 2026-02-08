# Introduction to modules

Source: https://processwire.com/docs/modules/intro/

## Summary

Learn about what modules are, what different flavors of modules are available, how to install them, and where to get them.

## Key Points

- Learn about what modules are, what different flavors of modules are available, how to install them, and where to get them.
- At the simplest level, a module is a PHP file containing a class that adheres to ProcessWire’s Module interface. Modules enable a high level of extensibility and customization to ProcessWire. Much of ProcessWire itself is a collection of plugin modules. In fact, the ProcessWire admin application is just a group of modules.
- In ProcessWire, there are Core modules and Site modules. Core modules (stored in /wire/modules/) are modules that are included with the core, many of which come pre-installed since they provide much of the functionality in ProcessWire. On the other hand, Site modules (stored in /site/modules/) are those that you obtain separately (or create) and install yourself.

## Sections


### What are modules?

At the simplest level, a module is a PHP file containing a class that adheres to ProcessWire’s Module interface. Modules enable a high level of extensibility and customization to ProcessWire. Much of ProcessWire itself is a collection of plugin modules. In fact, the ProcessWire admin application is just a group of modules.


### Core modules and site modules

In ProcessWire, there are Core modules and Site modules. Core modules (stored in /wire/modules/) are modules that are included with the core, many of which come pre-installed since they provide much of the functionality in ProcessWire. On the other hand, Site modules (stored in /site/modules/) are those that you obtain separately (or create) and install yourself.


### How modules are installed

Installing a Site module is as simple as uploading the module's files to the /site/modules/ModuleName/ directory on your server (where ModuleName is the name of the module) and then clicking Install in the Admin (Modules > Install). You can also install a module directly from the admin by uploading the ZIP file or providing the URL where it can be downloaded. Uninstalling a module is as simple as clicking Uninstall in the module's settings.


### Where to get modules
