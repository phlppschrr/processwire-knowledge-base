# $pageFinder->getQueryUnknownField($fieldName, array $data): bool|Field|int

Source: `wire/core/PageFinder.php`

Hook called when an unknown field is found in the selector

By default, PW will throw a PageFinderSyntaxException but that behavior can be overridden by
hooking this method and making it return true rather than false. It may also choose to
map it to a Field by returning a Field object. If it returns integer 1 then it indicates the
fieldName mapped to an API variable. If this method returns false, then it signals the getQuery()
method that it was unable to map it to anything and should be considered a fail.

## Usage

~~~~~
// basic usage
$bool = $pageFinder->getQueryUnknownField($fieldName, $data);

// usage with all arguments
$bool = $pageFinder->getQueryUnknownField($fieldName, array $data);
~~~~~

## Hookable

- Hookable method name: `getQueryUnknownField`
- Implementation: `___getQueryUnknownField`
- Hook with: `$pageFinder->getQueryUnknownField()`

## Hooking Before

~~~~~
$this->addHookBefore('PageFinder::getQueryUnknownField', function(HookEvent $event) {
  $pageFinder = $event->object;

  // Get arguments
  $fieldName = $event->arguments(0);
  $data = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $fieldName);
  $event->arguments(1, $data);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('PageFinder::getQueryUnknownField', function(HookEvent $event) {
  $pageFinder = $event->object;

  // Get arguments
  $fieldName = $event->arguments(0);
  $data = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$fieldName` `string`
- `$data` `array` Array of data containing the following in it: - `subfield` (string): First subfield - `subfields` (string): All subfields separated by period (i.e. subfield.tertiaryfield) - `fields` (array): Array of all other field names being processed in this selector. - `query` (DatabaseQuerySelect): Database query select object - `selector` (Selector): Selector that contains this field - `selectors` (Selectors): All the selectors

## Return value

- `bool|Field|int`

## Exceptions

- `PageFinderSyntaxException`
