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


### Potential permissions for writable directories and files

Permissions below are organized in order of most secure to least secure. If Apache runs as you, chances are you can use the most secure permission options. When possible, inquire with your web host as to which permissions are best to use in your environment.


### Potential permissions for writable directories

700 [rwx------] writable by owner, readable by owner (most secure, if it works) 750 [rwxr-x---] writable by owner, readable by owner and group 755 [rwxr-xr-x] writable by owner, readable by all (details) 770 [rwxrwx---] writable by owner and group, readable by owner and group 775 [rwxrwxr-x] writable by owner and group, readable by all 777 [rwxrwxrwx] writable by all, readable by all (not secure, details)


### Potential permissions for writable files

600 [rw-------] writable by owner, readable by owner (most secure, if it works) 640 [rw-r-----] writable by owner, readable by group 644 [rw-r--r--] writable by owner, readable by all (details) 660 [rw-rw----] writable by owner and group, readable by owner and group 664 [rw-rw-r--] writable by owner and group, readable by all 666 [rw-rw-rw-] writable by all, readable by all (not secure, details)


### Is "writable by group" safe in a shared hosting environment?

It depends who group implies. If group is the same as owner then it's just as safe as without any group permissions, though also not much point to it. But if group is instead the same group that other users on the system belong to, then it's not any safer than "writable by all".


### Is "writable by all" safe in a dedicated hosting environment?

If there aren't other users/accounts on the same server, then potentially yes, for the moment anyway. If there's nobody else on the server to consider, then "all" isn't anyone except you and your site. But we still recommend avoiding "writable by all" when possible because of what lies in the future. We simply don't know. Perhaps more accounts will be added to the server, perhaps the site will move to another server at some point, or perhaps some other part of the server or will get exploited. If you can avoid "writable by all" in your dedicated environment–even if it isn't technically necessary–you are buying some potential insurance for the future… though hopefully insurance that you'll never need.


### Permission 755 for directories and 644 for files

If you see the installer identify these permissions (755 and 644), they are a good place to start. Though we recommend you confirm with your host, as well as check if the permissions can be locked down further. For instance your host may recommend 700 for directories and 600 for files, which would make files writable only to you and readable only to you (which is great, if it will work). Or they may recommend 750 and 640 which would make files writable and readable to you, and readable to a group. Alternatively, your host may recommend something entirely different, so take the time to find out what's right for your environment. In the end, if 755 and 644 work for your environment, further potential tweaks could worthwhile but may not be urgent.


### Worst case: 777 for directories and 666 for files

If the installer populates permissions 777 for directories and 666 for files that means that it was unable to determine what the writable permissions should be, and 777/666 are the only permissions that we know for certain will work. However, these permissions are a worst-case scenario in terms of security, and you should not consider them unless in a dedicated environment. Those permissions effectively make the files readable and writable to all accounts on the server. That's not necessarily a problem if you are the only account on the server, but potentially a big problem if there are others. Particularly if you are in a shared environment, take the time to consult with your web host on what permissions to use for Apache-writable directories and files.
