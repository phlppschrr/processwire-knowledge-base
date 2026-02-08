# Process: other

Source: `wire/core/Process.php`

@method string|array execute()

@method string|array executeUnknown() Called when urlSegment matches no execute[Method], only if implemented.

@method Process headline(string $headline)

@method Process browserTitle(string $title)

@method Process breadcrumb(string $href, string $label)

@method void install()

@method void uninstall()

@method void upgrade($fromVersion, $toVersion)

@method void ready()

@method void setConfigData(array $data)

@method void executed($methodName) Hook called after a method has been executed in the Process
