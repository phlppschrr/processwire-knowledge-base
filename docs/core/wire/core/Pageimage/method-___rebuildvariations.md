# $pageimage->rebuildVariations($mode = 0, array $suffix = array(), array $options = array()): array

Source: `wire/core/Pageimage.php`

Rebuilds variations of this image

By default, this excludes crops and images with suffixes, but can be overridden with the `$mode` and `$suffix` arguments.

**Options for $mode argument**

- `0` (int): Rebuild only non-suffix, non-crop variations, and those w/suffix specified in $suffix argument. ($suffix is INCLUSION list)
- `1` (int): Rebuild all non-suffix variations, and those w/suffix specifed in $suffix argument. ($suffix is INCLUSION list)
- `2` (int): Rebuild all variations, except those with suffix specified in $suffix argument. ($suffix is EXCLUSION list)
- `3` (int): Rebuild only variations specified in the $suffix argument. ($suffix is ONLY-INCLUSION list)
- `4` (int): Rebuild only non-proportional, non-crop variations (variations that specify both width and height)

Mode 0 is the only truly safe mode, as in any other mode there are possibilities that the resulting
rebuild of the variation may not be exactly what was intended. The issues with other modes primarily
arise when the suffix means something about the technical details of the produced image, or when
rebuilding variations that include crops from an original image that has since changed dimensions or crops.

## Usage

~~~~~
// basic usage
$array = $pageimage->rebuildVariations();

// usage with all arguments
$array = $pageimage->rebuildVariations($mode = 0, array $suffix = array(), array $options = array());
~~~~~

## Arguments

- `$mode` (optional) `int` See the options for $mode argument above (default=0).
- `$suffix` (optional) `array` Optional argument to specify suffixes to include or exclude (according to $mode).
- `$options` (optional) `array` See $options for `Pageimage::size()` for details.

## Return value

- `array` Returns an associative array with with the following indexes: - `rebuilt` (array): Names of files that were rebuilt. - `skipped` (array): Names of files that were skipped. - `errors` (array): Names of files that had errors. - `reasons` (array): Reasons why files were skipped or had errors, associative array indexed by file name.

## Hooking

- Hookable method name: `rebuildVariations`
- Implementation: `___rebuildVariations`
- Hook with: `Pageimage::rebuildVariations`

### Hooking Before

~~~~~
$this->addHookBefore('Pageimage::rebuildVariations', function(HookEvent $event) {
  $pageimage = $event->object;

  // Get arguments
  $mode = $event->arguments(0);
  $suffix = $event->arguments(1);
  $options = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $mode);
  $event->arguments(1, $suffix);
  $event->arguments(2, $options);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pageimage::rebuildVariations', function(HookEvent $event) {
  $pageimage = $event->object;

  // Get arguments
  $mode = $event->arguments(0);
  $suffix = $event->arguments(1);
  $options = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
