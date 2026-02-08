# Upgrading ProcessWire from one version to another

Source: https://processwire.com/docs/start/install/upgrade/

## Summary

Most version upgrades in ProcessWire are as simple as just replacing the /wire/ directory with the new version.

## Key Points

- Most version upgrades in ProcessWire are as simple as just replacing the /wire/ directory with the new version.
- However, we recommend that you be familiar with the following best practices and general upgrade process, as well as any version-specific upgrade notes found in the version README.md file.
- If you have 3rd party modules installed, confirm that they are compatible with the ProcessWire version you are upgrading to. If you cannot confirm compatibility, uninstall the 3rd party modules before upgrading, when possible. You can attempt to re-install them after upgrading. If uninstalling is inconvenient, just be sure you have the ability to revert if for some reason one of your modules does not like the upgrade.

## Sections


### Best practices before upgrading

If you have 3rd party modules installed, confirm that they are compatible with the ProcessWire version you are upgrading to. If you cannot confirm compatibility, uninstall the 3rd party modules before upgrading, when possible. You can attempt to re-install them after upgrading. If uninstalling is inconvenient, just be sure you have the ability to revert if for some reason one of your modules does not like the upgrade.


### General upgrade process

Before upgrading, login to your ProcessWire admin under a superuser account. This is not required to upgrade, but is recommended for more verbose output during the upgrade. As with any upgrade, backup first (your site’s files and database). Upgrading from one version of ProcessWire to another is a matter of deleting/replacing these files and directories from your old version, and putting in fresh copies from the new version:


### Replacing the /wire/ directory

When you put in the new /wire/ directory, make sure that you remove or rename the old one first. If you just copy or FTP changed files into the existing /wire/ directory, you will end up with both old and new files, which will cause an error.


### Replacing the /index.php file

This file doesn't change often between minor versions. As a result, you don't need to replace this file unless it has changed. When in doubt, you should replace it. When upgrading from 2.7 to 3.x you will definitely need to replace it.


### Replacing the .htaccess file

This is also a file that does not always change between versions. But when it changes, it is usually important for security that you are up-to-date. When in doubt, replace your old .htaccess file with the htaccess.txt from the new version.


### Troubleshooting upgrades
