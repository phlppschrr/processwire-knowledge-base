# ProcessWire core updates (2.5.14)

Source: https://processwire.com/blog/posts/processwire-core-updates-2.5.14/

## Sections


## ProcessWire core updates (2.5.14)

9 January 2015 by Ryan Cramer [ 11 Comments](/blog/posts/processwire-core-updates-2.5.14/#comments)


## A week of Multiples

New support for multiple copies of the same module, multiple templates for users, and multiple parents for users.


### Multiple copies of the same module

There have always been instances where some people want to modify a core module to suit a particular need. But they may have avoided it because their changes could get overwritten on the next core upgrade, making it kind of a hassle. This weeks update enables you to have multiple copies of the same module in your ProcessWire installation, along with the ability to easily switch between them. Here's how:

- Copy any individual module's directory from /wire/modules/ into /site/modules/.
- Make any changes to the module that you'd like. It is no longer necessary to rename the module file(s) or class name(s).
- In the admin, click Modules > Refresh.
- You'll get notices at the top indicating multiple copies of a module were found, along with a link you can click to change which one gets used.
- Click that link and select the copy of the module you want to use.

There's no requirement that the duplicate module(s) be from the core. You can also have multiple copies of the same non-core module in your /site/modules/ directory too, so long as they are under different directories. But I anticipate most use cases for this feature will be to make custom modifications to core modules. For example:

- Make custom versions of ProcessWire's comments modules /wire/modules/Fieldtype/FieldtypeComments/ => /site/modules/FieldtypeComments/
- Make a custom login form for the admin /wire/modules/Process/ProcessLogin/ => /site/modules/ProcessLogin
- Make a custom user profile editor /wire/modules/Process/ProcessProfile/ => /site/modules/ProcessProfile/

Those are just examples, but hopefully enough to demonstrate some of the potential.


### Multiple templates or parents for users

This week we also added the ability for users in ProcessWire to have alternate templates or even alternate parents. This could be particularly useful if you want to have different fields of information maintained for different types of users. Since you can now utilize different templates, you can likewise attach entirely different sets of fields to them. Though note that some fields are required for users (pass, roles, admin_theme).

You can also now have different parents for users. One situation where you might find this useful is if you want your 'user' pages to represent URLs on the front-end of your site. For instance, if you were running a publication with lots of authors, you might like for those 'author' users and their biography pages to be one and the same. That's just one example of many possible use cases.

Currently it's a little bit verbose to get this going, but I'll describe it below in case anyone is interested in giving it a try. When we get a little further along with it, we'll likely setup something more automated that can do most of these steps for you. But the system is fully functional if you'd like to give it a try. These instructions below describe setting up both an alternate template and an alternate parent for users. But if you just need an alternate template, you can do that even more easily.

**1. First, make sure you are running the latest copy of the dev branch (2.5.14). **Then enable advanced mode in your /site/config.php file:** **

```
$config->advanced = true;
```

**2. Next, edit the "user" template (Setup > Templates), and do the following:**

- On the Advanced tab, uncheck the box that says "Don't allow pages to change their template?".
- On the Advanced tab, uncheck the box that says "Don't allow pages to be moved?".
- On the System tab, uncheck the box that says "Disable Settings Tab?".
- Click Save.
- On the Advanced tab, check the box that says "Duplicate/clone this template".
- Click Save again.

**3. Create a new template that we will use for the alternate users parent page (Setup > Templates > Add New).**

- You might call this "members" or "alternate-users" or whatever you'd like.
- On the family tab under "Allowed templates for children" select "user_1" (which is the user template you cloned in the previous step). Don't worry, we'll rename "user_1" to something else later.
- Save.

**4. Create a new page using your new template you just created in step 3.**

- This will serve as the parent page for your alternate users.
- You might call this page /members/ or /alternate-users/ or whatever you'd like.
- It doesn't matter what you call it or where you place it.

**5. Edit the "user_1" template (Setup > Templates > user_1) that you created in step 2. **

- On the Family tab, for "Allowed templates for parents" select the template that you created in step 3.
- The name "user_1" is a bit boring, so go ahead and rename it (on the Advanced tab). For example, perhaps you'd call it "member-user" or something like that.
- Note the "id" number of this template (as seen at the end of the URL in your address bar when editing the template), as you'll need it in step 6.

**6. Edit your /site/config.php file and add the following: **

```
$config->userTemplateIDs = array(3, 111);
$config->usersPageIDs = array(29, 222);
```

- Replace 111 with the id of the new user template that you added.
- Replace 222 with the id of the new /alternate-users/ parent page that you added.

**7. Go to Access > Users > Add New, and add a new user. **You should now have a choice of template and parent.

**8. After creating a new user and assigning one or more roles, you should now be able to login with that user. **You can add as many other user templates or parents as you'd like using the same instructions.

**9. Undo what you did in step 1 by turning off advanced module** (this is not something you want to leave on).

Special thanks to Avoine for sponsoring this users system update and thanks to Antti Peisa for coming up with the idea.
