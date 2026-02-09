# Notices

Source: `wire/core/Notices.php`

Inherits: `WireArray`

## Summary

ProcessWire Notices

Common methods:
- [`init()`](method-init.md)
- [`isValidItem()`](method-isvaliditem.md)
- [`makeBlankItem()`](method-makeblankitem.md)
- [`allowNotice()`](method-allownotice.md)
- [`formatNotice()`](method-formatnotice.md)

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

## Methods
- [`allowNotice(Notice $item): bool`](method-allownotice.md) Allow given Notice to be added?
- [`formatNotice(Notice $item)`](method-formatnotice.md) Format Notice text
- [`add(Notice $item): Notices|WireArray`](method-add.md) Add a Notice object
- [`storeNotice(Notice $item): bool`](method-storenotice.md) Store a persist Notice in Session
- [`loadStoredNotices(): int`](method-loadstorednotices.md) Load persist Notices stored in Session
- [`removeNotice(string|Notice $item): self`](method-removenotice.md) Remove a Notice
- [`isDuplicate(Notice $item): bool|Notice`](method-isduplicate.md) Is the given Notice a duplicate of one already here?
- [`addLog(Notice $item)`](method-addlog.md) Add Notice to log
- [`hasErrors(): bool`](method-haserrors.md) Are there NoticeError items present?
- [`hasWarnings(): bool`](method-haswarnings.md) Are there NoticeWarning items present?
- [`move(Wire $from, Wire $to, array $options = array()): int`](method-move.md) Move notices from one Wire instance to another
- [`getVisible(): Notices`](method-getvisible.md) Get all notices visible to current user
- [`render(array $options = []): string`](method-___render.md) (hookable) Render these notices as HTML
- [`renderText(): string`](method-___rendertext.md) (hookable) Render these Notices as plain text
