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
Method: [allowNotice()](method-allownotice.md)
Method: [formatNotice()](method-formatnotice.md)
Method: [add()](method-add.md)
Method: [storeNotice()](method-storenotice.md)
Method: [loadStoredNotices()](method-loadstorednotices.md)
Method: [removeNotice()](method-removenotice.md)
Method: [isDuplicate()](method-isduplicate.md)
Method: [addLog()](method-addlog.md)
Method: [hasErrors()](method-haserrors.md)
Method: [hasWarnings()](method-haswarnings.md)
Method: [move()](method-move.md)
Method: [getVisible()](method-getvisible.md)
Method: [render()](method-___render.md) (hookable)
Method: [renderText()](method-___rendertext.md) (hookable)
