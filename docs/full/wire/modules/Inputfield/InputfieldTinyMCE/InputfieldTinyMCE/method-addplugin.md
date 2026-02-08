# $inputfieldTinyMCE->addPlugin($file)

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCE.module.php`

Add an external plugin .js file

## Usage

~~~~~
// basic usage
$result = $inputfieldTinyMCE->addPlugin($file);
~~~~~

## Arguments

- `$file` `string` File must be .js file relative to PW installation root, i.e. /site/templates/mce/myplugin.js

## Exceptions

- `WireException`
