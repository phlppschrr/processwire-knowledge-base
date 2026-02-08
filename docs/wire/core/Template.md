# Template

Source: `wire/core/Template.php`

ProcessWire Template

Template is a Page’s connection to fields (via a Fieldgroup), access control, and output via a template file.
Template objects also maintain several properties which can affect the render behavior of pages using it.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

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


Hookable methods

## identification

@property int $id Numeric database ID.

@property string $name Name of template.

@property string $label Optional short text label to describe Template.

@property int $flags Flags (bitmask) assigned to this template. See the flag constants.

@property string $ns Namespace found in the template file, or blank if not determined.

@property string $pageClass Class for instantiated page objects. Page assumed if blank, or specify class name.

## family

@property string $sortfield Field that children of templates using this page should sort by (leave blank to let page decide, or specify "sort" for manual drag-n-drop).

@property int $noChildren Set to 1 to cancel use of childTemplates.

@property int $noParents Set to 1 to cancel use of parentTemplates, set to -1 to only allow one page using this template to exist.

@property int[] $childTemplates Array of template IDs that are allowed for children. Blank array indicates "any".

@property int[] $parentTemplates Array of template IDs that are allowed for parents. Blank array indicates "any".

@property string $childNameFormat Name format for child pages. when specified, the page-add UI step can be skipped when adding children. Counter appended till unique. Date format assumed if any non-pageName chars present. Use 'title' to pull from title field.

## URLs

@property int $allowPageNum Allow page numbers in URLs? (0=no, 1=yes)

@property int|string $urlSegments Allow URL segments on pages? (0=no, 1=yes (all), string=space separted list of segments to allow)

@property int $https Use https? (0 = http or https, 1 = https only, -1 = http only)

@property int $slashUrls Page URLs should have a trailing slash? 1 = yes, 0 = no

@property string|int $slashPageNum Should PageNum segments have a trailing slash? (0=either, 1=yes, -1=no) applies only if allowPageNum!=0.

@property string|int $slashUrlSegments Should last URL segment have a trailing slash? (0=either, 1=yes, -1=no) applies only if urlSegments!=0.

## access

@property int|bool $useRoles Whether or not this template defines access.

@property PageArray $roles Roles assigned to this template for view access.

@property array $editRoles Array of Role IDs that may edit pages using this template.

@property array $addRoles Array of Role IDs that may add pages using this template.

@property array $createRoles Array of Role IDs that may create pages using this template.

@property array $rolesPermissions Override permissions: Array indexed by role ID with values as permission ID (add) or negative permission ID (revoke).

@property int $noInherit Disable role inheritance? Specify 1 to prevent edit/create/add access from inheriting to children, or 0 for default inherit behavior.

@property int $redirectLogin Redirect when no access: 0 = 404, 1 = login page, url = URL to redirect to, int(>1) = ID of page to redirect to.

@property int $guestSearchable Pages appear in search results even when user doesnt have access? (0=no, 1=yes)

## files

@property string $filename Template filename, including path (this is auto-generated from the name, though you may modify it at runtime if it suits your need).

@property string $altFilename Alternate filename for template file, if not based on template name.

@property string $contentType Content-type header or index (extension) of content type header from $config->contentTypes

@property int|bool $noPrependTemplateFile Disable automatic prepend of $config->prependTemplateFile (if in use).

@property int|bool $noAppendTemplateFile Disabe automatic append of $config->appendTemplateFile (if in use).

@property string $prependFile File to prepend to template file (separate from $config->prependTemplateFile).

@property string $appendFile File to append to template file (separate from $config->appendTemplateFile).

@property int $pagefileSecure Use secure pagefiles for pages using this template? 0=No/not set, 1=Yes (for non-public pages), 2=Always (3.0.166+)

## cache

@property int $cacheTime Number of seconds pages using this template should cache for, or 0 for no cache. Negative values indicates setting used for external caching engine like ProCache.

@property string $noCacheGetVars GET vars that trigger disabling the cache (only when cache_time > 0)

@property string $noCachePostVars POST vars that trigger disabling the cache (only when cache_time > 0)

@property int $useCacheForUsers Use cache for: 0 = only guest users, 1 = guests and logged in users

@property int $cacheExpire Expire the cache for all pages when page using this template is saved? (1 = yes, 0 = no- only current page)

@property array $cacheExpirePages Array of Page IDs that should be expired, when cacheExpire == Template::cacheExpireSpecific

@property string $cacheExpireSelector Selector string matching pages that should be expired, when cacheExpire == Template::cacheExpireSelector

## page-editor

@property int $nameContentTab Pages should display the name field on the content tab? (0=no, 1=yes)

@property string $tabContent Optional replacement for default "Content" label

@property string $tabChildren Optional replacement for default "Children" label

@property string $nameLabel Optional replacement for the default "Name" label on pages using this template

@property int $errorAction Action to take when published page missing required field is saved (0=notify only, 1=restore prev value, 2=unpublish page)

## behaviors

@property int $allowChangeUser Allow the createdUser/created_users_id field of pages to be changed? (with API or in admin w/superuser only). 0=no, 1=yes

@property int $noGlobal Template should ignore the global option of fields? (0=no, 1=yes)

@property int $noMove Pages using this template are not moveable? (0=moveable, 1=not movable)

@property int $noTrash Pages using this template may not go in trash? (i.e. they will be deleted not trashed) (0=trashable, 1=not trashable)

@property int $noSettings Don't show a settings tab on pages using this template? (0=use settings tab, 1=no settings tab)

@property int $noChangeTemplate Don't allow pages using this template to change their template? (0=template change allowed, 1=template change not allowed)

@property int $noUnpublish Don't allow pages using this template to ever exist in an unpublished state - if page exists, it must be published. (0=page may be unpublished, 1=page may not be unpublished)

@property int $noShortcut Don't allow pages using this template to appear in shortcut "add new page" menu.

@property int $noLang Disable multi-language for this template (when language support active).

## other

@property int $modified Last modified time for template or template file

@property int $compile Set to 1 to enable compilation, 2 to compile file and included files, 3 for auto, or 0 to disable.

@property string $pageLabelField CSV or space separated string of field names to be displayed by ProcessPageList (overrides those set with ProcessPageList config).

## fields

@property Fieldgroup|Field[] $fieldgroup The Fieldgroup used by the template. Can also be used to iterate a Template's fields.

@property Fieldgroup|null $fieldgroupPrevious Previous fieldgroup, if it was changed. Null if not.

## tags

@property string $tags Optional tags that can group this template with others in the admin templates list.

## flagSystem

Flag used to indicate the field is a system-only field and thus can't be deleted or have it's name changed

## flagSystemOverride

Flag set if you need to override the system flag - set this first, then remove system flag in 2 operations.

## cacheExpirePage

Cache expiration options: expire only page cache

## cacheExpireSite

Cache expiration options: expire entire site cache

## cacheExpireParents

Cache expiration options: expire page and parents

## cacheExpireSpecific

Cache expiration options: expire page and other specific pages (stored in cacheExpirePages)

## cacheExpireSelector

Cache expiration options: expire pages matching a selector

## cacheExpireNone

Cache expiration options: don't expire anything

## roleTypeNames()

Given different ways to refer to a role type return array of type, property and permission name

@param string|Permission $type

@return array Returns array of [ typeName, propertyName, permissionName ]

@since 3.0.153

## getRoles()

Get the role pages that are part of this template

- This method returns a blank PageArray if roles haven’t yet been loaded into the template.
- If the roles have previously been loaded as an array, then this method converts that array
  to a PageArray and returns it.
- If you make changes to returned roles, make sure to set it back to the template again with setRoles().
  It’s preferable to make changes with addRole() and removeRole() methods instead.


@param string $type Default is 'view', but you may also specify 'edit', 'create' or 'add' to retrieve those.

@return PageArray of Role objects.

@throws WireException if given an unknown roles type

## hasRole()

Does this template have the given Role?


@param string|Role|Page $role Name of Role or Role object.

@param string|Permission Specify one of the following:
 - `view` (default)
 - `edit`
 - `create`
 - `add`
 - Or a `Permission` object of `page-view` or `page-edit`

@return bool True if template has the role, false if not

## setRoles()

Set roles for this template


@param array|PageArray $value Role objects or array or Role IDs.

@param string $type Specify one of the following:
 - `view` (default)
 - `edit`
 - `create`
 - `add`
 - Or a `Permission` object of `page-view` or `page-edit`

## addRole()

Add a Role to this template for view, edit, create, or add permission

@param Role|int|string $role Role instance, id or name

@param string $type Type of role being added, one of: view, edit, create, add. (default=view)

@return $this

@throws WireException If given $role cannot be resolved

## removeRole()

Remove a Role to this template for view, edit, create, or add permission

@param Role|int|string $role Role instance, id or name

@param string $type Type of role being added, one of: view, edit, create, add. (default=view)
  You may also specify “all” to remove the role entirely from all possible usages in the template.

@return $this

@throws WireException If given $role cannot be resolved

## addPermissionByRole()

Add a permission that applies to users having a specific role with pages using this template

Note that the change is not committed until you save() the template.

@param Permission|int|string $permission Permission object, name, or id

@param Role|int|string $role Role object, name or id

@param bool $test Specify true to only test if an update would be made, without changing anything

@return bool Returns true if an update was made (or would be made), false if not

## revokePermissionByRole()

Revoke a permission that applies to users having a specific role with pages using this template

Note that the change is not committed until you save() the template.

@param Permission|int|string $permission Permission object, name, or id

@param Role|int|string $role Role object, name or id

@param bool $test Specify true to only test if an update would be made, without changing anything

@return bool Returns true if an update was made (or would be made), false if not

## hasField()

Does this template have the given Field?


@param string|int|Field $name May be field name, id or object.

@return bool

## setCacheExpirePages()

Set the cacheExpirePages property

@param array $value

## urlSegments()

Get or set allowed URL segments


@param array|int|bool|string $value Omit to return current value, or to set value:
 - Specify array of allowed URL segments, may include 'segment', 'segment/path' or 'regex:your-regex'.
	- Or specify boolean true or 1 to enable all URL segments.
	- Or specify integer 0, boolean false, or blank array to disable all URL segments.

@return array|int Returns array of allowed URL segments, or 0 if disabled, or 1 if any allowed.

## isValidUrlSegmentStr()

Is the given URL segment string allowed according to this template’s settings?


@param string $urlSegmentStr

@return bool

@since 3.0.186

## setFlags()

Set the flags for this Template

As a safety it prevents the system flag from being removed.

@param int $value

## setFilename()

Set this template's filename, with or without path

@param string $value The filename with or without path

@deprecated Now just using filename() method

## setFieldgroup()

Set this Template's Fieldgroup


@param Fieldgroup $fieldgroup

@return $this

@throws WireException

## getNumPages()

Return the number of pages used by this template.


@return int

## save()

Save the template to database

This is the same as calling `$templates->save($template)`.


@return Template|bool Returns Template if successful, or false if not

## filename()

Return corresponding template filename including path, or set template filename


@param string $filename Specify basename or path+basename to set, or omit to get filename. This argument added 3.0.143.

@return string

@throws WireException

## filenameExists()

Does the template filename exist?


@return bool

## __toString()

The string value of a Template is always it's name

## parentTemplates()

Get or set parent templates (templates allowed for parent pages of pages using this template)

- May be specified as template IDs or names in an array, or Template objects in a TemplatesArray.
- To allow any template as parent, specify a blank array.
- To disallow any parents (other than what’s already in use) set the `$template->noParents` property to 1.


@param array|TemplatesArray|null $setValue Specify only when setting, an iterable value containing Template objects, IDs or names

@return TemplatesArray

@since 3.0.153

## childTemplates()

Get or set child templates (templates allowed for children of pages using this template)

- May be specified as template IDs or names in an array, or Template objects in a TemplatesArray.
- To allow any template to be used for children, specify a blank array.
- To disallow any children (other than what’s already in use) set the `$template->noChildren` property to 1.


@param array|TemplatesArray|null $setValue Specify only when setting, an iterable value containing Template objects, IDs or names

@return TemplatesArray|Template[]

@since 3.0.153

## allowNewPages()

Allow new pages that use this template?


@return bool

@since 3.0.153

## getParentPage()

Return the parent page that this template assumes new pages are added to

This is based on family settings, when applicable.
It also takes into account user access, if requested (see arg 1).

If there is no defined parent, NULL is returned.
If there are multiple defined parents, a NullPage is returned.


@param bool $checkAccess Whether or not to check for user access to do this (default=false).

@return Page|NullPage|null

## getParentPages()

Return all defined parent pages for this template


@param bool $checkAccess Specify true to exclude parents that user doesn't have access to add children to (default=false)

@return PageArray

## getLabel()

Return template label for current language, or specified language if provided

If no template label, return template name.
This is different from `$template->label` in that it knows about languages (when installed)
and it will always return something. If there's no label, you'll still get the name.


@param Page|Language $language Optional, if not used then user's current language is used

@return string

## getTabLabel()

Return page tab label for current language (or specified language if provided)


@param string $tab Which tab? 'content' or 'children'

@param Page|Language $language Optional, if not used then user's current language is used

@return string Returns blank if default tab label not overridden

## getNameLabel()

Return the overriden "page name" label, or blank if not overridden


@param Language|null $language

@return string

## getIcon()

Return the icon name used by this template


@param bool $prefix Specify true if you want the icon prefix (icon- or fa-) to be included (default=false).

@return string Returns a font-awesome icon name

## getLanguages()

Get languages allowed for this template or null if language support not active.


@return PageArray|Languages|null Returns a PageArray of Language objects, or NULL if language support not active.

## getPageClass()

Get class name to use for Page objects using this template

Note that value can be different from the `$template->pageClass` property, since it is determined at runtime.
If it is different, then it is at least a class that extends the one defined by the pageClass property.


@param bool $withNamespace Returned class includes namespace? (default=true)

@return string Returned page class includes namespace

@since 3.0.152

## getTags()

Get tags array


@return array

@since 3.0.176

## hasTag()

Does this template have given tag?


@param string $tag

@return bool

@since 3.0.176

## addTag()

Add tag


@param string $tag

@return $this

@since 3.0.176

## removeTag()

Remove tag


@param string $tag

@return self

@since 3.0.176

## setIcon()

Set the icon to use with this template


@param string $icon Font-awesome icon name

@return $this

## editUrl()

URL to edit template settings (for administrator)

@param bool $http Full http/https URL?

@return string

@since 3.0.170
