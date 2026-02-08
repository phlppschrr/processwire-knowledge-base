# Roles for ProcessWire access control (RBAC)

Source: https://processwire.com/docs/user-access/roles/

# Roles for access control in ProcessWire 

Roles are a way of grouping multiple users and assigning permissions to that group. They are the connection of both users and templates to permissions.
- [Roles and users](#roles-and-users)
  - [Default roles](#default-roles)
  - [Custom roles](#custom-roles)
  - [Checking if a user has a role](#checking-if-a-user-has-a-role)

- [Roles and permissions](#roles-and-permissions)
  - [Assigning permissions to roles](#assigning-permissions-to-roles)
  - [Permissions with template context](#permissions-with-template-context)

- [Roles and templates](#roles-and-templates)
  - [Enabling template access control](#enabling-template-access-control)

---
[](#)

## Roles and users

A user can have multiple roles, each with different permissions. Though for simple needs, it's common for a user to just have one non-guest role. However, you may assign as many roles to a user as you need, and the user will gain the access and permissions assigned to all of the roles they belong to.[](#)

### Default roles

ProcessWire includes two permanent roles by default, though you may add as many roles as you like. The two roles included with every ProcessWire installation are:
- 

**guest**
The guest role is automatically given to all anonymous site users. You should not give this role any access other than page-view permission.
- 

**superuser**
The superuser role has all-inclusive access to the site without limitation. This role should only be given to the most trusted users that operate the site. Superuser has all permissions regardless of what you assign with the superuser role.

[](#)

### Custom roles

You can also add as many other roles as you want and selectively assign them to specific users. Each role can be assigned a unique set of permissions. Any given user can have multiple roles, and that user will inherit all permissions assigned to each of their roles. All users also inherit permissions assigned to the guest role.[](#)

### Checking if a user has a role

To check if a user has a specific role from the API side, use the [$user->hasRole('roleName')](/api/ref/user/has-role/) method:

```
if($user->hasRole('editor')) {
  // user has the editor role, display editor_notes field
  echo "<h3>Editor notes</h3>" . $page->editor_notes;
}
```

---
[](#)

## Roles and permissions

Roles are essentially a group of [permissions](/docs/user-access/permissions/) that can be assigned to users. Users gain all the permissions assigned to all of their roles.

In some cases a permission doesn't do much until the role containing the permission is also assigned to a template (the context). A good example of this is the [page-edit](/docs/user-access/permissions/#page-edit) permission. If it were as simple as giving a role page-edit permission, then they would be able to edit any page anywhere in the site, which is usually not what you want. Instead, a permission like page-edit also requires a context, and templates (as used by pages) are that context. So a user might have a general page-edit permission via a role assigned to them, but they won't be able to actually edit any pages until a template also has that same role selected. This is how you can enable granular access (edit, view, create, add, delete, etc.) to some pages and not others.[](#)

### Assigning permissions to roles

Assigning permissions to roles is as simple as editing the role in your admin at Access > Roles > your_role. Once there, you will see a long list of checkboxes representing the various permissions that you can assign to the role. In some cases (like page-edit permission), clicking a permission reveals numerous other permissions below it. This indicates that such permissions are child permissions of the one you checked, and thus only apply if the role has the parent permission. Though you don't need to think about that, as the role editor adjusts the visibility of permissions according to what is applicable.[](#)

### Permissions with template context

Some permissions also support a template context. Meaning, the permission won't do much until the role having it is also assigned to a template. When this is the case, the role editor will show the permission along with a checkbox list of all templates where the permission can be assigned (which would be all templates that have access control enabled). If you don't see the template you need, you can enable access control for it (see [roles and templates](#roles-and-templates)).

Editing permissions with template context in the role editor is convenient because it enables you to edit all permissions for the role, in the context of those access controlled templates, right on a single screen. You can also edit template/role assignments from the template editor (Setup > Template > your_template > Access), but in this case you are editing access for *all* roles on *one* template, rather than *all* templates on *one* role. It does not matter which one you use, but which is more convenient will depend on whether you've got more templates or more roles.

---
[](#)

## Roles and templates

Roles are assigned to users, but they are also assigned to templates that have access control enabled. As stated earlier, this is how you limit access (view, edit, create, add, etc.) to certain pages, or groups of pages, in your site. By default, access control is not enabled for a template. When not enabled, pages using the template inherit access from the closest parent page that has access control enabled.[](#)

### Enabling template access control

You can enable access control for a template from the template editor *Access* tab (Setup > Templates > your_template > Access). From here you can dictate what roles are allowed to view, edit, create, add new pages, and more. Any role can be assigned for view permission, but only roles that have at least [page-edit permission](/docs/user-access/permissions/#page-edit) are assignable for edit/add/create access in these template access settings. Once a template has access control enabled, these can also be assigned in the role editor—see the section above on [permissions with template context](#permissions-with-template-context).
- [Access control](/docs/user-access/)
- [Roles](/docs/user-access/roles/)
- [Permissions](/docs/user-access/permissions/)

- [Docs](/docs/)
- [API reference](/api/ref/)
- [Getting started](/docs/start/)
- [Front-end](/docs/front-end/)
- [Tutorials](/docs/tutorials/)
- [Selectors](/docs/selectors/)
- [Modules & hooks](/docs/modules/)
- [Fields, types, input](/docs/fields/)
- [Access control](/docs/user-access/)
- [Security](/docs/security/)
- [Multi-language](/docs/multi-language-support/)
- [More topics](/docs/more/)
