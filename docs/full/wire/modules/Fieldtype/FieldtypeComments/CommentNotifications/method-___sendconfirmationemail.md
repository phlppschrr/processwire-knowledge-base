# $commentNotifications->sendConfirmationEmail(Comment $comment, $email, $subcode): mixed

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentNotifications.php`

Send confirmation/opt-in email for notifications (not yet active)

## Usage

~~~~~
// basic usage
$result = $commentNotifications->sendConfirmationEmail($comment, $email, $subcode);

// usage with all arguments
$result = $commentNotifications->sendConfirmationEmail(Comment $comment, $email, $subcode);
~~~~~

## Hookable

- Hookable method name: `sendConfirmationEmail`
- Implementation: `___sendConfirmationEmail`
- Hook with: `$commentNotifications->sendConfirmationEmail()`

## Arguments

- `$comment` `Comment`
- $email
- $subcode

## Return value

- `mixed`

## Exceptions

- `WireException`
