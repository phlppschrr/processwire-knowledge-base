# $templates->save(Saveable $item): bool

Source: `wire/core/Templates.php`

Save a Template

## Example

~~~~~
$templates->save($template);
~~~~~

## Usage

~~~~~
// basic usage
$bool = $templates->save($item);

// usage with all arguments
$bool = $templates->save(Saveable $item);
~~~~~

## Hookable

- Hookable method name: `save`
- Implementation: `___save`
- Hook with: `$templates->save()`

## Arguments

- `$item` `Saveable|Template` Template to save

## Return value

- `bool` True on success, false on failure

## Exceptions

- `WireException`
