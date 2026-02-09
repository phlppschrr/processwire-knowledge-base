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
- [`__construct()`](method-__construct.md) Construct
- [`execute(): string|array`](method-___execute.md) (hookable) Execute this Process and return the output. You may have any number of execute[name] methods, triggered by URL segments.
- [`executed(string $method)`](method-___executed.md) (hookable) Hookable method automatically called after execute() method has finished.
- [`headline(string $headline): $this`](method-___headline.md) (hookable) Set the current primary headline to appear in the admin interface
- [`browserTitle(string $title): $this`](method-___browsertitle.md) (hookable) Set the current browser title tag
- [`breadcrumb(string $href, string $label): $this`](method-___breadcrumb.md) (hookable) Add a breadcrumb
- [`install()`](method-___install.md) (hookable) Per the Module interface, Install the module
- [`uninstall()`](method-___uninstall.md) (hookable) Uninstall this Process
- [`upgrade(int|string $fromVersion, int|string $toVersion)`](method-___upgrade.md) (hookable) Called when module version changes
- [`installPage(string $name = '', $parent = null, string $title = '', $template = 'admin', array $extras = array()): Page`](method-___installpage.md) (hookable) Install a dedicated page for this Process module and assign it this Process
- [`uninstallPage(): int`](method-___uninstallpage.md) (hookable) Uninstall (trash) dedicated pages for this Process module
- [`setViewFile(string $file): $this`](method-setviewfile.md) Set the file to use for the output view, if different from default.
- [`getViewFile(): string`](method-getviewfile.md) If a view file has been set, this returns the full path to it.
- [`setViewVars(string|array $key, mixed|null $value = null): $this`](method-setviewvars.md) Set a variable that will be passed to the output view.
- [`getViewVars(): array`](method-getviewvars.md) Get all variables set for the output view
- [`getProcessPage(): Page|NullPage`](method-getprocesspage.md) Return the Page that this process lives on
- [`getAfterLoginUrl(Page $page): bool|string`](method-getafterloginurl.md) URL to redirect to after non-authenticated user is logged-in, or false if module does not support
