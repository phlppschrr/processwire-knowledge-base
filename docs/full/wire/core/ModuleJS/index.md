# ModuleJS

Source: `wire/core/ModuleJS.php`

Inherits: `WireData`
Implements: `Module`


Groups:
Group: [other](group-other.md)

ProcessWire ModuleJS

An abstract module intended as a base for modules needing to autoload JS or CSS files.

If you extend this, double check that the default isSingular() and isAutoload() methods
are doing what you want -- you may want to override them.

See the Module interface (Module.php) for details about each method.


This file is licensed under the MIT license
https://processwire.com/about/license/mit/

Methods:
- [`getModuleInfo()`](method-getmoduleinfo.md)
- [`addComponent(string $name, string $file): $this`](method-addcomponent.md)
- [`addComponents(array $components): $this`](method-addcomponents.md)
- [`init()`](method-init.md)
- [`use($name): $this`](method-___use.md) (hookable)
