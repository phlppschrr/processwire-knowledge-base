# Notices

Source: `wire/core/Notices.php`

Inherits: `WireArray`

ProcessWire Notices

Notices
$notices
A class to contain multiple Notice instances, whether messages, warnings or errors.
This class manages notices that have been sent by `Wire::message()`, `Wire::warning()` and `Wire::error()` calls.
The message(), warning() and error() methods are available on every `Wire` derived object. This class is primarily
for internal use in the admin. However, it may also be useful in some front-end contexts.
~~~~~
// Adding a NoticeMessage using object syntax
$notices->add(new NoticeMessage("Hello World"));

// Adding a NoticeMessage using regular syntax
$notices->message("Hello World");

// Adding a NoticeWarning, and allow markup in it
$notices->message("Hello <strong>World</strong>", Notice::allowMarkup);

// Adding a NoticeError that only appears if debug mode is on
$notices->error("Hello World", Notice::debug);
~~~~~
**Iterating and outputting Notices:**
In ProcessWire 3.0.254+ you can use the `$notices->render()` or `$notices->renderText()` methods.
In all versions of ProcessWire, you can also output them manually like this:
~~~~~
foreach($notices as $notice) {
  // skip over debug notices, if debug mode isn't active
  if($notice->flags & Notice::debug && !$config->debug) continue;
  // entity encode notices unless the allowMarkup flag is set
  if($notice->flags & Notice::allowMarkup) {
    $text = $notice->text;
  } else {
    $text = $sanitizer->entities($notice->text);
  }
  // output either an error, warning or message notice
  if($notice instanceof NoticeError) {
    echo "<p class='error'>$text</p>";
  } else if($notice instanceof NoticeWarning) {
    echo "<p class='warning'>$text</p>";
  } else {
    echo "<p class='message'>$text</p>";
  }
}
~~~~~

Methods:
- [`allowNotice(Notice $item): bool`](method-allownotice.md)
- [`formatNotice(Notice $item)`](method-formatnotice.md)
- [`add(Notice $item): Notices|WireArray`](method-add.md)
- [`storeNotice(Notice $item): bool`](method-storenotice.md)
- [`loadStoredNotices(): int`](method-loadstorednotices.md)
- [`removeNotice(string|Notice $item): self`](method-removenotice.md)
- [`isDuplicate(Notice $item): bool|Notice`](method-isduplicate.md)
- [`addLog(Notice $item)`](method-addlog.md)
- [`hasErrors(): bool`](method-haserrors.md)
- [`hasWarnings(): bool`](method-haswarnings.md)
- [`move(Wire $from, Wire $to, array $options = array()): int`](method-move.md)
- [`getVisible(): Notices`](method-getvisible.md)
- [`render(array $options = []): string`](method-___render.md) (hookable)
- [`renderText(): string`](method-___rendertext.md) (hookable)
