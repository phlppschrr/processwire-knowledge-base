# Wire::message()

Source: `wire/core/Wire.php`

Record an informational or “success” message in the system-wide notices.

This method automatically identifies the message as coming from this class.

~~~~~
$this->message("This is the notice text");
$this->message("This notice is also logged", true);
$this->message("This notice is only shown in debug mode", Notice::debug);
$this->message("This notice allows <em>markup</em>", Notice::allowMarkup);
$this->message("Notice using multiple flags", Notice::debug | Notice::logOnly);
~~~~~


@param string|array|Wire $text Text to include in the notice

@param int|bool|string $flags Optional flags to alter default behavior:
 - `Notice::admin` (constant): Show notice only if user is in the admin.
 - `Notice::allowMarkdown` (constant): Allow basic markdown and bracket markup (see $sanitizer->entitiesMarkdown()).
 - `Notice::allowMarkup` (constant): Indicates notice should allow the use of HTML markup tags.
 - `Notice::debug` (constant): Indicates notice should only be shown when debug mode is active.
 - `Notice::log` (constant): Indicates notice should also be logged.
 - `Notice::logOnly` (constant): Indicates notice should only be logged.
 - `Notice::login` (constant): Show notice only if it will be seen by a logged-in user.
 - `Notice::noGroup` (constant): Indicates notice should not group with others of the same type (where supported).
 - `Notice::prepend` (constant): Indicates notice should prepend rather than append.
 - `Notice::superuser` (constant): Show notice only if current user is a superuser.
 - `true` (boolean): Shortcut for the `Notice::log` constant.
 - In 3.0.149+ you may also specify a space-separated string of flag names, i.e. "admin log noGroup".

@return $this

@see Wire::messages(), Wire::warning(), Wire::error()
