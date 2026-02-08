# $inputfieldTinyMCEFormats->applyStyleFormatsCSS($css, array &$settings, $defaults)

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCEFormats.php`

Add CSS that converts to style_formats and content_style

Easier-to-use alternative to the importcss plugin

## Usage

~~~~~
// basic usage
$result = $inputfieldTinyMCEFormats->applyStyleFormatsCSS($css, $settings, $defaults);

// usage with all arguments
$result = $inputfieldTinyMCEFormats->applyStyleFormatsCSS($css, array &$settings, $defaults);
~~~~~

## Arguments

- `$css` `string` From the styleFormatsCSS setting
- `$settings` `array`
- `$defaults` `array`
