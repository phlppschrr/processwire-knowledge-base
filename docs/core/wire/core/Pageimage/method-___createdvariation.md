# $pageimage->___createdVariation(Pageimage $image, array $data)

Source: `wire/core/Pageimage.php`

Hook called after successful creation of image variation

## Usage

~~~~~
// basic usage
$result = $pageimage->___createdVariation($image, $data);

// usage with all arguments
$result = $pageimage->___createdVariation(Pageimage $image, array $data);
~~~~~

## Arguments

- `$image` `Pageimage` The variation image that was created
- `$data` `array` Verbose associative array of data used to create the variation

## Since

3.0.180
