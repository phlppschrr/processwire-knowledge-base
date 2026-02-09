# About the /site/modules/ directory

Source: https://processwire.com/docs/modules/about-site-modules/

## Sections


## About the /site/modules/ directory

This directory /site/modules/ is where you may install additional 3rd party plugin modules, or create your own. Modules in this directory are specific to your site only.

There is also a corresponding /wire/modules/ directory which contains ProcessWire's core modules—it's best to leave those ones alone so that you don't lose anything when doing core upgrades.

If safe for your hosting environment, you may wish to make your /site/modules/ directory writable to PHP so that the installation of your modules can be managed from ProcessWire's admin. However, this is not necessarily safe in all shared hosting environments and is completely optional.

To get 3rd party modules for installation, visit [ProcessWire’s modules directory](https://processwire.com/modules/).


### Installing modules from the ProcessWire admin

If your /site/modules/ directory is writable, you can install modules from ProcessWire's admin directly from the Modules Directory, from either a ZIP file or from an https URL to a ZIP file. In your ProcessWire admin, see *Modules > New* for installation options.


### Installing modules from the file system

Each module (and any related files) should live in a directory of its own. The directory should have the same name as the module. For instance, if you are installing a module named `ProcessDatabaseBackups.module`, then it should live in the directory /site/modules/ProcessDatabaseBackups/.

Once you have placed a new module in this directory, you need to let ProcessWire know about it. Login to the admin and click "Modules". Then click the "Check for new modules" button. It will find your new module(s). Click the "Install" button for any new modules that you want to install.


### Removing modules

The first step in removing a module is to uninstall it from ProcessWire (if it isn't already). You do this by going to the "Modules" page, and "Site" tab in your ProcessWire admin. Locate the module you want to remove and click its name (or Config/Settings button, if it has one). On the next screen (the module info/config screen), scroll to the bottom and you should see an "Uninstall" field. Click it to open, check the Uninstall box, and submit the form.

After the module is uninstalled, you may optionally remove the module files. If your modules file system is writable to ProcessWire, it will give you a "Delete" button next to the module in your "Modules" admin page. You may click that to remove the module files.

If your file system is not writable, you may remove the module files manually from the file system (via SFTP or whatever tool you are using to manage your files on the server).


### Interested in learning how to make your own modules?

We've created two "Hello World" modules as examples for those interested in learning module development:

Also check out the [Modules development forum](https://processwire.com/talk/forum/19-moduleplugin-development/).


## Additional resources

- To find and download new modules, see the [modules directory](https://processwire.com/modules/process-hello/).
- For more information about modules, see the [modules documentation](https://processwire.com/docs/modules/).
- For discussion and support of modules, see [modules support forum](https://processwire.com/talk/forum/4-modulesplugins/).
- For commercially developed and supported 1st party modules see [Pro modules](/store/).
