# ModuleJS

Source: `wire/core/ModuleJS.php`

Inherits: `WireData`
Implements: `Module`

## Summary

ProcessWire ModuleJS

Common methods:
- [`getModuleInfo()`](method-getmoduleinfo.md)
- [`addComponent()`](method-addcomponent.md)
- [`addComponents()`](method-addcomponents.md)
- [`init()`](method-init.md)
- [`use()`](method-___use.md)

Groups:
Group: [other](group-other.md)

An abstract module intended as a base for modules needing to autoload JS or CSS files.

If you extend this, double check that the default isSingular() and isAutoload() methods
are doing what you want -- you may want to override them.

See the Module interface (Module.php) for details about each method.


This file is licensed under the MIT license
https://processwire.com/about/license/mit/

## Methods
- [`getModuleInfo()`](method-getmoduleinfo.md) Per the Module interface, return an array of information about the Module
- [`addComponent(string $name, string $file): $this`](method-addcomponent.md) Add an optional component that can be used with this module
- [`addComponents(array $components): $this`](method-addcomponents.md) Add an array of optional components
- [`init()`](method-init.md) Per the Module interface, Initialize the Process, loading any related CSS or JS files
- [`use($name): $this`](method-___use.md) (hookable) Use an extra named component
