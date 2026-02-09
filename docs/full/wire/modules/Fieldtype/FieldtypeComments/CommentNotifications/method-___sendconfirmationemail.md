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

## Arguments

- `$comment` `Comment`
- $email
- $subcode

## Return value

- `mixed`

## Hooking

- Hookable method name: `sendConfirmationEmail`
- Implementation: `___sendConfirmationEmail`
- Hook with: `CommentNotifications::sendConfirmationEmail`

### Hooking Before

~~~~~
$this->addHookBefore('CommentNotifications::sendConfirmationEmail', function(HookEvent $event) {
  $commentNotifications = $event->object;

  // Get arguments
  $comment = $event->arguments(0);
  $email = $event->arguments(1);
  $subcode = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $comment);
  $event->arguments(1, $email);
  $event->arguments(2, $subcode);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('CommentNotifications::sendConfirmationEmail', function(HookEvent $event) {
  $commentNotifications = $event->object;

  // Get arguments
  $comment = $event->arguments(0);
  $email = $event->arguments(1);
  $subcode = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException`
