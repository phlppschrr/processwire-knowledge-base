# Unknown

Source: https://processwire.com/docs/start/install/troubleshooting/

If you’ve run into an issue during installation or upgrade of ProcessWire, find out how to fix it here.

- [Troubleshooting Installation](#troubleshooting-installation)
  - [The homepage works but nothing else does](#the-homepage-works-but-nothing-else-does)
  - [Resolving an Apache 500 error](#resolving-an-apache-500-error)
  - [Resolving other error messages or a blank screen](#resolving-other-error-messages-or-a-blank-screen)

- [Troubleshooting Upgrades](#troubleshooting-upgrades)
  - [General troubleshooting upgrade tips](#general-troubleshooting-upgrade-tips)
  - [Enabling debug mode](#enabling-debug-mode)
  - [Troubleshooting a 2.x to 3.x upgrade](#troubleshooting-a-2.x-to-3.x-upgrade)

---

[#](#)

## Troubleshooting Installation

[#](#)

### The homepage works but nothing else does

This indicates that Apache is not properly reading your .htaccess file. First we need to determine if Apache is reading your .htaccess file at all. To do this, open the .htaccess file in an editor and type in some random characters at the top, like `lkjalefkjalkef` and save. Load your site in your browser. You should get a "500 Error". If you do not, that means Apache is not reading your .htaccess file at all. If this is your case, contact your web host for further assistance. Or if maintaining your own server, look into the Apache *AllowOverride* directive which you may need to configure for the account in your httpd.conf file.

If the above test did result in a 500 error, then that is good because we know your .htaccess file is at least being used. Go ahead and remove the random characters you added at the top. Now look further down in the .htaccess file for suggested changes. Specially, you will want to look at the `RewriteBase` directive, which is commented out (disabled) by default. You may need to enable it.

[#](#)

### Resolving an Apache 500 error

The presence of an Apache 500 error indicates that Apache does not like one or more of the directives in the .htaccess file. Open the .htaccess file in an editor and read the comments. Note those that indicate the term "500 NOTE" and they will provide further instructions on optional directives you can try to comment out. Test one at a time, save and reload in your browser till you determine which directive is not working with your server.

[#](#)

### Resolving other error messages or a blank screen

If you are getting an error message, a blank screen, or something else unexpected, see the section at the end of this document on enabling debug mode. This will enable more detailed error reporting which may help to resolve any issues.

In addition, the ProcessWire error log is located in the file: /site/assets/logs/errors.txt - look in here to see if more information is available about the error message you have received.

If the above suggestions do not help you to resolve the installation error, please post in the [ProcessWire forums](https://processwire.com/talk/).

---

[#](#)

## Troubleshooting Upgrades

[#](#)

### General troubleshooting upgrade tips

- 

If you get an error message when loading your site after an upgrade, hit "reload" in your browser until the error messages disappear. It may take up to 5 reloads for ProcessWire to apply all updates.

- 

If your site still doesn't work, remove the /wire/ directory completely. Then upload a fresh copy of the /wire/ directory.

- 

If your site still doesn't work, view the latest entries in your error log file to see if it clarifies anything. The error log can be found in: /site/assets/logs/errors.txt

- 

If your site still doesn't work, enable debug mode (as described in the next section) to see if the more verbose error messages help you to determine what the issue is. If you need help, please post in our [support forum](https://processwire.com/talk/).

[#](#)

### Enabling debug mode

Debug mode causes all errors to be reported to the screen, which can be helpful during development or troubleshooting. When in the admin, it also enables reporting of extra information in the footer. Debug mode is not intended for live or production sites, as the information reported could be a problem for security. So be sure not to leave debug mode on for any live/production sites.

1. Edit this file: /site/config.php
2. Find this line: `$config->debug = false; `
3. Change the `false` to `true`, like below, and save.

```
$config->debug = true;
```

This can be found near the bottom of the file, or you can add it if not already there. It will make PHP and ProcessWire report all errors, warnings, notices, etc. Of course, you'll want to set it back to false once you've resolved any issues.

[#](#)

### Troubleshooting a 2.x to 3.x upgrade

Before we mention anything else, if you run into any troubles with the 3.x upgrade, you may want to consider upgrading to version 2.8.x instead. It is identical to 3.x in terms of features, except that it lacks namespace support (just like 2.7). Because of that omission, version 2.8 may be more of a turn-key upgrade from 2.7 if that is your preference. You can find ProcessWire 2.8 as the [processwire-legacy](https://github.com/processwire/processwire-legacy) repository.

Any error messages you see in 3.x are likely related to the fact that this version of the core is now running in a namespace called ProcessWire, rather than in the root PHP namespace. Error messages will likely mention a file in your /site/modules/ directory or a file in your /site/templates/ directory.

ProcessWire attempts to compile any module or template PHP files that it thinks will have issues due to namespace. This should work well in most instances. However, if you come across any instances where it does not work, you may need to add the ProcessWire namespace to your file. To add the namespace to a file, simply edit the file and add this at the very top:

```
<?php namespace ProcessWire;
```

To prevent ProcessWire from attempting to compile a file, place the text `FileCompiler=0` anywhere in the file, and ProcessWire will skip over it.

If necessary, file compilation can also be disabled completely by adding the following to your /site/config.php file. However, keep in mind file compilation is there to make your life easier, so be careful about disabling it, especially for modules.

```
// disable module compilation
$config->moduleCompile = false;

// disable template file compilation
$config->templateCompile = false;
```

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
