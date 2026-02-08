# AdminThemeDefaultHelpers

Source: `wire/modules/AdminTheme/AdminThemeDefault/AdminThemeDefaultHelpers.php`

AdminThemeDefaultHelpers.php

Rendering helper functions for use with ProcessWire admin theme.

__('FOR TRANSLATORS: please translate the file /wire/templates-admin/default.php rather than this one.');

## _()

Perform a translation, based on text from shared admin file: /wire/templates-admin/default.php

@param string $text

@return string

## getHeadline()

Get the headline for the current admin page

@return string

## renderBreadcrumbs()

Render a list of breadcrumbs (list items), excluding the containing <ul>

@param bool $appendCurrent Whether to append the current title/headline to the breadcrumb trail (default=true)

@return string

## renderAdminShortcuts()

Render the populated shortcuts head button or blank when not applicable

@return string

## renderAdminNotices()

Render runtime notices div#notices

@param array $options See defaults in method

@param Notices $notices

@return string

## getPageIcon()

Get markup for icon used by the given page

@param Page $p

@return mixed|null|string

## renderTopNavItem()

Render a single top navigation item for the given page

This function designed primarily to be called by the renderTopNavItems() function.

@param Page $p

@param int $level Recursion level (default=0)

@return string

## getPageTitle()

Get navigation title for the given page, return blank if page should not be shown

@param Page $c

@return string

## renderTopNavItemArray()

Renders static navigation from an array coming from getModuleInfo()['nav'] array (see wire/core/Process.php)

@param Page $p

@param array $nav

@return string

## renderTopNavItems()

Render all top navigation items, ready to populate in ul#topnav

@return string

## renderTopNavMarkCurrent()

Identify current "on" items in the topnav and add appropriate class

@param $out

## renderBrowserTitle()

Render the browser <title>

@return string

## renderBodyClass()

Render the class that will be used in the <body class=''> tag

@return string

## renderJSConfig()

Render the required javascript 'config' variable for the document <head>

@return string
