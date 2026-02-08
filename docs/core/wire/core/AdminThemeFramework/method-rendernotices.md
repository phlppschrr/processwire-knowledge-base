# $adminThemeFramework->renderNotices($notices, array $options = array()): string|array

Source: `wire/core/AdminThemeFramework.php`

Render runtime notices div#notices

## Arguments

- Notices|bool $notices Notices object or specify boolean true to return array of all available $options
- array $options See defaults in method

## Return value

string|array Returns string unless you specify true for $notices argument, then it returns an array.
