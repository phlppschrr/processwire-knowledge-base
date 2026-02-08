# AdminThemeRenoHelpers

Source: `wire/modules/AdminTheme/AdminThemeReno/AdminThemeRenoHelpers.php`


## renderAdminNotices()

Render runtime notices div#notices

@param Notices $notices

@param array $options

@return string

## renderQuicklinks()

Render quicklinks for templates/fields. Designed to be called by renderSideNav()

@param Page $page

@param array $items

@param string $title

@param string $json

@return string

## renderTopNav()

Render top navigation items

@return string

## ___topNavItems()

Render top navigation items (hookable)

@return string

## renderSideNavItem()

Render a side navigation items

This function designed primarily to be called by the renderSideNavItems() function.

@param Page $p

@return string

## getDisplayName()

Render the the user display name as specified in module config.

@return string

## renderSideNavItems()

Render all sidenav navigation items, ready to populate in ul#main-nav

@return string
