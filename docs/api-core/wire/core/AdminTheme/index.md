# AdminTheme

Source: `wire/core/AdminTheme.php`

Inherits: `WireData`
Implements: `Module`

## Summary

ProcessWire Admin Theme Module

Common methods:
- [`getModuleInfo()`](method-getmoduleinfo.md)
- [`init()`](method-init.md)
- [`initConfig()`](method-initconfig.md)
- [`get()`](method-get.md)
- [`url()`](method-url.md)

Groups:
Group: [other](group-other.md)

An abstract module intended as a base for admin themes.

See the Module interface (Module.php) for details about each method.

This file is licensed under the MIT license.
https://processwire.com/about/license/mit/

## Methods
- [`getModuleInfo()`](method-getmoduleinfo.md) Per the Module interface, return an array of information about the Module
- [`__construct()`](method-__construct.md) Construct
- [`init()`](method-init.md) Initialize the admin theme system and determine which admin theme should be used
- [`initConfig()`](method-initconfig.md) Initialize configuration properties and JS config for when this is current admin theme
- [`get(string $key): int|mixed|null|string`](method-get.md) Get property
- [`url(): string`](method-url.md) Get URL to this admin theme
- [`path(): string`](method-path.md) Get disk path to this admin theme
- [`getLabel(string $key, string $val = ''): string`](method-getlabel.md) Get predefined translated label by key for labels shared among admin themes
- [`isCurrent()`](method-iscurrent.md) Returns true if this admin theme is the one that will be used for this request
- [`setCurrent()`](method-setcurrent.md) Set this admin theme as the current one
- [`getExtraMarkup(): array`](method-___getextramarkup.md) (hookable) Enables hooks to append extra markup to various sections of the admin page
- [`addExtraMarkup(string $name, string $value)`](method-addextramarkup.md) Add extra markup to a region in the admin theme
- [`addBodyClass(string $className)`](method-addbodyclass.md) Add a <body> class to the admin theme
- [`getBodyClass(): string`](method-getbodyclass.md) Get the body[class] attribute string
- [`getClass(string $name = '', bool $getArray = false): string|array`](method-getclass.md) Return class for a given named item or blank if none available
- [`install()`](method-___install.md) (hookable) Install the admin theme
