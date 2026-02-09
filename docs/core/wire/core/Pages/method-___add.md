# $pages->add($template, $parent, $name = '', array $values = array()): Page

Source: `wire/core/Pages.php`

Add a new page using the given template and parent

If no page “name” is specified, one will be automatically assigned.

For an alternate interface for adding new pages, see the `$pages->new()` method.

## Example

~~~~~
// Add new page using 'skyscraper' template into Atlanta
$building = $pages->add('skyscraper', '/skyscrapers/atlanta/');

// Same as above, but with specifying a name/title as well:
$building = $pages->add('skyscraper', '/skyscrapers/atlanta/', 'Symphony Tower');

// Same as above, but with specifying several properties:
$building = $pages->add('skyscraper', '/skyscrapers/atlanta/', [
  'title' => 'Symphony Tower',
  'summary' => 'A 41-story skyscraper located at 1180 Peachtree Street',
  'height' => 657,
  'floors' => 41
]);
~~~~~

## Usage

~~~~~
// basic usage
$page = $pages->add($template, $parent);

// usage with all arguments
$page = $pages->add($template, $parent, $name = '', array $values = array());
~~~~~

## Arguments

- `$template` `string|Template` Template name or Template object
- `$parent` `string|int|Page` Parent path, ID or Page object
- `$name` (optional) `string` Optional name or title of page. If none provided, one will be automatically assigned. If you want to specify a different name and title then specify the $name argument, and $values['title'].
- `$values` (optional) `array` Field values to assign to page (optional). If $name is omitted, this may also be 3rd param.

## Return value

- `Page` New page ready to populate. Note that this page has output formatting off.

## Hooking

- Hookable method name: `add`
- Implementation: `___add`
- Hook with: `Pages::add`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::add', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $template = $event->arguments(0);
  $parent = $event->arguments(1);
  $name = $event->arguments(2);
  $values = $event->arguments(3);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $template);
  $event->arguments(1, $parent);
  $event->arguments(2, $name);
  $event->arguments(3, $values);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pages::add', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $template = $event->arguments(0);
  $parent = $event->arguments(1);
  $name = $event->arguments(2);
  $values = $event->arguments(3);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException` When some criteria prevents the page from being saved.

## See Also

- [Pages::new()](method-___new.md)
- [Pages::newPage()](method-newpage.md)
