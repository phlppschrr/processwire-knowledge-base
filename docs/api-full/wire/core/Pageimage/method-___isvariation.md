# $pageimage->isVariation($basename, $options = array()): bool|string|array

Source: `wire/core/Pageimage.php`

Given a file name (basename), return array of info if this is a variation for this instance’s file, or false if not.

Returned array includes the following indexes:

- `original` (string): Original basename
- `url` (string): URL to image
- `path` (string): Full path + filename to image
- `width` (int): Specified width in filename
- `height` (int): Specified height in filename
- `actualWidth` (int): Actual width when checked manually
- `actualHeight` (int): Acual height when checked manually
- `crop` (string): Cropping info string or blank if none
- `suffix` (array): Array of suffixes

The following are only present if variation is based on another variation, and thus has a parent variation
image between it and the original:

- `suffixAll` (array): Contains all suffixes including among parent variations
- `parent` (array): Variation info array of direct parent variation file

## Usage

~~~~~
// basic usage
$bool = $pageimage->isVariation($basename);

// usage with all arguments
$bool = $pageimage->isVariation($basename, $options = array());
~~~~~

## Arguments

- `$basename` `string` Filename to check (basename, which excludes path)
- `$options` (optional) `array|bool` Array of options to modify behavior, or boolean to only specify `allowSelf` option. - `allowSelf` (bool): When true, it will return variation info even if same as current Pageimage. (default=false) - `verbose` (bool): Return verbose array of info? If false, just returns basename (string) or false. (default=true)

## Return value

- `bool|string|array` Returns false if not a variation, or array (verbose) or string (non-verbose) of info if it is.

## Hooking

- Hookable method name: `isVariation`
- Implementation: `___isVariation`
- Hook with: `Pageimage::isVariation`

### Hooking Before

~~~~~
$this->addHookBefore('Pageimage::isVariation', function(HookEvent $event) {
  $pageimage = $event->object;

  // Get arguments
  $basename = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $basename);
  $event->arguments(1, $options);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pageimage::isVariation', function(HookEvent $event) {
  $pageimage = $event->object;

  // Get arguments
  $basename = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
