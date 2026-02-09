# $notificationArray->messages($options = array()): Notices|string

Source: `wire/modules/System/SystemNotifications/NotificationArray.php`

Return messages recorded by this object

## Usage

~~~~~
// basic usage
$notices = $notificationArray->messages();

// usage with all arguments
$notices = $notificationArray->messages($options = array());
~~~~~

## Arguments

- `$options` (optional) `string|array` One or more of array elements or space separated string of: first: only first item will be returned (string) last: only last item will be returned (string) clear: clear out all items that are returned from this method (includes both local and global) errors: returns errors rather than messages. warnings: returns warnings rather than messages.

## Return value

- `Notices|string` Array of NoticeError error messages or string if last, first or str option was specified.
