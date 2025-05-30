#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v13
# autospec commit: dc0ff31
#
Name     : rebootmgr
Version  : 2.4
Release  : 9
URL      : https://github.com/SUSE/rebootmgr/releases/download/v2.4/rebootmgr-2.4.tar.xz
Source0  : https://github.com/SUSE/rebootmgr/releases/download/v2.4/rebootmgr-2.4.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: rebootmgr-bin = %{version}-%{release}
Requires: rebootmgr-config = %{version}-%{release}
Requires: rebootmgr-data = %{version}-%{release}
Requires: rebootmgr-license = %{version}-%{release}
Requires: rebootmgr-man = %{version}-%{release}
Requires: rebootmgr-services = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(libeconf)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the rebootmgr package.
Group: Binaries
Requires: rebootmgr-data = %{version}-%{release}
Requires: rebootmgr-config = %{version}-%{release}
Requires: rebootmgr-license = %{version}-%{release}
Requires: rebootmgr-services = %{version}-%{release}

%description bin
bin components for the rebootmgr package.


%package config
Summary: config components for the rebootmgr package.
Group: Default

%description config
config components for the rebootmgr package.


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
Requires: systemd

%description services
services components for the rebootmgr package.


%prep
%setup -q -n rebootmgr-2.4
cd %{_builddir}/rebootmgr-2.4
pushd ..
cp -a rebootmgr-2.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720036213
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --libexecdir=/usr/lib
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --libexecdir=/usr/lib
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1720036213
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rebootmgr
cp %{_builddir}/rebootmgr-%{version}/COPYING %{buildroot}/usr/share/package-licenses/rebootmgr/3127907a7623734f830e8c69ccee03b693bf993e || :
cp %{_builddir}/rebootmgr-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/rebootmgr/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/rebootmgrctl
/V3/usr/bin/rebootmgrd
/usr/bin/rebootmgrctl
/usr/bin/rebootmgrd

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/soft-reboot-cleanup.conf

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.opensuse.RebootMgr.xml
/usr/share/dbus-1/system.d/org.opensuse.RebootMgr.conf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rebootmgr/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/rebootmgr/3127907a7623734f830e8c69ccee03b693bf993e

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
