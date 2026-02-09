# TemplateFile

Source: `wire/core/TemplateFile.php`

Inherits: `WireData`


Groups:
Group: [other](group-other.md)

ProcessWire TemplateFile

A template file that will be loaded and executed as PHP and its output returned.

Methods:
- [`__construct(string $filename = '')`](method-__construct.md)
- [`setFilename(string $filename): bool`](method-setfilename.md)
- [`setPrependFilename(string $filename): bool`](method-setprependfilename.md)
- [`setAppendFilename(string $filename): bool`](method-setappendfilename.md)
- [`setThrowExceptions(bool $throwExceptions)`](method-setthrowexceptions.md)
- [`setTrim(bool $trim)`](method-settrim.md)
- [`setChdir(string|bool $chdir)`](method-setchdir.md)
- [`render(): string|array`](method-___render.md) (hookable)
- [`fileReady(string $filename)`](method-fileready.md)
- [`fileFinished()`](method-filefinished.md)
- [`fileFailed(string $filename, \Exception $e): bool`](method-___filefailed.md) (hookable)
- [`renderReady()`](method-renderready.md)
- [`renderFinished()`](method-renderfinished.md)
- [`renderFailed(\Exception $e): \Exception`](method-renderfailed.md)
- [`setCurrentFilename(string $filename)`](method-setcurrentfilename.md)
- [`getArray(): array`](method-getarray.md)
- [`get(string $key): mixed`](method-get.md)
- [`set(string $key, mixed $value): $this|WireData`](method-set.md)
- [`getRenderStack(): array`](method-getrenderstack.md)
- [`clearAll(): int`](method-clearall.md)
- [`__toString(): string`](method-__tostring.md)
- [`halt(bool|string $halt = true): $this`](method-halt.md)
