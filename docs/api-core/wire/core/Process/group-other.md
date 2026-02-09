# Process: other

Source: `wire/core/Process.php`

- [`execute(): string|array`](method-___execute.md)
- [`executeUnknown(): string|array`](method-executeunknown.md) Called when urlSegment matches no execute[Method], only if implemented.
- [`headline(string $headline): Process`](method-___headline.md)
- [`browserTitle(string $title): Process`](method-___browsertitle.md)
- [`breadcrumb(string $href, string $label): Process`](method-___breadcrumb.md)
- [`install(): void`](method-___install.md)
- [`uninstall(): void`](method-___uninstall.md)
- [`upgrade($fromVersion, $toVersion): void`](method-___upgrade.md)
- [`ready(): void`](method-ready.md)
- [`setConfigData(array $data): void`](method-setconfigdata.md)
- [`executed($methodName): void`](method-___executed.md) Hook called after a method has been executed in the Process
