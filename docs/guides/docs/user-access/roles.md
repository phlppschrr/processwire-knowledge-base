# Roles for access control in ProcessWire

Source: https://processwire.com/docs/user-access/roles/

## Summary

Roles are a way of grouping multiple users and assigning permissions to that group. They are the connection of both users and templates to permissions.

## Key Points

- Roles are a way of grouping multiple users and assigning permissions to that group. They are the connection of both users and templates to permissions.
- A user can have multiple roles, each with different permissions. Though for simple needs, it's common for a user to just have one non-guest role. However, you may assign as many roles to a user as you need, and the user will gain the access and permissions assigned to all of the roles they belong to.
- ProcessWire includes two permanent roles by default, though you may add as many roles as you like. The two roles included with every ProcessWire installation are:

## Sections


## Roles and users

A user can have multiple roles, each with different permissions. Though for simple needs, it's common for a user to just have one non-guest role. However, you may assign as many roles to a user as you need, and the user will gain the access and permissions assigned to all of the roles they belong to.


### Default roles

ProcessWire includes two permanent roles by default, though you may add as many roles as you like. The two roles included with every ProcessWire installation are:


### Custom roles

You can also add as many other roles as you want and selectively assign them to specific users. Each role can be assigned a unique set of permissions. Any given user can have multiple roles, and that user will inherit all permissions assigned to each of their roles. All users also inherit permissions assigned to the guest role.


### Checking if a user has a role

To check if a user has a specific role from the API side, use the $user->hasRole('roleName') method:


## Roles and permissions

Roles are essentially a group of permissions that can be assigned to users. Users gain all the permissions assigned to all of their roles.


### Assigning permissions to roles

Assigning permissions to roles is as simple as editing the role in your admin at Access > Roles > your_role. Once there, you will see a long list of checkboxes representing the various permissions that you can assign to the role. In some cases (like page-edit permission), clicking a permission reveals numerous other permissions below it. This indicates that such permissions are child permissions of the one you checked, and thus only apply if the role has the parent permission. Though you don't need to think about that, as the role editor adjusts the visibility of permissions according to what is applicable.


### Permissions with template context

Some permissions also support a template context. Meaning, the permission won't do much until the role having it is also assigned to a template. When this is the case, the role editor will show the permission along with a checkbox list of all templates where the permission can be assigned (which would be all templates that have access control enabled). If you don't see the template you need, you can enable access control for it (see roles and templates).


## Roles and templates

Roles are assigned to users, but they are also assigned to templates that have access control enabled. As stated earlier, this is how you limit access (view, edit, create, add, etc.) to certain pages, or groups of pages, in your site. By default, access control is not enabled for a template. When not enabled, pages using the template inherit access from the closest parent page that has access control enabled.
