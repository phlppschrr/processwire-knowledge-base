# $pages->of($of = null): bool

Source: `wire/core/Pages.php`

Get or set the current output formatting state

This affects pages loaded after this method has been called.
By default, output formatting is turned on on the front-end of the site,
and off on the back-end (admin) of the site.

~~~~~
// Dictate that loaded pages should have output formatting enabled
$pages->of(true);

// Get the output formatting state for future loaded pages
if($pages->of()) {
  echo "Output formatting is ON";
} else {
  echo "Output formatting is OFF";
}
~~~~~

## Arguments

- `$of` (optional) `null|bool` Specify boolean to set output formatting state, or omit to get output formatting state.

## Return value

bool Returns current output formatting state.
