# WireProfilerInterface

Source: `wire/core/Interfaces.php`

Interface for tracking runtime events

Methods:
- [`start(string $name, $source = null, array $data = array()): mixed`](method-start.md) Start profiling an event
- [`stop(array|object|string $event): void`](method-stop.md) Stop profiling an event
- [`maintenance(): void`](method-maintenance.md) End of request maintenance
