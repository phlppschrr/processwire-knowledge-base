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

## Hooking Before

~~~~~
$this->addHookBefore('CommentNotifications::sendAdminNotificationEmail', function(HookEvent $event) {
  $commentNotifications = $event->object;

  // Get arguments
  $comment = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $comment);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('CommentNotifications::sendAdminNotificationEmail', function(HookEvent $event) {
  $commentNotifications = $event->object;

  // Get arguments
  $comment = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$comment` `Comment`

## Return value

- `int` Number of emails sent
