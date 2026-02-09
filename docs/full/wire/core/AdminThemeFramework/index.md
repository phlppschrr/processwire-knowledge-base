# AdminThemeFramework

Source: `wire/core/AdminThemeFramework.php`

Inherits: `AdminTheme`


Groups:
Group: [other](group-other.md)

AdminTheme Framework

The methods in this class may eventually be merged to AdminTheme.php,
but are isolated to this class during development.

This file is licensed under the MIT license.
https://processwire.com/about/license/mit/

Methods:
- [`__construct()`](method-__construct.md)
- [`get(string $key): bool|int|mixed|null|string`](method-get.md)
- [`init()`](method-init.md)
- [`includeInitFile()`](method-includeinitfile.md)
- [`_(string $text): string`](method-_.md)
- [`getHeadline(): string`](method-getheadline.md)
- [`getPageTitle(Page $p): string`](method-getpagetitle.md)
- [`getPageIcon(Page $p): mixed|null|string`](method-getpageicon.md)
- [`getAddNewActions(): array`](method-getaddnewactions.md)
- [`getAddNewLabel(): string`](method-getaddnewlabel.md)
- [`getBodyClass(): string`](method-getbodyclass.md)
- [`getHeadJS(): string`](method-getheadjs.md)
- [`allowPageInNav(Page $p, PageArray|array $children = array(), string|null $permission = null): bool`](method-allowpageinnav.md)
- [`getPrimaryNavArray(): array`](method-___getprimarynavarray.md) (hookable)
- [`moduleToNavArray(array|Module|string $module, Page $p): array`](method-moduletonavarray.md)
- [`pageToNavArray(Page $p): array|null`](method-pagetonavarray.md)
- [`getUserNavArray(): array`](method-___getusernavarray.md) (hookable)
- [`getBrowserTitle(): string`](method-getbrowsertitle.md)
- [`testNotices(): bool`](method-testnotices.md)
- [`renderNotices(Notices|bool $notices, array $options = array()): string|array`](method-rendernotices.md)
- [`renderIcon(string $icon, bool $fw = false): string`](method-rendericon.md)
- [`renderNavIcon(string $icon): string`](method-rendernavicon.md)
- [`renderExtraMarkup(string $for): mixed|string`](method-renderextramarkup.md)
- [`renderFile(string $file, array $vars = array()): string`](method-___renderfile.md) (hookable)
- [`includeFile(string $basename, array $vars = array())`](method-includefile.md)
- [`setCustomTemplatePath(string $path)`](method-setcustomtemplatepath.md)
- [`getModuleConfigInputfields(InputfieldWrapper $inputfields)`](method-getmoduleconfiginputfields.md)
