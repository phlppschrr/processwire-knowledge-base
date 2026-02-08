# $commentNotifications->sendAdminNotificationEmail(Comment $comment): int

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentNotifications.php`

Send notification email to specified admin to review the comment

## Usage

~~~~~
// basic usage
$int = $commentNotifications->sendAdminNotificationEmail($comment);

// usage with all arguments
$int = $commentNotifications->sendAdminNotificationEmail(Comment $comment);
~~~~~

## Hookable

- Hookable method name: `sendAdminNotificationEmail`
- Implementation: `___sendAdminNotificationEmail`
- Hook with: `$commentNotifications->sendAdminNotificationEmail()`

## Arguments

- `$comment` `Comment`

## Return value

- `int` Number of emails sent
