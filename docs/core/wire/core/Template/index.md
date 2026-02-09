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
Method: [roleTypeNames()](method-roletypenames.md)
Method: [getRoles()](method-getroles.md)
Method: [hasRole()](method-hasrole.md)
Method: [setRoles()](method-setroles.md)
Method: [addRole()](method-addrole.md)
Method: [removeRole()](method-removerole.md)
Method: [addPermissionByRole()](method-addpermissionbyrole.md)
Method: [revokePermissionByRole()](method-revokepermissionbyrole.md)
Method: [hasField()](method-hasfield.md)
Method: [setCacheExpirePages()](method-setcacheexpirepages.md)
Method: [urlSegments()](method-urlsegments.md)
Method: [isValidUrlSegmentStr()](method-isvalidurlsegmentstr.md)
Method: [setFlags()](method-setflags.md)
Method: [setFilename()](method-setfilename.md)
Method: [setFieldgroup()](method-setfieldgroup.md)
Method: [getNumPages()](method-getnumpages.md)
Method: [save()](method-save.md)
Method: [filename()](method-filename.md)
Method: [filenameExists()](method-filenameexists.md)
Method: [__toString()](method-__tostring.md)
Method: [parentTemplates()](method-parenttemplates.md)
Method: [childTemplates()](method-childtemplates.md)
Method: [allowNewPages()](method-allownewpages.md)
Method: [getParentPage()](method-getparentpage.md)
Method: [getParentPages()](method-getparentpages.md)
Method: [getLabel()](method-getlabel.md)
Method: [getTabLabel()](method-gettablabel.md)
Method: [getNameLabel()](method-getnamelabel.md)
Method: [getIcon()](method-geticon.md)
Method: [getLanguages()](method-getlanguages.md)
Method: [getPageClass()](method-getpageclass.md)
Method: [getTags()](method-gettags.md)
Method: [hasTag()](method-hastag.md)
Method: [addTag()](method-addtag.md)
Method: [removeTag()](method-removetag.md)
Method: [setIcon()](method-seticon.md)
Method: [editUrl()](method-editurl.md)

Constants:
Const: [flagSystem](const-flagsystem.md)
Const: [flagSystemOverride](const-flagsystemoverride.md)
Const: [cacheExpirePage](const-cacheexpirepage.md)
Const: [cacheExpireSite](const-cacheexpiresite.md)
Const: [cacheExpireParents](const-cacheexpireparents.md)
Const: [cacheExpireSpecific](const-cacheexpirespecific.md)
Const: [cacheExpireSelector](const-cacheexpireselector.md)
Const: [cacheExpireNone](const-cacheexpirenone.md)

Hookable methods
