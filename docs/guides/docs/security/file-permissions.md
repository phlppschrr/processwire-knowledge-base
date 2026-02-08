# Securing file permissions

Source: https://processwire.com/docs/security/file-permissions/

## Summary

Getting your file permissions right is one of the most important factors in maintaining the security of your ProcessWire installation, particularly in non-dedicated/shared environments.

## Key Points

- Getting your file permissions right is one of the most important factors in maintaining the security of your ProcessWire installation, particularly in non-dedicated/shared environments.
- Yet it's also one of the most difficult to get right, because there is no single correct answer that applies across all hosting environments. It is most definitely worth taking the time to make sure your file permissions are optimal for your environment.
- One of the first questions in determining what file permissions should be is whether Apache runs as your user account, or whether it runs as the same user for all accounts (like "nobody", "www" or "apache", for example). This is a question for your web host, as it depends entirely on their server configuration. Though if you want to do it yourself, there are a couple things you can do to make a reasonable determination yourself.

## Sections


## Securing writable directories and files

When you install ProcessWire, it performs a check to see if the install.php file is writable. If it is, then there's a good chance (though not a guarantee) that Apache runs as your user account. If it detects this, it will recommend the 755 permission for writable directories and 644 permission for writable files, as a starting point. This translates to directories and files that are writable only to you, but readable to everyone else.

If the installer populates 777 and 666 permissions, this translates to directories and files that are readable and writable to everyone, which is not a good scenario in shared environments. But without knowing more about the hosting environment, they may be the only permissions that we know for certain will enable ProcessWire to run. In either case, please read on for more details. In most cases you can further lock down these permissions with a little more information.


### Potential permissions for writable directories and files

Permissions below are organized in order of most secure to least secure. If Apache runs as you, chances are you can use the most secure permission options. When possible, inquire with your web host as to which permissions are best to use in your environment.


### Potential permissions for writable directories

700 [rwx------] writable by owner, readable by owner (most secure, if it works) 750 [rwxr-x---] writable by owner, readable by owner and group 755 [rwxr-xr-x] writable by owner, readable by all (details) 770 [rwxrwx---] writable by owner and group, readable by owner and group 775 [rwxrwxr-x] writable by owner and group, readable by all 777 [rwxrwxrwx] writable by all, readable by all (not secure, details)


### Potential permissions for writable files

600 [rw-------] writable by owner, readable by owner (most secure, if it works) 640 [rw-r-----] writable by owner, readable by group 644 [rw-r--r--] writable by owner, readable by all (details) 660 [rw-rw----] writable by owner and group, readable by owner and group 664 [rw-rw-r--] writable by owner and group, readable by all 666 [rw-rw-rw-] writable by all, readable by all (not secure, details)


### Is "writable by group" safe in a shared hosting environment?

It depends who group implies. If group is the same as owner then it's just as safe as without any group permissions, though also not much point to it. But if group is instead the same group that other users on the system belong to, then it's not any safer than "writable by all".

A common situation in web hosting is for group to be the same group belonged to by Apache (but not by other users), so that one could use a 770 for directories or 660 for files to give write permission to Apache without giving it to other users on the system.

There's still a significant danger here though: other users on the system may still be able to create a PHP (or other language) script that runs as Apache, and thereby has all the group permissions that Apache does. In such a case, that user can still gain access to your files, if they are motivated enough and know what they are doing. That's assuming the hosting environment permits it. But last we tested, many still do. For these reasons, it's important to consult with your web host on what are the ideal permissions for your environment. For these same reasons, we recommend hosting in a dedicated environment whenever possible (regardless of CMS).


### Is "writable by all" safe in a dedicated hosting environment?

If there aren't other users/accounts on the same server, then potentially yes, for the moment anyway. If there's nobody else on the server to consider, then "all" isn't anyone except you and your site. But we still recommend avoiding "writable by all" when possible because of what lies in the future. We simply don't know. Perhaps more accounts will be added to the server, perhaps the site will move to another server at some point, or perhaps some other part of the server or will get exploited. If you can avoid "writable by all" in your dedicated environment–even if it isn't technically necessary–you are buying some potential insurance for the future… though hopefully insurance that you'll never need.


### Permission 755 for directories and 644 for files

If you see the installer identify these permissions (755 and 644), they are a good place to start. Though we recommend you confirm with your host, as well as check if the permissions can be locked down further. For instance your host may recommend 700 for directories and 600 for files, which would make files writable only to you and readable only to you (which is great, if it will work). Or they may recommend 750 and 640 which would make files writable and readable to you, and readable to a group. Alternatively, your host may recommend something entirely different, so take the time to find out what's right for your environment. In the end, if 755 and 644 work for your environment, further potential tweaks could worthwhile but may not be urgent.


### Worst case: 777 for directories and 666 for files

If the installer populates permissions 777 for directories and 666 for files that means that it was unable to determine what the writable permissions should be, and 777/666 are the only permissions that we know for certain will work. However, these permissions are a worst-case scenario in terms of security, and you should not consider them unless in a dedicated environment. Those permissions effectively make the files readable and writable to all accounts on the server. That's not necessarily a problem if you are the only account on the server, but potentially a big problem if there are others. Particularly if you are in a shared environment, take the time to consult with your web host on what permissions to use for Apache-writable directories and files.


### Where to modify ProcessWire's writable directory/file settings

Your /site/config.php file contains two settings that control the writable directory and file settings:

```
// permission for directories created by ProcessWire
$config->chmodDir = '0755';
```

```
// permission for files created by ProcessWire
$config->chmodFile = '0644';
```

Note that these permissions should be provided like above, as a string preceded with a 0. In other contexts (like with chmod, or perhaps your FTP client) you typically would omit the leading 0 that you see above.

When you change the values of these two $config properties, it only affects directories and files created from that point forward. Any existing directories and files continue to have the existing permissions they already had. As a result, any time you make changes to these settings, you should also perform a recursive change to the permissions of all files in ProcessWire's writable directories. This includes /site/assets/ and everything within it, as well as /site/modules/ and everything in it (if you want to have a writable modules file system). Read the next section for details on how to do this.


### How to change permissions of existing files

If you have SSH access to your account, a recursive permission can be performed with chmod. If you have FTP access to your account, most FTP clients support recursive permission changes, but usage will vary. We'll cover use of chmod here, since usage will always be the same. The following examples all assume you are executing chmod from the root installation of your ProcessWire site (the same directory where index.php is located).


### Change the permission of just one file

Replace /site/config.php with name of file you want to change, and replace 600 with permission you want to use.

```

chmod 600 site/config.php
```


### Change the permission of just one directory

Replace site/assets with the name of the directory you want to change, and replace 755 with the permission you want to use.

```

chmod 755 site/assets
```

The above would only change the permission for the site/assets directory, and not any directories within it. To change the permission of the site/assets directory and all directories within it recursively, see below.


### Change the permission of ALL directories (recursively)

Replace site/assets with the name of the starting directory you want to change, and replace 755 with the permission you want to use.

```

find site/assets -type d -exec chmod 755 {} \;
```


### Change the permission of ALL files (recursively)

Replace site/assets/ with the name of the directory where files are located, and replace 644 with the permission you want to use.

```

find site/assets/ -type f -exec chmod 644 {} \;
```


## Securing your /site/config.php file

In a typical ProcessWire installation, your /site/config.php file is the one file that you need to make sure is not readable to any other user on the system (other than yourself and Apache). This file contains your database login and password information (and potentially other confidential information), so it's particularly important to lock this one down.

In addition, the /site/config.php file needs to be writable by the installer (so it can record your settings), but it doesn't need to be writable afterwards. So it's a good idea to make adjusting the permissions of this file part of your regular installation process.

As with other file permission settings, your /site/config.php permissions are primarily a consideration if you are in a shared (non-dedicated) hosting environment. In a dedicated environment, there aren't other potential users to worry about.

While you can consult with your web host on what the best permissions for this file might be, you can also test things out yourself fairly easily. You can experiment with most restrictive permissions to least restrictive, until you find one that works.

To change the permissions of this file, use chmod (if connected to your account via SSH) or use the permission settings in your FTP client. Usage will vary by FTP client. If using chmod from SSH, usage is as follows (replace "400" with whatever permission you want to apply):

```

chmod 400 site/config.php
```


### Potential permissions for /site/config.php

Below are potential settings, ordered from most secure to least secure. Find the setting that works with your server, that balances your needs and security the best.

How can you tell if the setting works with your server? Simply change the permission and load your site in a web browser. If you get your site, the setting worked. If you get an error message, 404 or nothing at all, the setting didn't work. Thats all there is to it.

Recommend settings if you don't need write access: 400 [r--------] readable by owner (most secure, if it works) 440 [r--r-----] readable by owner and group (if 400 doesn't work)

Recommended settings if you need write access: 600 [rw-------] readable and writable by owner (most secure, if it works) 640 [rw-r-----] readable and writable by owner, readable to group 660 [rw-rw----] readable and writable by owner and group

Not recommended unless nothing else will work:* 444 [r--r--r--] readable by all 644 [rw-r--r--] readable by all, writable to owner 664 [rw-rw-r--] readable by all, writable to owner and group

* Should be okay in a dedicated environment.


### Determining what user apache runs as

This is a question for your web host, but if you are the DIY type, there's a way to find out yourself. Paste the following into a test.php file on your server and then load it in your browser:

```php
<?php echo exec('whoami');
```

```php
<?php echo file_put_contents("test.txt", "test");
```

If you get a positive number number and no error message then Apache is most likely running as you–read item #1 above. If you get the number 0 and/or an error message, Apache is most likely not running as you–read item #2 above.

Remember to delete your test.php file (and test.txt file, if applicable).


### Should /site/modules/ be writable?

When you install ProcessWire, if it detects that your file system is writable by default (indicating that Apache is likely running as you), then you may wish to likewise maintain a writable /site/modules/ directory. This enables you to upload, pull, install, update and delete modules from your admin, which is a nice convenience.

However, that convenience comes with a compromise. Writable directories with executable PHP files is making a compromise in terms of security. If a superuser account on your system is ever hacked into, you've got problems.

If your environment is non-dedicated and you have to supply any "all" (or even "group") write permissions, then don't have a writable /site/modules/ directory. You are safer just installing modules by FTP in this environment.
