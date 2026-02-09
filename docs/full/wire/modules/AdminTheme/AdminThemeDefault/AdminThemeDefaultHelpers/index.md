# AdminThemeDefaultHelpers

Source: `wire/modules/AdminTheme/AdminThemeDefault/AdminThemeDefaultHelpers.php`

Inherits: `WireData`

AdminThemeDefaultHelpers.php

Rendering helper functions for use with ProcessWire admin theme.

__('FOR TRANSLATORS: please translate the file /wire/templates-admin/default.php rather than this one.');

Methods:
- [`_(string $text): string`](method-_.md) Perform a translation, based on text from shared admin file: /wire/templates-admin/default.php
- [`getHeadline(): string`](method-getheadline.md) Get the headline for the current admin page
- [`renderBreadcrumbs(bool $appendCurrent = true): string`](method-renderbreadcrumbs.md) Render a list of breadcrumbs (list items), excluding the containing <ul>
- [`renderAdminShortcuts(): string`](method-renderadminshortcuts.md) Render the populated shortcuts head button or blank when not applicable
- [`renderAdminNotices(Notices $notices, array $options = array()): string`](method-renderadminnotices.md) Render runtime notices div#notices
- [`getPageIcon(Page $p): mixed|null|string`](method-getpageicon.md) Get markup for icon used by the given page
- [`renderTopNavItem(Page $p, int $level = 0): string`](method-rendertopnavitem.md) Render a single top navigation item for the given page
- [`getPageTitle(Page $c): string`](method-getpagetitle.md) Get navigation title for the given page, return blank if page should not be shown
- [`renderTopNavItemArray(Page $p, array $nav): string`](method-rendertopnavitemarray.md) Renders static navigation from an array coming from getModuleInfo()['nav'] array (see wire/core/Process.php)
- [`renderTopNavItems(): string`](method-rendertopnavitems.md) Render all top navigation items, ready to populate in ul#topnav
- [`renderTopNavMarkCurrent(&$out)`](method-rendertopnavmarkcurrent.md) Identify current "on" items in the topnav and add appropriate class
- [`renderBrowserTitle(): string`](method-renderbrowsertitle.md) Render the browser <title>
- [`renderBodyClass(): string`](method-renderbodyclass.md) Render the class that will be used in the <body class=''> tag
- [`renderJSConfig(): string`](method-renderjsconfig.md) Render the required javascript 'config' variable for the document <head>
