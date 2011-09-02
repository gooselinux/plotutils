
Name:      plotutils
Version:   2.5
Release:   7.1%{?dist}
Summary:   GNU vector and raster graphics utilities and libraries

Group:     Applications/Productivity
License:   GPLv2+
URL:       http://www.gnu.org/software/plotutils/
Source0:   ftp://ftp.gnu.org/gnu/plotutils/plotutils-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:   flex
BuildRequires:   libpng-devel
BuildRequires:   xorg-x11-proto-devel
BuildRequires:   libX11-devel
BuildRequires:   libXaw-devel
BuildRequires:   libXt-devel
BuildRequires:   libXext-devel

Requires(post):  /sbin/install-info
Requires(post):  /sbin/ldconfig
Requires(preun): /sbin/install-info

%description
The GNU plotutils package contains software for both programmers and
technical users. Its centerpiece is libplot, a powerful C/C++ function
library for exporting 2-D vector graphics in many file formats, both
vector and raster. It can also do vector graphics animations. Besides
libplot, the package contains command-line programs for plotting
scientific data. Many of them use libplot to export graphics


%package devel
Summary:     Headers for developing programs that will use %{name}
Group:       Development/Libraries
Requires:    %{name} = %{version}-%{release}


%description devel
This package contains the header files needed for developing %{name}
applications


%prep
%setup -q
cp -f lib/fontlist.c graph/
cp -f lib/fontlist.c plot/
cp -f lib/fontlist.c pic2plot/
cp -f lib/fontlist.c plotfont/
cp -f lib/fontlist.c tek2plot/


%build
%configure --disable-static --enable-libplotter --enable-libxmi --enable-ps-fonts-in-pcl
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT docs-to-include
make install DESTDIR=$RPM_BUILD_ROOT
mkdir docs-to-include
mv ${RPM_BUILD_ROOT}%{_datadir}/ode docs-to-include
mv ${RPM_BUILD_ROOT}%{_datadir}/pic2plot docs-to-include
mv ${RPM_BUILD_ROOT}%{_datadir}/libplot docs-to-include
mv ${RPM_BUILD_ROOT}%{_datadir}/tek2plot docs-to-include
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT%{_infodir}/dir


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/install-info %{_infodir}/libxmi.info %{_infodir}/dir || :
/sbin/install-info %{_infodir}/plotutils.info %{_infodir}/dir || :
/sbin/ldconfig


%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete %{_infodir}/libxmi.info %{_infodir}/dir || :
    /sbin/install-info --delete %{_infodir}/plotutils.info %{_infodir}/dir || :
fi


%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, -)
%doc AUTHORS COMPAT COPYING NEWS THANKS README PROBLEMS KNOWN_BUGS
%doc docs-to-include/*
%{_bindir}/graph
%{_bindir}/ode
%{_bindir}/double
%{_bindir}/plot
%{_bindir}/pic2plot
%{_bindir}/plotfont
%{_bindir}/spline
%{_bindir}/tek2plot
%{_libdir}/*.so.*
%{_mandir}/man1/*
%{_infodir}/*.info*


%files devel
%defattr(-, root, root, -)
%doc TODO
%{_includedir}/*.h
%{_libdir}/*.so


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.5-7.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.5-5
- Autorebuild for GCC 4.3

* Mon Aug 20 2007 Denis Leroy <denis@poolshark.org> - 2.5-4
- License tag update

* Mon Aug 28 2006 Denis Leroy <denis@poolshark.org> - 2.5-3
- FE6 Rebuild

* Thu Aug 10 2006 Denis Leroy <denis@poolshark.org> - 2.5-2
- Some reformatting, added ldconfig Req

* Wed Aug  9 2006 Denis Leroy <denis@poolshark.org> - 2.5-1
- Initial version

