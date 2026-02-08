# $templateFile->halt($halt = true): $this

Source: `wire/core/TemplateFile.php`

This method can be called by any template file to stop further render inclusions

This is preferable to doing an exit; or die() from your template file(s), as it only halts the rendering
of output and doesn't halt the rest of ProcessWire.

Can be called from prepend/append files as well.

USAGE from template file is: return $this->halt();

## Arguments

- `$halt` (optional) `bool|string` If given boolean, it will set the halt status. If given string, it will be output (3.0.239+)

## Return value

$this
