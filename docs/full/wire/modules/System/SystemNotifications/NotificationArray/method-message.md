# $notificationArray->message($text, $flags = 0): Notification

Source: `wire/modules/System/SystemNotifications/NotificationArray.php`

Record an informational or 'success' message

## Usage

~~~~~
// basic usage
$notification = $notificationArray->message($text);

// usage with all arguments
$notification = $notificationArray->message($text, $flags = 0);
~~~~~

## Arguments

- `$text` `string`
- `$flags` (optional) `int|bool` See Notification flags

## Return value

- `Notification`
