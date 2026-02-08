# $page->of($outputFormatting = null): bool

Source: `wire/core/Page.php`

Get or set the current output formatting state of the page

- Always returns the current output formatting state: true if ON, or false if OFF.

- To set the current output formatting state, provide a boolean true to turn it ON, or boolean false to turn it OFF.

- Pages used for front-end output should have output formatting turned ON.

- Pages that you are manipulating and saving should have output formatting turned OFF.

See this post about [output formatting](https://processwire.com/blog/posts/output-formatting/).

~~~~~
// Set output formatting state off, for page manipulation
$page->of(false);
$page->title = 'About Us';
$page->save();
~~~~~

## Arguments

- `$outputFormatting` (optional) `bool` If specified, sets output formatting state ON or OFF. If not specified, nothing is changed.

## Return value

bool Current output formatting state (before this function call, if it was changed)

## Details

- @link https://processwire.com/blog/posts/output-formatting/
