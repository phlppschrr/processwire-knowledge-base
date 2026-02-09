# AdminThemeDefaultHelpers

Source: `wire/modules/AdminTheme/AdminThemeDefault/AdminThemeDefaultHelpers.php`

Inherits: `WireData`

AdminThemeDefaultHelpers.php

Rendering helper functions for use with ProcessWire admin theme.

__('FOR TRANSLATORS: please translate the file /wire/templates-admin/default.php rather than this one.');

Methods:
- [`_(string $text): string`](method-_.md)
- [`getHeadline(): string`](method-getheadline.md)
- [`renderBreadcrumbs(bool $appendCurrent = true): string`](method-renderbreadcrumbs.md)
- [`renderAdminShortcuts(): string`](method-renderadminshortcuts.md)
- [`renderAdminNotices(Notices $notices, array $options = array()): string`](method-renderadminnotices.md)
- [`getPageIcon(Page $p): mixed|null|string`](method-getpageicon.md)
- [`renderTopNavItem(Page $p, int $level = 0): string`](method-rendertopnavitem.md)
- [`getPageTitle(Page $c): string`](method-getpagetitle.md)
- [`renderTopNavItemArray(Page $p, array $nav): string`](method-rendertopnavitemarray.md)
- [`renderTopNavItems(): string`](method-rendertopnavitems.md)
- [`renderTopNavMarkCurrent(&$out)`](method-rendertopnavmarkcurrent.md)
- [`renderBrowserTitle(): string`](method-renderbrowsertitle.md)
- [`renderBodyClass(): string`](method-renderbodyclass.md)
- [`renderJSConfig(): string`](method-renderjsconfig.md)
