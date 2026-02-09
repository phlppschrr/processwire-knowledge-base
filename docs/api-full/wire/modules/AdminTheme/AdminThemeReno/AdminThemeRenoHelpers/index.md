# AdminThemeRenoHelpers

Source: `wire/modules/AdminTheme/AdminThemeReno/AdminThemeRenoHelpers.php`

Inherits: `AdminThemeDefaultHelpers`

Methods:
- [`renderAdminNotices(Notices $notices, array $options = array()): string`](method-renderadminnotices.md) Render runtime notices div#notices
- [`renderQuicklinks(Page $page, array $items, string $title, string $json = ''): string`](method-renderquicklinks.md) Render quicklinks for templates/fields. Designed to be called by renderSideNav()
- [`renderTopNav(): string`](method-rendertopnav.md) Render top navigation items
- [`topNavItems(array $items): string`](method-___topnavitems.md) (hookable) Render top navigation items (hookable)
- [`renderSideNavItem(Page $p): string`](method-rendersidenavitem.md) Render a side navigation items
- [`getDisplayName(User $user): string`](method-getdisplayname.md) Render the the user display name as specified in module config.
- [`renderSideNavItems(): string`](method-rendersidenavitems.md) Render all sidenav navigation items, ready to populate in ul#main-nav
