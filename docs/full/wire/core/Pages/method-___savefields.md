# $pages->saveFields(Page $page, $fields, array $options = array()): array

Source: `wire/core/Pages.php`

Save multiple named fields from given page

## Example

~~~~~
// you can specify field names as array…
$a = $pages->saveFields($page, [ 'title', 'body', 'summary' ]);

// …or a CSV string of field names:
$a = $pages->saveFields($page, 'title, body, summary');

// return value is array of saved field/property names
print_r($a); // outputs: array( 'title', 'body', 'summary' )
~~~~~

## Usage

~~~~~
// basic usage
$array = $pages->saveFields($page, $fields);

// usage with all arguments
$array = $pages->saveFields(Page $page, $fields, array $options = array());
~~~~~

## Hookable

- Hookable method name: `saveFields`
- Implementation: `___saveFields`
- Hook with: `$pages->saveFields()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::saveFields', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $fields = $event->arguments(1);
  $options = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $fields);
  $event->arguments(2, $options);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Pages::saveFields', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $fields = $event->arguments(1);
  $options = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Page` Page to save
- `$fields` `array|string|string[]|Field[]` Array of field names to save or CSV/space separated field names to save. These should only be Field names and not native page property names.
- `$options` (optional) `array|string` Optionally specify one or more of the following to modify default behavior: - `quiet` (boolean): Specify true to bypass updating of modified user and time (default=false). - `noHooks` (boolean): Prevent before/after save hooks (default=false), please also use $pages->___saveField() for call. - See $options argument for Pages::save() for additional options

## Return value

- `array` Array of saved field names (may also include property names if they were modified)

## Exceptions

- `WireException`

## Since

3.0.242
