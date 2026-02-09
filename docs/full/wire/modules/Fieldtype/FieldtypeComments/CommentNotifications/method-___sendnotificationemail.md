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

## Hooking Before

~~~~~
$this->addHookBefore('CommentNotifications::sendNotificationEmail', function(HookEvent $event) {
  $commentNotifications = $event->object;

  // Get arguments
  $comment = $event->arguments(0);
  $email = $event->arguments(1);
  $subcode = $event->arguments(2);
  $options = $event->arguments(3);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $comment);
  $event->arguments(1, $email);
  $event->arguments(2, $subcode);
  $event->arguments(3, $options);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('CommentNotifications::sendNotificationEmail', function(HookEvent $event) {
  $commentNotifications = $event->object;

  // Get arguments
  $comment = $event->arguments(0);
  $email = $event->arguments(1);
  $subcode = $event->arguments(2);
  $options = $event->arguments(3);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$comment` `Comment`
- `$email` `string|array`
- `$subcode` `string` Subscribe/unsubscribe code or blank string if not in use
- `$options` (optional) `array`

## Return value

- `int`
