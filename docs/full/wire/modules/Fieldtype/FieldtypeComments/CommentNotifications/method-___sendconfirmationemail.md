# $commentNotifications->___sendConfirmationEmail(Comment $comment, $email, $subcode): mixed

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentNotifications.php`

Send confirmation/opt-in email for notifications (not yet active)

## Usage

~~~~~
// basic usage
$result = $commentNotifications->___sendConfirmationEmail($comment, $email, $subcode);

// usage with all arguments
$result = $commentNotifications->___sendConfirmationEmail(Comment $comment, $email, $subcode);
~~~~~

## Arguments

- `$comment` `Comment`
- $email
- $subcode

## Return value

- `mixed`

## Exceptions

- `WireException`
