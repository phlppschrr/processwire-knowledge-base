# TemplateFile

Source: `wire/core/TemplateFile.php`

Inherits: `WireData`


Groups:
Group: [other](group-other.md)

ProcessWire TemplateFile

A template file that will be loaded and executed as PHP and its output returned.

Methods:
- [`__construct(string $filename = '')`](method-__construct.md) Construct the template file
- [`setFilename(string $filename): bool`](method-setfilename.md) Sets the template file name, replacing whatever was set in the constructor
- [`setPrependFilename(string $filename): bool`](method-setprependfilename.md) Set a file to prepend to the template file at render time
- [`setAppendFilename(string $filename): bool`](method-setappendfilename.md) Set a file to append to the template file at render time
- [`setThrowExceptions(bool $throwExceptions)`](method-setthrowexceptions.md) Call this with boolean false to disable exceptions when file doesn’t exist
- [`setTrim(bool $trim)`](method-settrim.md) Set whether rendered output should have leading/trailing whitespace trimmed
- [`setChdir(string|bool $chdir)`](method-setchdir.md) Set the directory to temporarily change to during rendering
- [`render(): string|array`](method-___render.md) (hookable) Render the template: execute it and return its output
- [`fileReady(string $filename)`](method-fileready.md) Prepare to nclude specific file (whether prepend, main or append)
- [`fileFinished()`](method-filefinished.md) Clean up after include specific file
- [`fileFailed(string $filename, \Exception $e): bool`](method-___filefailed.md) (hookable) Called when render of specific file failed with Exception
- [`renderReady()`](method-renderready.md) Prepare to render
- [`renderFinished()`](method-renderfinished.md) Cleanup after render
- [`renderFailed(\Exception $e): \Exception`](method-renderfailed.md) Called when overall render failed
- [`setCurrentFilename(string $filename)`](method-setcurrentfilename.md) Set the current filename being rendered
- [`getArray(): array`](method-getarray.md) Get an array of all variables accessible (locally scoped) to the PHP template file
- [`get(string $key): mixed`](method-get.md) Get a set property from the template file, typically to check if a template has access to a given variable
- [`set(string $key, mixed $value): $this|WireData`](method-set.md) Set a property
- [`getRenderStack(): array`](method-getrenderstack.md) Get the current render stack
- [`clearAll(): int`](method-clearall.md) Clear out all pending output buffers
- [`__toString(): string`](method-__tostring.md) The string value of a TemplateFile is its PHP template filename OR its class name if no filename is set
- [`halt(bool|string $halt = true): $this`](method-halt.md) This method can be called by any template file to stop further render inclusions
