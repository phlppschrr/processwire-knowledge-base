# Process

Source: `wire/core/Process.php`

Inherits: `WireData`
Implements: `Module`


Groups:
Group: [other](group-other.md)

ProcessWire Process

Process is the base Module class for each part of ProcessWire's web admin.

Process modules are self contained applications that run in the ProcessWire admin.
Please be sure to see the `Module` interface for full details on methods you can specify in a Process module.


This file is licensed under the MIT license
https://processwire.com/about/license/mit/

Methods:
- [`__construct()`](method-__construct.md)
- [`execute(): string|array`](method-___execute.md) (hookable)
- [`executed(string $method)`](method-___executed.md) (hookable)
- [`headline(string $headline): $this`](method-___headline.md) (hookable)
- [`browserTitle(string $title): $this`](method-___browsertitle.md) (hookable)
- [`breadcrumb(string $href, string $label): $this`](method-___breadcrumb.md) (hookable)
- [`install()`](method-___install.md) (hookable)
- [`uninstall()`](method-___uninstall.md) (hookable)
- [`upgrade(int|string $fromVersion, int|string $toVersion)`](method-___upgrade.md) (hookable)
- [`installPage(string $name = '', $parent = null, string $title = '', $template = 'admin', array $extras = array()): Page`](method-___installpage.md) (hookable)
- [`uninstallPage(): int`](method-___uninstallpage.md) (hookable)
- [`setViewFile(string $file): $this`](method-setviewfile.md)
- [`getViewFile(): string`](method-getviewfile.md)
- [`setViewVars(string|array $key, mixed|null $value = null): $this`](method-setviewvars.md)
- [`getViewVars(): array`](method-getviewvars.md)
- [`getProcessPage(): Page|NullPage`](method-getprocesspage.md)
- [`getAfterLoginUrl(Page $page): bool|string`](method-getafterloginurl.md)
