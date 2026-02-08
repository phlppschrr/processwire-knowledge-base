# Template: files

Source: `wire/core/Template.php`

@property string $filename Template filename, including path (this is auto-generated from the name, though you may modify it at runtime if it suits your need).

@property string $altFilename Alternate filename for template file, if not based on template name.

@property string $contentType Content-type header or index (extension) of content type header from $config->contentTypes

@property int|bool $noPrependTemplateFile Disable automatic prepend of $config->prependTemplateFile (if in use).

@property int|bool $noAppendTemplateFile Disabe automatic append of $config->appendTemplateFile (if in use).

@property string $prependFile File to prepend to template file (separate from $config->prependTemplateFile).

@property string $appendFile File to append to template file (separate from $config->appendTemplateFile).

@property int $pagefileSecure Use secure pagefiles for pages using this template? 0=No/not set, 1=Yes (for non-public pages), 2=Always (3.0.166+)
