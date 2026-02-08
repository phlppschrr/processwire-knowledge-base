# $wireInput->urlSegments(): array

Source: `wire/core/WireInput.php`

Retrieve array of all URL segments

- URL segments must be enabled in the template settings (for template used by the page).
- The maximum segments allowed can be adjusted in your `$config->maxUrlSegments` setting.
- URL segments are populated by ProcessWire automatically on each request.
- URL segments are already sanitized as page names.

## Usage

~~~~~
// basic usage
$array = $wireInput->urlSegments();
~~~~~

## Return value

- `array` Returns an array of strings, or an empty array if no URL segments available.
