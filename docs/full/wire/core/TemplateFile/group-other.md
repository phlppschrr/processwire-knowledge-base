# TemplateFile: other

Source: `wire/core/TemplateFile.php`

@property bool $halt Set to true to halt during render, or use method $this->halt();

@property-read string $filename Primary file to render.

@property-read array $prependFilename Optional file name(s) used for prepend.

@property-read array $appendFilename Optional file name(s) used for append.

@property-read string $currentFilename Current file being rendered (whether primary, prepend, append).

@property-read bool $trim Whether or not leading/trailing whitespace is trimmed from output (3.0.154+).

@method string render()

@method bool fileFailed($filename, \Exception $e)
