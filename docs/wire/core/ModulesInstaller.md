# ModulesInstaller

Source: `wire/core/ModulesInstaller.php`

ProcessWire Modules: Installer

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## install()

Install the given module name


@param string $class Module name (class name)

@param array|bool $options Optional associative array that can contain any of the following:
 - `dependencies` (boolean): When true, dependencies will also be installed where possible. Specify false to prevent installation of uninstalled modules. (default=true)
 - `resetCache` (boolean): When true, module caches will be reset after installation. (default=true)
 - `force` (boolean): Force installation, even if dependencies can't be met.

@return null|Module Returns null if unable to install, or ready-to-use Module object if successfully installed.

@throws WireException

## delete()

Delete the given module, physically removing its files


@param string $class Module name (class name)

@return bool

@throws WireException If module can't be deleted, exception will be thrown containing reason.

## uninstall()

Uninstall the given module name


@param string $class Module name (class name)

@return bool

@throws WireException

## getModuleInstallUrl()

Get URL where an administrator can install given module name

If module is already installed, it returns the URL to edit the module.

@param string $className

@return string
