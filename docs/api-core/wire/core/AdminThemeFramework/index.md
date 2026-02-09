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
- [`__construct()`](method-__construct.md) Construct
- [`get(string $key): bool|int|mixed|null|string`](method-get.md) Override get() method from WireData to support additional properties
- [`init()`](method-init.md) Initialize and attach hooks
- [`includeInitFile()`](method-includeinitfile.md) Include the admin theme init file
- [`_(string $text): string`](method-_.md) Perform a translation, based on text from shared admin file: /wire/templates-admin/default.php
- [`getHeadline(): string`](method-getheadline.md) Get the current page headline
- [`getPageTitle(Page $p): string`](method-getpagetitle.md) Get navigation title for the given page, return blank if page should not be shown
- [`getPageIcon(Page $p): mixed|null|string`](method-getpageicon.md) Get icon used by the given page
- [`getAddNewActions(): array`](method-getaddnewactions.md) Get “Add New” button actions
- [`getAddNewLabel(): string`](method-getaddnewlabel.md) Get the translated “Add New” label that’s used in a couple spots
- [`getBodyClass(): string`](method-getbodyclass.md) Get the classes that will be used in the <body class=''> tag
- [`getHeadJS(): string`](method-getheadjs.md) Get Javascript that must be present in the document <head>
- [`allowPageInNav(Page $p, PageArray|array $children = array(), string|null $permission = null): bool`](method-allowpageinnav.md) Allow the given Page to appear in admin theme navigation?
- [`getPrimaryNavArray(): array`](method-___getprimarynavarray.md) (hookable) Return nav array of primary navigation
- [`moduleToNavArray(array|Module|string $module, Page $p): array`](method-moduletonavarray.md) Get navigation array from a Process module
- [`pageToNavArray(Page $p): array|null`](method-pagetonavarray.md) Get a navigation array the given Page, or null if page not allowed in nav
- [`getUserNavArray(): array`](method-___getusernavarray.md) (hookable) Get navigation items for the “user” menu
- [`getBrowserTitle(): string`](method-getbrowsertitle.md) Get the browser <title>
- [`testNotices(): bool`](method-testnotices.md) Test all notice types
- [`renderNotices(Notices|bool $notices, array $options = array()): string|array`](method-rendernotices.md) Render runtime notices div#notices
- [`renderIcon(string $icon, bool $fw = false): string`](method-rendericon.md) Render markup for a font-awesome icon
- [`renderNavIcon(string $icon): string`](method-rendernavicon.md) Render markup for a font-awesome icon that precedes a navigation label
- [`renderExtraMarkup(string $for): mixed|string`](method-renderextramarkup.md) Render an extra markup region
- [`renderFile(string $file, array $vars = array()): string`](method-___renderfile.md) (hookable) Render a admin theme template file
- [`includeFile(string $basename, array $vars = array())`](method-includefile.md) Include an admin theme file
- [`setCustomTemplatePath(string $path)`](method-setcustomtemplatepath.md) Set custom path for admin theme templates
- [`getModuleConfigInputfields(InputfieldWrapper $inputfields)`](method-getmoduleconfiginputfields.md) Module Configuration
