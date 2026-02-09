# AdminTheme

Source: `wire/core/AdminTheme.php`

Inherits: `WireData`
Implements: `Module`


Groups:
Group: [other](group-other.md)

ProcessWire Admin Theme Module

An abstract module intended as a base for admin themes.

See the Module interface (Module.php) for details about each method.

This file is licensed under the MIT license.
https://processwire.com/about/license/mit/

Methods:
- [`getModuleInfo()`](method-getmoduleinfo.md)
- [`__construct()`](method-__construct.md)
- [`init()`](method-init.md)
- [`initConfig()`](method-initconfig.md)
- [`get(string $key): int|mixed|null|string`](method-get.md)
- [`url(): string`](method-url.md)
- [`path(): string`](method-path.md)
- [`getLabel(string $key, string $val = ''): string`](method-getlabel.md)
- [`isCurrent()`](method-iscurrent.md)
- [`setCurrent()`](method-setcurrent.md)
- [`getExtraMarkup(): array`](method-___getextramarkup.md) (hookable)
- [`addExtraMarkup(string $name, string $value)`](method-addextramarkup.md)
- [`addBodyClass(string $className)`](method-addbodyclass.md)
- [`getBodyClass(): string`](method-getbodyclass.md)
- [`getClass(string $name = '', bool $getArray = false): string|array`](method-getclass.md)
- [`install()`](method-___install.md) (hookable)
