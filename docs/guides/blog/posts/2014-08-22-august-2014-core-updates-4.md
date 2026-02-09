# August 2014 Core Updates #4

Source: https://processwire.com/blog/posts/august-2014-core-updates-4/

## Sections


## August 2014 Core Updates #4

22 August 2014 by Ryan Cramer [ 1 Comment](/blog/posts/august-2014-core-updates-4/#comments)


### Database backup capability now in the core

A new class called [WireDatabaseBackup](https://github.com/ryancramerdesign/ProcessWire/blob/dev/wire/core/WireDatabaseBackup.php) has been added to the core. It provides an easy way to backup and/or restore from the API. To make a new backup file you can do this:

```
$file = $database->backups()->backup();
```

To restore a backup file, you can do this:

```
$database->backups()->restore($file);
```

Both the backup() and restore() methods also accept several options for limiting the backup to certain tables, adding annotations and more. For details, see [backup options](https://github.com/ryancramerdesign/ProcessWire/blob/dev/wire/core/WireDatabaseBackup.php#L44) and [restore options](https://github.com/ryancramerdesign/ProcessWire/blob/dev/wire/core/WireDatabaseBackup.php#L91).

Plans for the WireDatabaseBackup class are for it to be used by our main installer. It will also provide future backup options before making changes to fields, templates or modules, so that you have undo capability. A future automated upgrade utility for the core will also be using the backups function.

Please note that the restore function is only designed to restore backups created by the backup function. While it may also work with other SQL dump files, don't assume it will work. Make sure you have a good "backup" when experimenting with these new functions, as these are brand new and not widely tested just yet.


### Process modules are now a lot smarter

All interactive modules that run in the ProcessWire admin extend the base Process class. We've added some new capabilities to that class to make development of Process modules even simpler.

**Headlines and breadcrumbs** Now you can call `$this->headline("Your Headline");` in your Process module to set the headline, and `$this->breadcrumb("path", "Label");` to add an item to the breadcrumb trail. However, usage is of course optional. The base Process class now adds these things for you automatically where appropriate. So you only need to set the breadcrumbs or headline if you find that you want to vary from what the base Process class has automated for you.

Incidentally, you could set the headline and breadcrumbs relatively easily before, but the code to do it was just plain ugly, and these new methods are a lot cleaner and easier to remember.

**Automatic page creation (and removal)** Every Process module needs a page to live on. Previously your Process modules had to create that page on their own (from the install method), and likewise remove it (from the uninstall method). Now the base Process class will do this for you. Simplify specify a `page` property in your `getModuleInfo()` function, like this:

```
public static function getModuleInfo() {
  return array(
    'title' => 'Hello World',
    'version' => 1,
    'summary' => 'Just saying hello',
    'icon' => 'globe', // fa-icon to show with module
    'permission' => 'hello-world', // required permission to use
    'permissions' => array( // permissions to create at install
      'hello-world' => 'Use the fun Hello World process',
    ),
    'page' => array( // create a page at install
      'name' => 'hello-world',
      'parent' => 'setup'
    )
  );
}
```

Note that `page` property above. It is an array containing the name of the page you want to create, and the parent page where it should live. In this case, this Hello World module will be added below the Setup page, since we've specified "setup" as the parent (which is the page name). The parent may also be omitted, in which case the page will be added with admin root as parent. You can also specify a `title` property if you want to here. If omitted the module title is used instead.

When you specify this page property in your module information like above, that page will be created automatically (at installation time) and your Process module will be assigned to it. When/if the module is uninstalled, the page will be automatically trashed.

The above module information also demonstrates a few other recently added properties (mentioned in previous core notes), including `icon` and `permissions`.


### Database backups module

This is a new module that brings the backups capabilty (mentioned earlier) into an interactive Process module. If you are running the latest dev branch, you can install this module directly by [zip file](https://github.com/ryancramerdesign/ProcessDatabaseBackups/archive/master.zip) or by grabbing it on [GitHub](https://github.com/ryancramerdesign/ProcessDatabaseBackups). While this module is not currently part of the core, we will add it if there is demand for it. Otherwise it will be added to the modules directory once ProcessWire 2.5 is released.

This module is a work in progress, and there's still more to add. But we hope you find it useful. Consider it very much a beta test module at the moment, so don't make it your main backup/restore solution just yet.
