# $pages->new($selector = ''): Page

Source: `wire/core/Pages.php`

Create a new Page populated from selector string or array and save to database

This is similar to the `$pages->add()` method but with a simpler 1-argument (selector) interface.
This method can also auto-detect some properties that the add() method cannot.

To create a new page without saving to the database use the `$pages->newPage()` method instead.
It accepts the same arguments as this method.

Minimum requirements to create a new page that is saved in database:

- A `template` must be specified, unless it can be auto-detected from a given `parent`.
- A `parent` must be specified, unless it can be auto-detected from a given `template` or `path`.

Please note the following:

- If a `path` is specified but not a `name` or `parent` then both will be derived from the `path`.
- If a `title` is specified but not a `name` or `path` then the `name` will be derived from the `title`.
- If given `parent` or `path` only allows one template (via family settings) then `template` becomes optional.
- If given `template` only allows one parent (via family settings) then `parent` becomes optional.
- If given selector string starts with a `/` it is assumed to be the `path` property.
- If new page has name that collides with an existing page (i.e. “foo”), new page name will increment (i.e. “foo-1”).
- If no `name`, `path` or `title` is given (that name can be derived from) then an “untitled-page” name will be used.

## Example

~~~~~
// Creating a page via selector string
$p = $pages->new("template=category, parent=/categories/, title=New Category");

// Creating a page via selector using path, which implies parent and name
$p = $pages->new("template=category, path=/categories/new-category");

// Creating a page via array
$p = $pages->new([
  'template' => 'category',
  'parent' => '/categories/',
  'title' => 'New Category'
]);

// Parent and name can be auto-detected when you specify path…
$p = $pages->new('path=/blog/posts/foo-bar-baz');

// …and even 'path=' is optional if slash '/' is at beginning
$p = $pages->new('/blog/posts/foo-bar-baz');
~~~~~

## Usage

~~~~~
// basic usage
$page = $pages->new();

// usage with all arguments
$page = $pages->new($selector = '');
~~~~~

## Arguments

- `$selector` (optional) `string|array` Selector string or array of properties to set

## Return value

- `Page`

## Hooking

- Hookable method name: `new`
- Implementation: `___new`
- Hook with: `Pages::new`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::new', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $selector = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $selector);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pages::new', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $selector = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## See Also

- [Pages::add()](method-___add.md)
- [Pages::newPage()](method-newpage.md)

## Since

3.0.191
