# Driving around a DDOS attack

Source: https://processwire.com/blog/posts/driving-around-a-ddos-attack/

## Sections


## Driving around a DDOS attack

7 February 2020 by Ryan Cramer [ 7 Comments](/blog/posts/driving-around-a-ddos-attack/#comments)

This week the plan was to work mostly on the ProcessWire core and a client project, but last Saturday we started getting hit with heavy traffic at processwire.com, and it soon became an apparent full blown DOS/DDOS attack.

It continued for half the week till things were back under control. If you visited our forums earlier this week, you likely noticed things responding slowly or even with an error. This post describes how we got it back under control and what was learned along the way.

Unlike most posts here, this one isn’t really about ProcessWire per se, as the target appeared to be our IP.Board forums rather than our software or main site. But had it been the main site or software, the strategies and solutions would have been the same.


### Target and traffic

I’m not sure anyone was intentionally targeting the ProcessWire site, and can’t think of any reason why they would want to. The traffic was instead targeting our IP.Board forums, which were serving more than a thousand (sometimes more than 1500) user sessions at a time. We’ve got a nice and fast AWS server (load balanced no less), but there are limits to how many requests you can deliver at a time, regardless of the server. This was really slowing things down and in some cases preventing the server from responding at all. No fault of IP.Board, which performs very nicely and securely, but this is just a lot of traffic.


### Aggressive bots from China

In comparing the traffic hitting the server with the traffic that Google Analytics was reporting, it became clear that much of this was not legitimate user traffic and instead was bot traffic. It appears to have been a widely distributed denial of service attack (DDOS), originating mostly from countless different ISPs throughout China.

There were seemingly millions of pageviews where there are usually thousands. And we were seeing more than 10,000 unique IPs hitting the server every hour multiple times, with such a broad range that it wasn’t feasible to block them at the IP level. Blocking at the regional level wasn’t a good option either, as we have a lot of legitimate users in China as well. Server load was often over 70.0 (and sometimes higher), when it is usually under 1.0.


### First try: upgrading and optimizing

Initially, rather than trying to block the traffic, we instead focused on optimizations to the server and IP.Board software. There are a lot of optimizations available in IP.Board that we hadn’t yet put to use, and so it seemed like the right time to do it. Here’s what we did:

- Installed memcached on the server and have configured IP.Board to use it.
- Enabled template disk caching and sidebar, header and footer block caching (5 mins).
- Page output seen by guests of the forums is now running on a 10 minute cache.
- Setup IP.Board to store and deliver all of its file assets from Amazon S3.
- Updated the forums to use ImageMagick rather than GD for all image features.

After doing all of that, it seemed to be helping. But apparently recognizing the recovery, it seemed like the bots started hitting it even harder. A few hours later, we were once again back where we started with the server regularly reaching a denial of service state.


### Second try: blocking everyone (except logged-in users)

In order to get things back under control, I hacked together a quick PHP script to make the forums only respond to already logged-in users. That quickly brought things under control. Despite all the bots continuing to hit the server, the overhead of the forums trying to serve them was gone. But this wasn’t a solution to leave in place for long, as most of our real forum traffic isn’t logged in, and we were denying that traffic (not to mention the legitimate bots like Googlebot).


### Looking for DDOS traffic patterns

Not really certain what to do next, I just sat there watching the live Apache log of requests, looking for patterns (good old `tail -f access_log`). I followed the URL paths that the apparent bots took and mirrored them in my browser. The bots spent a lot of time hitting URLs that most legitimate users rarely did—some for IP.Board features I never even knew about. More often than not, they were URLs that were apparently time consuming for IP.Board to render. Perfect targets for a denial of service attack.

Whether this particular attack was designed to exploit time consuming URLs in IP.Board, or whether the bots monitored render times before figuring out what to attack, I’m not certain. But they clearly had patterns, and those patterns weren’t consistent with those followed by our legitimate traffic. Once that became apparent, it was possible to more easily identify the bot requests and block a large percentage of them with custom PHP scripts.


### Third try: blocking identified patterns

After spending a lot of time looking at traffic patterns, we blocked traffic that matched those patterns. These were largely URLs with query strings focused on rarely used features. After about a day of delivering a combination of “403 Unauthorized”, “404 Not Found”, and “503 Service Not Available” http error codes to these bots (depending on the case and URL), they apparently gave up and moved on to other things. Though I’m guessing they will be back at some point. So rather than getting woken up in the middle of the night by server alarms, I thought I’d put in a permanent solution this time.


### Scripting a solution

The final solution ended up as a custom PHP script that runs before every IP.Board request, monitors the server load, and starts blocking URLs according to the load and session. It took about a day to build, but long term will hopefully prevent the issue from occurring again. Here’s how it works. If the server load is within normal limits, it doesn’t block anything. But if the server load starts to climb, then it starts blocking traffic from user agents that we saw on a lot of the bots (maybe 30-40% of them), like those mentioned in the next section. As load climbs higher, it starts looking closer at what is being accessed rather than just what is accessing it, and begins to block clients accessing URLs that fit a pattern.


### Problematic user agents

Following are strings found in user agents of what we found to be bots (or unknowing users) contributing to the DDOS attack. Most of these aren’t technically bot user agents, but rather user agent strings used by specific browsers; but browsers that aren’t commonly seen at processwire.com, except during an attack. So they don’t necessarily indicate illegitimate traffic, but my experience here was that we weren’t seeing any legitimate traffic from these user agents (though I could be wrong).

- LieBaoFast
- Mb2345Browser
- MicroMessenger
- MJ12bot
- Kinza
- QQBrowser and MQQBrowser
- among many others

Just blocking these user agent strings isn't a solution, but it's an easy thing to do and a good place to start.


### Bots that aren't bad, but are still pests

We also start blocking the bots that aren’t necessarily malicious, but that can be annoying pests that are doing SEO research for other companies. These are from (as far as I understand) companies using your server resources to research and index your content for other companies, rather than you or your users. These bots aren’t bringing any value to us, and sometimes they aren’t honoring our robots.txt crawl-delay, so if we’ve got any kind of server load, then these SEO bots are blocked too. To be clear, these bots aren’t responsible for any DDOS activity, but they certainly aren’t helping matters when load starts to climb, so it doesn't hurt to stop delivering traffic to them at that point. Some examples of these bots:

- AhrefsBot
- DotBot
- Semrushbot
- Seokicks
- Seoscanners
- and others


### The worst bots probably don't identify themselves

If the load continues to climb, even after blocking bot user agents (the easiest way), that’s not really a surprise — many bots do their best to look like a regular browser when it comes to the user agent string. These bots are coming from thousands of seemingly random different IP addresses, and we can’t identify and filter them by IP or by user agent. At this point we consider what URLs they are visiting and whether the pattern is consistent with real user traffic. There’s always potential for false positives here, so we don’t start blocking these until server load reaches a moderate level. But assuming that level is reached, we start delivering an error page to traffic that looks suspicious. The error page basically asks them to login if they want to continue with they are doing.


### High load situations

If server load reaches a higher load level, where things are starting to slow down, then at that point it shuts down many time-consuming [to render] IP.Board URLs. You can still browse the forums, topics and threads, and you can still sign-up or login, but many functions are disabled at that point. If load goes even higher, then most forum URLs are shut down for all but logged in users, and the forum asks you to either sign-up for an account or login in order to proceed. As soon as the load begins to drop, then the available features and URLs likewise begins to open up automatically.


### Conclusion and special thanks

This really isn’t what I wanted to work on this week, but the circumstances made it necessary. We can’t afford to have the support forums (and all that accompanies it) inaccessible for days on end. While it sounds like a big pain, it actually was pretty fun, and we sure managed to get some nice upgrades in the process. Not to mention, I learned a lot.

This post described my experience with the issue this week, but I wasn’t the only one that worked on it. A huge thanks to [Jan](https://www.tripsite.com/about/our-people/jan-van-den-hengel/) who collaborated with me on much of it during multiple days this week. He also added another node to our load balancer, installed memcache on the server, optimized PHP and MySQL settings, and was responsible for setting up and moving all of our static forum assets over to Amazon S3, among other things. [Pete](https://www.nifty.solutions/about-us/) (forum administrator) also helped out a lot this week, helping to look for bottlenecks and potential optimizations, and installing a forum upgrade, among other things. It was a real team effort.

By the way, ProcessWire 3.0.150 is now on the dev branch. Not much new was added in terms of commits *this* week (per the contents of this post), but for details on what’s been added, see ProcessWire Weekly [#298](https://weekly.pw/issue/298/) and [#299](https://weekly.pw/issue/299/) as well as [this post](https://processwire.com/talk/topic/23037-core-updates-%E2%80%93%C2%A0january-31-2020/) from last week in the forum. (It looks like the 300th issue of [ProcessWire Weekly](https://weekly.pw) is next!)
