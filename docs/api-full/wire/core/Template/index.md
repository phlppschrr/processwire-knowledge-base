# Template

Source: `wire/core/Template.php`

Inherits: `WireData`
Implements: `Saveable`, `Exportable`

## Summary

ProcessWire Template

Common methods:
- [`loaded()`](method-loaded.md)
- [`get()`](method-get.md)
- [`roleTypeNames()`](method-roletypenames.md)
- [`getRoles()`](method-getroles.md)
- [`hasRole()`](method-hasrole.md)

Groups:
Group: [identification](group-identification.md)
Group: [family](group-family.md)
Group: [URLs](group-urls.md)
Group: [access](group-access.md)
Group: [files](group-files.md)
Group: [cache](group-cache.md)
Group: [page-editor](group-page-editor.md)
Group: [behaviors](group-behaviors.md)
Group: [other](group-other.md)
Group: [fields](group-fields.md)
Group: [tags](group-tags.md)

Template is a Page’s connection to fields (via a Fieldgroup), access control, and output via a template file.
Template objects also maintain several properties which can affect the render behavior of pages using it.


@todo add multi-language option for redirectLogin setting

Identification


Fieldgroup/Fields


Cache


Access


Family


URLs


Files


Page Editor


Behaviors


Other


## Methods
- [`roleTypeNames(string|Permission $type): array`](method-roletypenames.md) Given different ways to refer to a role type return array of type, property and permission name
- [`getRoles(string $type = 'view'): PageArray`](method-getroles.md) Get the role pages that are part of this template
- [`hasRole(string|Role|Page $role, $type = 'view'): bool`](method-hasrole.md) Does this template have the given Role?
- [`setRoles(array|PageArray $value, string $type = 'view')`](method-setroles.md) Set roles for this template
- [`addRole(Role|int|string $role, string $type = 'view'): $this`](method-addrole.md) Add a Role to this template for view, edit, create, or add permission
- [`removeRole(Role|int|string $role, string $type = 'view'): $this`](method-removerole.md) Remove a Role to this template for view, edit, create, or add permission
- [`addPermissionByRole(Permission|int|string $permission, Role|int|string $role, bool $test = false): bool`](method-addpermissionbyrole.md) Add a permission that applies to users having a specific role with pages using this template
- [`revokePermissionByRole(Permission|int|string $permission, Role|int|string $role, bool $test = false): bool`](method-revokepermissionbyrole.md) Revoke a permission that applies to users having a specific role with pages using this template
- [`hasField(string|int|Field $name): bool`](method-hasfield.md) Does this template have the given Field?
- [`setCacheExpirePages(array $value)`](method-setcacheexpirepages.md) Set the cacheExpirePages property
- [`urlSegments(array|int|bool|string $value = '~'): array|int`](method-urlsegments.md) Get or set allowed URL segments
- [`isValidUrlSegmentStr(string $urlSegmentStr): bool`](method-isvalidurlsegmentstr.md) Is the given URL segment string allowed according to this template’s settings?
- [`setFlags(int $value)`](method-setflags.md) Set the flags for this Template
- [`setFilename(string $value)`](method-setfilename.md) Set this template's filename, with or without path
- [`setFieldgroup(Fieldgroup $fieldgroup): $this`](method-setfieldgroup.md) Set this Template's Fieldgroup
- [`getNumPages(): int`](method-getnumpages.md) Return the number of pages used by this template.
- [`save(): Template|bool`](method-save.md) Save the template to database
- [`filename(string $filename = null): string`](method-filename.md) Return corresponding template filename including path, or set template filename
- [`filenameExists(): bool`](method-filenameexists.md) Does the template filename exist?
- [`__toString()`](method-__tostring.md) The string value of a Template is always it's name
- [`parentTemplates(array|TemplatesArray|null $setValue = null): TemplatesArray`](method-parenttemplates.md) Get or set parent templates (templates allowed for parent pages of pages using this template)
- [`childTemplates(array|TemplatesArray|null $setValue = null): TemplatesArray|Template[]`](method-childtemplates.md) Get or set child templates (templates allowed for children of pages using this template)
- [`allowNewPages(): bool`](method-allownewpages.md) Allow new pages that use this template?
- [`getParentPage(bool $checkAccess = false): Page|NullPage|null`](method-getparentpage.md) Return the parent page that this template assumes new pages are added to
- [`getParentPages(bool $checkAccess = false): PageArray`](method-getparentpages.md) Return all defined parent pages for this template
- [`getLabel(Page|Language $language = null): string`](method-getlabel.md) Return template label for current language, or specified language if provided
- [`getTabLabel(string $tab, Page|Language $language = null): string`](method-gettablabel.md) Return page tab label for current language (or specified language if provided)
- [`getNameLabel(Language|null $language = null): string`](method-getnamelabel.md) Return the overriden "page name" label, or blank if not overridden
- [`getIcon(bool $prefix = false): string`](method-geticon.md) Return the icon name used by this template
- [`getLanguages(): PageArray|Languages|null`](method-getlanguages.md) Get languages allowed for this template or null if language support not active.
- [`getPageClass(bool $withNamespace = true): string`](method-getpageclass.md) Get class name to use for Page objects using this template
- [`getTags(): array`](method-gettags.md) Get tags array
- [`hasTag(string $tag): bool`](method-hastag.md) Does this template have given tag?
- [`addTag(string $tag): $this`](method-addtag.md) Add tag
- [`removeTag(string $tag): self`](method-removetag.md) Remove tag
- [`setIcon(string $icon): $this`](method-seticon.md) Set the icon to use with this template
- [`editUrl(bool $http = false): string`](method-editurl.md) URL to edit template settings (for administrator)

## Constants
- [`flagSystem = 8`](const-flagsystem.md)
- [`flagSystemOverride = 32768`](const-flagsystemoverride.md)
- [`cacheExpirePage = 0`](const-cacheexpirepage.md)
- [`cacheExpireSite = 1`](const-cacheexpiresite.md)
- [`cacheExpireParents = 2`](const-cacheexpireparents.md)
- [`cacheExpireSpecific = 3`](const-cacheexpirespecific.md)
- [`cacheExpireSelector = 4`](const-cacheexpireselector.md)
- [`cacheExpireNone = -1`](const-cacheexpirenone.md)

Hookable methods
