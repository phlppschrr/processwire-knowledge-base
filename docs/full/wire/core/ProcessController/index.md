# ProcessController

Source: `wire/core/ProcessController.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

A Controller for Process* Modules

Intended to be used by templates that call upon Process objects

Methods:
- [`__construct()`](method-__construct.md)
- [`setProcess(Process $process)`](method-setprocess.md)
- [`setProcessName(string $processName)`](method-setprocessname.md)
- [`setProcessMethodName(string $processMethod)`](method-setprocessmethodname.md)
- [`setPrefix(string $prefix)`](method-setprefix.md)
- [`getProcess(): Process`](method-getprocess.md)
- [`hasPermission(string $permissionName, bool $throw = true): bool`](method-haspermission.md)
- [`hasMethodPermission(string $method, bool $throw = true): bool`](method-hasmethodpermission.md)
- [`hasUrlSegmentPermission(string $urlSegment, bool $throw = true): bool`](method-hasurlsegmentpermission.md)
- [`getProcessMethodName(Process $process): string`](method-getprocessmethodname.md)
- [`execute(): string`](method-___execute.md) (hookable)
- [`getViewFile(Process $process, string $method = ''): string`](method-getviewfile.md)
- [`jsonMessage(string|array $msg, bool $error = false, bool $allowMarkup = false): string`](method-jsonmessage.md)
- [`isAjax(): bool`](method-isajax.md)

Constants:
- [`defaultProcessMethodName`](const-defaultprocessmethodname.md)
