# About the /site/modules/ directory

Source: https://processwire.com/docs/modules/about-site-modules/

## Summary

This directory /site/modules/ is where you may install additional 3rd party plugin modules, or create your own. Modules in this directory are specific to your site only.

## Key Points

- This directory /site/modules/ is where you may install additional 3rd party plugin modules, or create your own. Modules in this directory are specific to your site only.
- There is also a corresponding /wire/modules/ directory which contains ProcessWire's core modules—it's best to leave those ones alone so that you don't lose anything when doing core upgrades.
- If safe for your hosting environment, you may wish to make your /site/modules/ directory writable to PHP so that the installation of your modules can be managed from ProcessWire's admin. However, this is not necessarily safe in all shared hosting environments and is completely optional.

## Sections


### Installing modules from the ProcessWire admin

If your /site/modules/ directory is writable, you can install modules from ProcessWire's admin directly from the Modules Directory, from either a ZIP file or from an https URL to a ZIP file. In your ProcessWire admin, see Modules > New for installation options.


### Installing modules from the file system

Each module (and any related files) should live in a directory of its own. The directory should have the same name as the module. For instance, if you are installing a module named ProcessDatabaseBackups.module, then it should live in the directory /site/modules/ProcessDatabaseBackups/.


### Removing modules

The first step in removing a module is to uninstall it from ProcessWire (if it isn't already). You do this by going to the "Modules" page, and "Site" tab in your ProcessWire admin. Locate the module you want to remove and click its name (or Config/Settings button, if it has one). On the next screen (the module info/config screen), scroll to the bottom and you should see an "Uninstall" field. Click it to open, check the Uninstall box, and submit the form.


### Interested in learning how to make your own modules?

We've created two "Hello World" modules as examples for those interested in learning module development:


## Additional resources
