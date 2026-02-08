# $inputfieldTinyMCE->removePlugin($file): bool

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCE.module.php`

Remove an external plugin .js file

## Usage

~~~~~
// basic usage
$bool = $inputfieldTinyMCE->removePlugin($file);
~~~~~

## Arguments

- `$file` `string` File must be .js file relative to PW installation root, i.e. /site/templates/mce/myplugin.js

## Return value

- `bool`
