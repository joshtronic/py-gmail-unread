py-gmail-unread
===============

I wanted to inject the number of unread messages I have into my ZSH prompt and
obviously I needed a way to get the unread count. This script should be set up
in cron to run periodically as it's a bit too slow for inline calls. Depends on
the EMAIL environment variable as well as your password being loaded up into
the OSX keychain under the name "email" using your password as the account. The
script saves the unread count out to /tmp/GMAIL_UNREAD and then you can do
whatever the fuck you want do to with it, as long as it's not illegal.
