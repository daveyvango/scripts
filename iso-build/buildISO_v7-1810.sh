#!/bin/sh

# Author: David VanGorder
# Use this script to create an ISO with a kickstart file.  It's useful
# when trying to automate or quickly deploy new VMs because default answers
# are fed to the installer right from the ISO.

# These two versions will change with any new release
MAJOR=7
RELEASE=1810
MIRROR=http://mirrors.mit.edu/centos/$MAJOR/isos/x86_64/
ISOFILE=CentOS-$MAJOR\-x86_64-Minimal-$RELEASE.iso
ISOKSFILE=CentOS-$MAJOR\-x86_64-Minimal-Kickstart-$RELEASE.iso
MIRROR2=http://www.gtlib.gatech.edu/pub/centos/7/isos/x86_64/
CHECKSUM=sha256sum.txt
TMPBOOTCFG=working/isolinux-tmp.cfg

echo "running cleanup first"
rm -rf working
rm -rf final
rm -rf src
rm -rf mount

echo "make somre room to work"
mkdir working
mkdir final
mkdir src
mkdir mount

echo "Installing genisoimage.x86_64 package for isoinfo command"
yum install genisoimage.x86_64

echo "Downloading $MIRROR/$ISOFILE"
curl -v $MIRROR/$ISOFILE -o src/$ISOFILE

echo "Mounting ISO to ./mount"
mount -o loop src/$ISOFILE mount
shopt -s dotglob
cp -aRf mount/* working/

SHACHECK=$(curl $MIRROR2/$CHECKSUM | grep $ISOFILE | awk '{print $1}')
echo "Checking sha sum on local $ISOFILE"
THISSHA=$(sha256sum src/$ISOFILE | awk '{print $1}')

echo "Local ISO SHA: $THISSHA"
echo "Cross ref SHA: $SHACHECK"
if [[ "$SHACHECK" == "$THISSHA" ]]; then
  echo "sha's from both mirrors match.  Looks legit"
else
  echo "ISO may be corrupt"
  exit 1
fi

echo "Let's see that Volume ID to use for our kickstart references"
VOLID=$(isoinfo -d -i src/$ISOFILE | grep "Volume id:" | sed 's/Volume id: //g')
VOLIDFORMATTED=$(isoinfo -d -i src/$ISOFILE | grep "Volume id:" | sed 's/Volume id: //g' | sed 's/ /\\x20/g')

BOOTMENUSTARTLINE=$(grep -n "menu title CentOS 7" working/isolinux/isolinux.cfg | awk -F: {'print $1}')
BOOTFILETAIL=$(($(wc -l working/isolinux/isolinux.cfg | awk '{print $1}') - $BOOTMENUSTARTLINE))

echo "Building boot config file isolinux.cfg"
head -$BOOTMENUSTARTLINE working/isolinux/isolinux.cfg > $TMPBOOTCFG
echo "#######################################" >> $TMPBOOTCFG
echo "label kickstart" >> $TMPBOOTCFG
echo "menu label ^Kickstart Installation of CentOS 7" >> $TMPBOOTCFG
echo "menu default" >> $TMPBOOTCFG
echo "kernel vmlinuz" >> $TMPBOOTCFG
echo "append initrd=initrd.img inst.stage2=hd:LABEL=$VOLIDFORMATTED inst.ks=cdrom:/anaconda-ks.cfg" >> $TMPBOOTCFG
echo "#######################################" >> $TMPBOOTCFG
# We re-assigned menu default to be kickstart
tail -$(($BOOTFILETAIL)) working/isolinux/isolinux.cfg | grep -v "menu default" >> $TMPBOOTCFG
echo "Copying temp boot config into final location"
cp -f $TMPBOOTCFG working/isolinux/isolinux.cfg
rm $TMPBOOTCFG
echo "Copying kickstart file"
cp -f anaconda-ks.cfg working/

echo "Making Kickstart ISO final/$ISOKSFILE"
echo "mkisofs -J -T -o final/$ISOKSFILE -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -R -m TRANS.TBL -graft-points -V \"$VOLID\" $(pwd)/working/"
mkisofs -J -T -o final/$ISOKSFILE -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -R -m TRANS.TBL -graft-points -V "$VOLID" $(pwd)/working/
umount mount/
