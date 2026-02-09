# ModuleJS

Source: `wire/core/ModuleJS.php`

ProcessWire ModuleJS

An abstract module intended as a base for modules needing to autoload JS or CSS files.

If you extend this, double check that the default isSingular() and isAutoload() methods
are doing what you want -- you may want to override them.

See the Module interface (Module.php) for details about each method.


This file is licensed under the MIT license
https://processwire.com/about/license/mit/

Groups:
Group: [other](group-other.md)

Methods:
Method: [getModuleInfo()](method-getmoduleinfo.md)
Method: [addComponent()](method-addcomponent.md)
Method: [addComponents()](method-addcomponents.md)
Method: [init()](method-init.md)
Method: [use()](method-___use.md) (hookable)
