# Unknown

Source: https://processwire.com/docs/modules/intro/

Learn about what modules are, what different flavors of modules are available, how to install them, and where to get them.

### What are modules?

At the simplest level, a module is a PHP file containing a class that adheres to ProcessWire’s *Module* interface. Modules enable a high level of extensibility and customization to ProcessWire. Much of ProcessWire itself is a collection of plugin modules. In fact, the ProcessWire admin application is just a group of modules.

### Core modules and site modules

In ProcessWire, there are *Core modules* and *Site modules*. Core modules (stored in /wire/modules/) are modules that are included with the core, many of which come pre-installed since they provide much of the functionality in ProcessWire. On the other hand, *Site modules* (stored in /site/modules/) are those that you obtain separately (or create) and install yourself.

### How modules are installed

Installing a Site module is as simple as uploading the module's files to the /site/modules/ModuleName/ directory on your server (where *ModuleName* is the name of the module) and then clicking *Install* in the Admin (Modules > Install). You can also install a module directly from the admin by uploading the ZIP file or providing the URL where it can be downloaded. Uninstalling a module is as simple as clicking *Uninstall* in the module's settings.

ProcessWire also comes with many Core modules that are not pre-installed, but are ready for 1-click installation. These can be listed and installed by navigating in the admin to Modules > Core.

### Where to get modules

ProcessWire itself comes with many modules. The modules that are most likely to be used in all installations come pre-installed, while modules that are likely to be used in at least 30% of installations may not be pre-installed, but are included with the core and installable with one click (see Modules > Core). Many free third-party modules are available for from the [modules directory](https://modules.processwire.com). Several [Pro modules](/docs/modules/pro/) (a type of commercial module developed by the lead developer of ProcessWire) are also available. You can also create your own modules, which is simple to do—see our section on [module development](../development/).

- [Modules & hooks](/docs/modules/)
- [Introduction to modules](/docs/modules/intro/)
- [Module development](/docs/modules/development/)
- [Module types](/docs/modules/types/)
- [Using hooks](/docs/modules/hooks/)
- [Pro modules](/store/)
- [About the /site/modules/ directory](/docs/modules/about-site-modules/)
- [Third-party modules](https://modules.processwire.com)

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

[Module development](/docs/modules/development/)
