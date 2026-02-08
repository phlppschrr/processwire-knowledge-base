# InputfieldTinyMCETools

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCETools.php`

InputfieldTinyMCETools

Helper tools for InputfieldTinyMCE module.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## other

@property array $jsonBlankObjectProperties

## sanitizeNames()

Sanitize toolbar or plugin names

@param string|array $value

@return string

## getImageField()

Get field that images can be uploaded to or null if none found

@return Field|null

## purifyValue()

Clean up a value that will be sent to/from the editor

This is primarily for HTML Purifier

@param string $value

@return string

## purifyValueToggles()

Apply markup cleaning toggles

@param string $value

@return string

## purifier()

@return MarkupHTMLPurifier

## linkConfig()

Get config for ProcessPageEditLink module

@param string $key

@return array|string

## jsonDecode()

Decode JSON

@param string $json JSON string

@param string $propertyName Name of property JSON is for

@return array

## jsonDecodeFile()

Decode JSON file

@param string $file

@param string $propertyName

@return array

## jsonEncode()

Encode array to JSON

@param array $a

@param string $propertyName Name of property JSON is for

@param bool $pretty

@return string

## getPasteFiltersForJS()

Prepare pasteFilters string for JS

This converts the rules to a longer format that is optimized for matching from the
InputfieldTinyMCE.js pasteProcess() function.

@return string

## __get()

Get content.css file contents for inline editor output

@return string

@deprecated

public function getContentCssInline() {
$file = $this->getContentCssFile();
$css = file_get_contents($file);
$css = str_replace(array("\n", "\t", "\r", "  "), " ", $css);
$css = str_replace('}', "}\n", $css);
while(strpos($css, '  ') !== false) $css = str_replace('  ', ' ', $css);
$css = str_replace(array(' { ', ' } ', '; ', ': ', ', ', ';}'), array('{', '}', ';', ':', ',', '}'), $css);
$lines = explode("\n", $css);
foreach($lines as $key => $line) {
$line = trim($line);
if(empty($line)) {
unset($lines[$key]);
continue;
}
if(strpos($line, '{')) {
list($a, $b) = explode('{', $line, 2);
$a = str_replace(',', ',.mce-content-body ', $a);
$line = $a . '{' . $b;
}
if(strpos($line, 'body{') === 0) $line = str_replace('body{', '{', $line);
$lines[$key] = ".mce-content-body $line";
}
return implode("\n", $lines);
}

## __get()

@param string $name

@return array|mixed|string|null
