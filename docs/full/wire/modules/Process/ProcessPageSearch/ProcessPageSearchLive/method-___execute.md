# $processPageSearchLive->execute($getJSON = true): string|array

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Execute live search and return JSON result

## Usage

~~~~~
// basic usage
$string = $processPageSearchLive->execute();

// usage with all arguments
$string = $processPageSearchLive->execute($getJSON = true);
~~~~~

## Hookable

- Hookable method name: `execute`
- Implementation: `___execute`
- Hook with: `$processPageSearchLive->execute()`

## Arguments

- `$getJSON` (optional) `bool` Get results as JSON string? Specify false to get array instead.

## Return value

- `string|array`
