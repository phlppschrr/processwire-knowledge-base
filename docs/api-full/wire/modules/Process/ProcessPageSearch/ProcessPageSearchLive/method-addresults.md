# $processPageSearchLive->addResults($group, array $results): true

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Add multiple results at once

## Usage

~~~~~
// basic usage
$result = $processPageSearchLive->addResults($group, $results);

// usage with all arguments
$result = $processPageSearchLive->addResults($group, array $results);
~~~~~

## Arguments

- `$group` `string` Group name for these search results
- `$results` `array` Associative array where keys are URLs and values are titles/labels

## Return value

- `true`

## Since

3.0.240
