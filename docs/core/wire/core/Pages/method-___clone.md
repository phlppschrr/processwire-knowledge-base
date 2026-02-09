# $pages->clone(Page $page, ?Page $parent = null, $recursive = true, $options = array()): Page|NullPage

Source: `wire/core/Pages.php`

Clone entire page and return it

This also clones any file assets assets associated with the page. The clone is recursive
by default, cloning children (and so on) as well. To clone only the page without children,
specify false for the `$recursive` argument.

Warning: this method can fail when recursive and cloning a page with huge amounts of
children (or descendent family), and adequate resources (like memory or time limit) are
not available.

## Example

~~~~~
// Clone the Westin Peachtree skyscraper page
$building = $pages->get('/skyscrapers/atlanta/westin-peachtree/');
$copy = $pages->clone($building);

// Bonus: Now that the clone exists, lets move and rename it
$copy->parent = '/skyscrapers/detroit/';
$copy->title = 'Renaissance Center';
$copy->name = 'renaissance-center';
$copy->save();
~~~~~

## Usage

~~~~~
// basic usage
$page = $pages->clone($page);

// usage with all arguments
$page = $pages->clone(Page $page, ?Page $parent = null, $recursive = true, $options = array());
~~~~~

## Hookable

- Hookable method name: `clone`
- Implementation: `___clone`
- Hook with: `$pages->clone()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::clone', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $parent = $event->arguments(1);
  $recursive = $event->arguments(2);
  $options = $event->arguments(3);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $parent);
  $event->arguments(2, $recursive);
  $event->arguments(3, $options);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Pages::clone', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $parent = $event->arguments(1);
  $recursive = $event->arguments(2);
  $options = $event->arguments(3);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Page` Page that you want to clone
- `$parent` (optional) `Page|null` New parent, if different (default=null, which implies same parent)
- `$recursive` (optional) `bool` Clone the children too? (default=true)
- `$options` (optional) `array|string` Options that can be passed to modify default behavior of clone or save: - `forceID` (int): force a specific ID. - `set` (array): Array of properties to set to the clone (you can also do this later). - `recursionLevel` (int): recursion level, for internal use only.

## Return value

- `Page|NullPage` The newly cloned Page or a NullPage() with id=0 if unsuccessful.

## Exceptions

- `WireException|\Exception` on fatal error
