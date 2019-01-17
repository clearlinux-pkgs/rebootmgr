#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rebootmgr
Version  : 0.18
Release  : 2
URL      : https://github.com/SUSE/rebootmgr/releases/download/v0.18/rebootmgr-0.18.tar.xz
Source0  : https://github.com/SUSE/rebootmgr/releases/download/v0.18/rebootmgr-0.18.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: rebootmgr-bin = %{version}-%{release}
Requires: rebootmgr-data = %{version}-%{release}
Requires: rebootmgr-license = %{version}-%{release}
Requires: rebootmgr-man = %{version}-%{release}
Requires: rebootmgr-services = %{version}-%{release}
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(json-c)

%description
No detailed description available

%package bin
Summary: bin components for the rebootmgr package.
Group: Binaries
Requires: rebootmgr-data = %{version}-%{release}
Requires: rebootmgr-license = %{version}-%{release}
Requires: rebootmgr-man = %{version}-%{release}
Requires: rebootmgr-services = %{version}-%{release}

%description bin
bin components for the rebootmgr package.


%package data
Summary: data components for the rebootmgr package.
Group: Data

%description data
data components for the rebootmgr package.


%package license
Summary: license components for the rebootmgr package.
Group: Default

%description license
license components for the rebootmgr package.


%package man
Summary: man components for the rebootmgr package.
Group: Default

%description man
man components for the rebootmgr package.


%package services
Summary: services components for the rebootmgr package.
Group: Systemd services

%description services
services components for the rebootmgr package.


%prep
%setup -q -n rebootmgr-0.18

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547744057
%configure --disable-static --libexecdir=/usr/lib
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1547744057
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rebootmgr
cp COPYING %{buildroot}/usr/share/package-licenses/rebootmgr/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/rebootmgr/COPYING.LIB
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rebootmgrctl
/usr/bin/rebootmgrd

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.opensuse.RebootMgr.xml
/usr/share/dbus-1/system.d/org.opensuse.RebootMgr.conf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rebootmgr/COPYING
/usr/share/package-licenses/rebootmgr/COPYING.LIB

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/rebootmgrctl.1
/usr/share/man/man5/rebootmgr.conf.5
/usr/share/man/man8/org.opensuse.RebootMgr.conf.8
/usr/share/man/man8/rebootmgr.service.8
/usr/share/man/man8/rebootmgrd.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/rebootmgr.service
