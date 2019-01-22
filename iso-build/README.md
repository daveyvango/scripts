# iso-build
ISO build scripts, kickstart files, etc.

**buildISO.sh** - used to build a kickstart ISO of CentOS 7.  This is a scripted version of the manual steps laid out in [Red Hat Installation Guide 4.2 Automatic Installation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/installation_guide/sect-simple-install-kickstart)

1. Update "rootpw" line anaconda-ks.cfg to set the **root** password
2. Run the script: `sudo ./buildISO_v7-1810.sh`.  Root required because of `yum` and `mount` usage.
3. Copy the resulting ISO into vCenter for using in server builds
4. Remove the password from `anacond-ks.cfg` (*hint*: just use `git checkout -- anaconda-ks.cfg`)
