# $processPageSearchLive->useType($type, $requestType = ''): bool

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Allow this search type?

## Usage

~~~~~
// basic usage
$bool = $processPageSearchLive->useType($type);

// usage with all arguments
$bool = $processPageSearchLive->useType($type, $requestType = '');
~~~~~

## Arguments

- `$type` `string` Type to check
- `$requestType` (optional) `string` Type specifically requested by user

## Return value

- `bool`
