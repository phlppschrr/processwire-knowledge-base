# Template

Source: `wire/core/Template.php`

Inherits: `WireData`
Implements: `Saveable`, `Exportable`


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

ProcessWire Template

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


Methods:
- [`roleTypeNames(string|Permission $type): array`](method-roletypenames.md)
- [`getRoles(string $type = 'view'): PageArray`](method-getroles.md)
- [`hasRole(string|Role|Page $role, $type = 'view'): bool`](method-hasrole.md)
- [`setRoles(array|PageArray $value, string $type = 'view')`](method-setroles.md)
- [`addRole(Role|int|string $role, string $type = 'view'): $this`](method-addrole.md)
- [`removeRole(Role|int|string $role, string $type = 'view'): $this`](method-removerole.md)
- [`addPermissionByRole(Permission|int|string $permission, Role|int|string $role, bool $test = false): bool`](method-addpermissionbyrole.md)
- [`revokePermissionByRole(Permission|int|string $permission, Role|int|string $role, bool $test = false): bool`](method-revokepermissionbyrole.md)
- [`hasField(string|int|Field $name): bool`](method-hasfield.md)
- [`setCacheExpirePages(array $value)`](method-setcacheexpirepages.md)
- [`urlSegments(array|int|bool|string $value = '~'): array|int`](method-urlsegments.md)
- [`isValidUrlSegmentStr(string $urlSegmentStr): bool`](method-isvalidurlsegmentstr.md)
- [`setFlags(int $value)`](method-setflags.md)
- [`setFilename(string $value)`](method-setfilename.md)
- [`setFieldgroup(Fieldgroup $fieldgroup): $this`](method-setfieldgroup.md)
- [`getNumPages(): int`](method-getnumpages.md)
- [`save(): Template|bool`](method-save.md)
- [`filename(string $filename = null): string`](method-filename.md)
- [`filenameExists(): bool`](method-filenameexists.md)
- [`__toString()`](method-__tostring.md)
- [`parentTemplates(array|TemplatesArray|null $setValue = null): TemplatesArray`](method-parenttemplates.md)
- [`childTemplates(array|TemplatesArray|null $setValue = null): TemplatesArray|Template[]`](method-childtemplates.md)
- [`allowNewPages(): bool`](method-allownewpages.md)
- [`getParentPage(bool $checkAccess = false): Page|NullPage|null`](method-getparentpage.md)
- [`getParentPages(bool $checkAccess = false): PageArray`](method-getparentpages.md)
- [`getLabel(Page|Language $language = null): string`](method-getlabel.md)
- [`getTabLabel(string $tab, Page|Language $language = null): string`](method-gettablabel.md)
- [`getNameLabel(Language|null $language = null): string`](method-getnamelabel.md)
- [`getIcon(bool $prefix = false): string`](method-geticon.md)
- [`getLanguages(): PageArray|Languages|null`](method-getlanguages.md)
- [`getPageClass(bool $withNamespace = true): string`](method-getpageclass.md)
- [`getTags(): array`](method-gettags.md)
- [`hasTag(string $tag): bool`](method-hastag.md)
- [`addTag(string $tag): $this`](method-addtag.md)
- [`removeTag(string $tag): self`](method-removetag.md)
- [`setIcon(string $icon): $this`](method-seticon.md)
- [`editUrl(bool $http = false): string`](method-editurl.md)

Constants:
- [`flagSystem`](const-flagsystem.md)
- [`flagSystemOverride`](const-flagsystemoverride.md)
- [`cacheExpirePage`](const-cacheexpirepage.md)
- [`cacheExpireSite`](const-cacheexpiresite.md)
- [`cacheExpireParents`](const-cacheexpireparents.md)
- [`cacheExpireSpecific`](const-cacheexpirespecific.md)
- [`cacheExpireSelector`](const-cacheexpireselector.md)
- [`cacheExpireNone`](const-cacheexpirenone.md)

Hookable methods
