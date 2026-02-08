# $commentNotifications->___sendAdminNotificationEmail(Comment $comment): int

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentNotifications.php`

Send notification email to specified admin to review the comment

## Usage

~~~~~
// basic usage
$int = $commentNotifications->___sendAdminNotificationEmail($comment);

// usage with all arguments
$int = $commentNotifications->___sendAdminNotificationEmail(Comment $comment);
~~~~~

## Arguments

- `$comment` `Comment`

## Return value

- `int` Number of emails sent
