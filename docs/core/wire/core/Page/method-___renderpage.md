# $page->renderPage(array $options = []): string|mixed

Source: `wire/core/Page.php`

Render page output

This method is essentially the same as the `render()` method except that the `render()` method
is a gateway to this method or the `renderField()` method, and this one is not. More specifically:

- This method has only one purpose, which is rendering page output.
- This method has only has one argument, which is always an array.
- This method is available only in ProcessWire 3.0.253+.

This method is preferable to `render()` when it comes hooks or overriding in custom page classes,
as you don't need to figure out anything about the arguments.

## Example

~~~~~
// regular page render call
echo $page->renderPage();

// render while passing in custom variables
echo $page->renderPage([
  'firstName' => 'Ryan',
  'lastName' => 'Cramer'
]);

// in your template file, you can access the passed-in variables like this:
echo "<p>Full name: $options[firstName] $options[lastName]</p>";

// hoooking this method
$wire->addHookAfter('Page::renderPage', function(HookEvent $event) {
  $event->return = str_replace("</body>", "<p>Hello</p></body>", $event->return);
});
~~~~~

## Usage

~~~~~
// basic usage
$string = $page->renderPage();

// usage with all arguments
$string = $page->renderPage(array $options = []);
~~~~~

## Hookable

- Hookable method name: `renderPage`
- Implementation: `___renderPage`
- Hook with: `$page->renderPage()`

## Hooking Before

~~~~~
$this->addHookBefore('Page::renderPage', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $options = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $options);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Page::renderPage', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $options = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$options` (optional) `array` Custom variables to pass to template file, and/or options as described below: - `foo_bar` (mixed): Specify any of your own variable names and values to send to the template file (foo_bar is just an example, use your own). - `filename` (string): Filename to render, typically relative to /site/templates/. Absolute paths must resolve somewhere in PW’s install. (default='') - `prependFile` (string): Filename to prepend to output, must be in /site/templates/. - `prependFiles` (array): Array of additional filenames to prepend to output, must be relative to /site/templates/. - `appendFile` (string): Filename to append to output, must be in /site/templates/. - `appendFiles` (array): Array of additional filenames to append to output, must be relative to /site/templates/. - `allowCache` (bool): Allow cache to be used when template settings ask for it? (default=true) - `forceBuildCache` (bool): If true, the cache will be re-created for this page. (default=false) -  Note that the prepend and append options above have default values in `$config` or with the Template.

## Return value

- `string|mixed` Renders the rendered output

## Exceptions

- `WireException`

## Since

3.0.253
