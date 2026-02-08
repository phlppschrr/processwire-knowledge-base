# Permissions for access control in ProcessWire

Source: https://processwire.com/docs/user-access/permissions/

## Summary

Permissions represent a granular permission to access something or to perform some action. This page outlines permissions recognized by the core.

## Key Points

- Permissions represent a granular permission to access something or to perform some action. This page outlines permissions recognized by the core.
- Your system may also have permissions beyond those mentioned here. Any given module may install its own permissions, and likewise you may add your own custom permissions. This page only documents permissions commonly used by the core.
- Permissions in ProcessWire are objects of type Permission (a type of Page object). They each represent permission to access something, or to perform some action. Each permission has a name, and most are self describing. For instance, the page-edit permission is the foundation of providing page editing access.

## Sections


## Permissions overview


### What are permissions?

Permissions in ProcessWire are objects of type Permission (a type of Page object). They each represent permission to access something, or to perform some action. Each permission has a name, and most are self describing. For instance, the page-edit permission is the foundation of providing page editing access.


### How do you create a permission?

ProcessWire comes with several permissions that it recognizes (described on this page), but you can also create your own permissions and name them whatever you would like.


### How are permissions used from the API?

Whether from the core, a module, or the front-end of your site/application, most permission checking is performed from a single method call on the $user API variable:


## Default core permissions

These permissions come pre-installed with every copy of ProcessWire.


### page-add

Indicates whether a user has permission to add child pages to a given parent page. This is a symbolic runtime permission and thus does not exist in your list of permissions, but you may occasionally see reference to it. The permission becomes available only if a role already has page-edit permission, and "add" permission is specifically assigned to a role in the template access settings. Since this is a runtime-only permission, you should not attempt to create this permission.


### page-create

Indicates whether a user has permission to create pages of a certain type (template). This is a symbolic runtime permission and thus does not exist in your list of permissions, but you may occasionally see reference to it. The permission becomes available only if a role already has page-edit permission, and "create" permission is specifically assigned to a role in the template access settings. Since this is a runtime-only permission, you should not attempt to create this permission.


### page-delete

Enables a user to remove a page they have edit access to edit. For non-superusers, removing a page implies moving it to the trash. As a result, superusers can recover pages deleted by non-superusers. Also requires page-edit permission.
