# How to upgrade ProcessWire to the latest version

Source: https://processwire.com/docs/start/install/upgrade/

# Upgrading ProcessWire from one version to another 

Most version upgrades in ProcessWire are as simple as just replacing the /wire/ directory with the new version.

However, we recommend that you be familiar with the following best practices and general upgrade process, as well as any version-specific upgrade notes found in the version README.md file.
- [Best practices before upgrading](#best-practices-before-upgrading)
- [General upgrade process](#general-upgrade-process)
- [Replacing the /wire/ directory](#replacing-the-wire-directory)
- [Replacing the /index.php file](#replacing-the-index.php-file)
- [Replacing the .htaccess file](#replacing-the-htaccess-file)
- [Troubleshooting upgrades](#troubleshooting-upgrades)

---
[](#)

### Best practices before upgrading

- Backup your database and backup all the files in your site (ensuring you can revert if needed).
- When possible, test the upgrade on a development/staging site before performing the upgrade on a live/production site.
- Login to your ProcessWire admin under a superuser account before upgrading.
- Temporarily [enable debug mode](https://processwire.com/docs/start/install/troubleshooting/#enabling-debug-mode) during the upgrade (optional but recommended).

**If you have 3rd party modules installed, confirm that they are compatible with the ProcessWire version you are upgrading to.** If you cannot confirm compatibility, uninstall the 3rd party modules before upgrading, when possible. You can attempt to re-install them after upgrading. If uninstalling is inconvenient, just be sure you have the ability to revert if for some reason one of your modules does not like the upgrade.

**If you prefer an automatic/web-based upgrade**, an [upgrade module](https://processwire.com/modules/process-wire-upgrade/) is available. This module can also help with identifying and upgrading other modules as well. When upgrading the core, we prefer to do this manually since it is already very simple, but wanted to let you know about the option either way. Whether or not you use the module to perform the upgrades, it is a handy way to identify when upgrades are available.[](#)

### General upgrade process

Before upgrading, login to your ProcessWire admin under a superuser account. This is not required to upgrade, but is recommended for more verbose output during the upgrade. As with any upgrade, backup first (your site’s files and database). Upgrading from one version of ProcessWire to another is a matter of deleting/replacing these files and directories from your old version, and putting in fresh copies from the new version:
- `/wire/` (required) [details](#replacing-the-wire-directory)
- `/index.php` (if needed) [details](#replacing-the-index.php-file)
- `/.htaccess` (if needed) [details](#replacing-the-htaccess-file)

Unless otherwise noted in the version’s README file, removing and replacing the above directory/files is typically the primary thing you need to do in order to upgrade. Further below are more details about how you should replace the files mentioned above.

After replacing the /wire/ directory (and the other two files if needed), hit reload in your browser, anywhere in the ProcessWire admin. You should see messages at the top of your screen about updates that were applied. Depending on which version you are upgrading from, you might also see error messages–this is normal. Keep hitting reload in your browser until you no longer see any upgrade related messages (up to 5 reloads may be necessary).

**Renaming is an alternative to deleting**, which gives you a quicker path to revert should you want to. For example, you might rename your /wire/ directory to be /.wire-2.7.2/ with ".wire" rather than "wire" to ensure the directory is hidden, and the 2.7.2 indicating the version that it was. Once your upgrade is safely in place, you could delete that .wire-2.7.2 directory (or keep it around). If you keep old version dirs/files in place, make sure they are not http accessible. This is typically done by preceding the directory with a period to make it hidden.[](#)

### Replacing the /wire/ directory

When you put in the new /wire/ directory, make sure that you remove or rename the old one first. If you just copy or FTP changed files into the existing /wire/ directory, you will end up with both old and new files, which will cause an error.

Note that the /wire/ directory does not contain any files specific to your site, only to ProcessWire. All the files specific to your site are stored in /site/ and you would leave that directory alone during an upgrade.[](#)

### Replacing the /index.php file

This file doesn't change often between minor versions. As a result, you don't need to replace this file unless it has changed. When in doubt, you should replace it. When upgrading from 2.7 to 3.x you will definitely need to replace it.[](#)

### Replacing the .htaccess file

This is also a file that does not always change between versions. But when it changes, it is usually important for security that you are up-to-date. When in doubt, replace your old .htaccess file with the htaccess.txt from the new version.

This file is initially named htaccess.txt in the ProcessWire source. You will want to remove your existing .htaccess file and rename the new htaccess.txt to .htaccess

Sometimes people have made changes to the .htaccess file. If this is the case for your site, remember to migrate those changes to the new .htaccess file.

**If you are using [**ProCache**](/store/pro-cache/)**, it will have added some things to your .htaccess file. Copy these changes from your old .htaccess file to your new one. The changes are easy to identify in your previous .htaccess file as they start and end with a `# ProCache` comment. Alternatively, you can have ProCache re-apply the changes itself by logging in to your admin and going to Setup > ProCache.[](#)

### Troubleshooting upgrades

Please see our [Troubleshooting Upgrades](https://processwire.com/docs/start/install/troubleshooting/#troubleshooting-upgrades) page.
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
