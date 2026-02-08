# $commentNotifications->sendNotificationEmail(Comment $comment, $email, $subcode, array $options = array()): int

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentNotifications.php`

Send a user (not admin) notification email

## Usage

~~~~~
// basic usage
$int = $commentNotifications->sendNotificationEmail($comment, $email, $subcode);

// usage with all arguments
$int = $commentNotifications->sendNotificationEmail(Comment $comment, $email, $subcode, array $options = array());
~~~~~

## Hookable

- Hookable method name: `sendNotificationEmail`
- Implementation: `___sendNotificationEmail`
- Hook with: `$commentNotifications->sendNotificationEmail()`

## Arguments

- `$comment` `Comment`
- `$email` `string|array`
- `$subcode` `string` Subscribe/unsubscribe code or blank string if not in use
- `$options` (optional) `array`

## Return value

- `int`
