# $templates->___save(Saveable $item): bool

Source: `wire/core/Templates.php`

Save a Template

## Example

~~~~~
$templates->save($template);
~~~~~

## Usage

~~~~~
// basic usage
$bool = $templates->___save($item);

// usage with all arguments
$bool = $templates->___save(Saveable $item);
~~~~~

## Arguments

- `$item` `Saveable|Template` Template to save

## Return value

- `bool` True on success, false on failure

## Exceptions

- `WireException`
