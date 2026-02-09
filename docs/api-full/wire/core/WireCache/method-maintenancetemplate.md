# $wireCache->maintenanceTemplate(Template $template): bool

Source: `wire/core/WireCache.php`

Run maintenance for a template that was just saved or deleted

## Usage

~~~~~
// basic usage
$bool = $wireCache->maintenanceTemplate($template);

// usage with all arguments
$bool = $wireCache->maintenanceTemplate(Template $template);
~~~~~

## Arguments

- `$template` `Template`

## Return value

- `bool` Returns true if any caches were deleted, false if not
