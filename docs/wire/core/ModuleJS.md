# ModuleJS

Source: `wire/core/ModuleJS.php`

ProcessWire ModuleJS

An abstract module intended as a base for modules needing to autoload JS or CSS files.

If you extend this, double check that the default isSingular() and isAutoload() methods
are doing what you want -- you may want to override them.

See the Module interface (Module.php) for details about each method.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

## other

@method ModuleJS use(string $name)

## getModuleInfo()

Per the Module interface, return an array of information about the Module

## addComponent()

Add an optional component that can be used with this module

@param string $name

@param string $file

@return $this

## addComponents()

Add an array of optional components

@param array $components

@return $this

## init()

Per the Module interface, Initialize the Process, loading any related CSS or JS files

## ___use()

Use an extra named component

@param $name

@return $this
