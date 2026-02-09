# TemplateFile: other

Source: `wire/core/TemplateFile.php`

- [$halt: bool](method-halt.md) Set to true to halt during render, or use method $this->halt();
- $filename: string Primary file to render.
- $prependFilename: array Optional file name(s) used for prepend.
- $appendFilename: array Optional file name(s) used for append.
- $currentFilename: string Current file being rendered (whether primary, prepend, append).
- $trim: bool Whether or not leading/trailing whitespace is trimmed from output (3.0.154+).
- [render(): string](method-___render.md)
- [fileFailed($filename, \Exception $e): bool](method-___filefailed.md)
