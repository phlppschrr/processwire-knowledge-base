# Including and bootstrapping ProcessWire

Source: https://processwire.com/docs/front-end/include/

## Summary

Use ProcessWire’s API in other PHP apps and shell scripts… It’s easy!

## Key Points

- Use ProcessWire’s API in other PHP apps and shell scripts… It’s easy!
- ProcessWire's API and data can be used from other PHP scripts, including command line PHP scripts. This is a simple matter of just including ProcessWire's ./index.php file from any other PHP script.
- It doesn't matter if your intended use is HTTP or command line... ProcessWire will auto-detect the state from which it was included.

## Sections


### Creating a ProcessWire command-line script

Here is an example of a command line shell script called sitemap.sh that outputs all pages in the site in an indented site map. We do this with a very small amount of code by creating a function called listPage that we use recursively:


### Including ProcessWire from another PHP script

ProcessWire can be included from any other PHP script in the same manner it was included from the command line script above. Just include ProcessWire's root ./index.php file, and you have full access to it's API.
