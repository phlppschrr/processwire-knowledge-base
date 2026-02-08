# Notices

Source: `wire/core/Notices.php`

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

## allowNotice()

Allow given Notice to be added?

@param Notice $item

@return bool

## formatNotice()

Format Notice text

@param Notice $item

## add()

Add a Notice object

~~~~
$notices->add(new NoticeError("An error occurred!"));
~~~~

@param Notice $item

@return Notices|WireArray

## storeNotice()

Store a persist Notice in Session

@param Notice $item

@return bool

## loadStoredNotices()

Load persist Notices stored in Session

@return int Number of Notices loaded

## removeNotice()

Remove a Notice

Like the remove() method but also removes persist notices.

@param string|Notice $item Accepts a Notice object or Notice ID string.

@return self

@since 3.0.149

## isDuplicate()

Is the given Notice a duplicate of one already here?

@param Notice $item

@return bool|Notice Returns Notice that it duplicate sor false if not a duplicate

## addLog()

Add Notice to log

@param Notice $item

## hasErrors()

Are there NoticeError items present?

@return bool

## hasWarnings()

Are there NoticeWarning items present?

@return bool

## move()

Move notices from one Wire instance to another

@param Wire $from

@param Wire $to

@param array $options Additional options:
 - `types` (array): Types to move (default=['messages','warnings','errors'])
 - `prefix` (string): Optional prefix to add to moved notices text (default='')
 - `suffix` (string): Optional suffix to add to moved notices text (default='')

@return int Number of notices moved

## getVisible()

Get all notices visible to current user

@return Notices Returns a new Notices object

@since 3.0.252

## ___render()

Render these notices as HTML

@param array $options
- `groupByType` (bool): Group notices by type? (default=true)
- `messageClass` (string): Class for messages (default=NoticeMessage)
- `messageIcon` (string): Default icon to show with notices (default: check-square)
- `warningClass` (string): Class for warnings (default=NoticeWarning)
- `warningIcon` (string): Default icon to show with warnings (default=exclamation-circle)
- `errorClass` (string): Class for errors (default=NoticeError)
- `errorIcon` (string): Default icon to show with errors (default=exclamation-triangle)
- `debugClass` (string): Class for debug items (default=NoticeDebug)
- `debugIcon` (string): Default icon for debug notices (default=bug)
- `closeClass` (string): Class for close-notices link (default=pw-notice-remove)
- `closeIcon` (string): 'Icon for close notices link (default=times)
- `listMarkup` (string): List markup (default=`<ul class='pw-notices'>{out}</ul>`)
- `itemMarkup` (string): Item markup (default=`<li class='{class}'><div>{remove}{icon}{text}</div></li>`)

@return string

@since 3.0.254

## ___renderText()

Render these Notices as plain text

Note: if this ends up in HTML, such as in a `<pre>`, you should pass the returned text
through `$sanitizer->entities()` or `htmlspecialchars()` before outputting.

@return string

@since 3.0.254
