Summary:	OpenCORE Framework implementation of Adaptive Multi Rate Narrowband and Wideband speech codec
Name:		opencore-amr
Version:	0.1.3
Release:	1
License:	Apache v2.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/opencore-amr/%{name}-%{version}.tar.gz
# Source0-md5:	09d2c5dfb43a9f6e9fec8b1ae678e725
URL:		http://opencore-amr.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library contains an implementation of the 3GPP TS 26.073
specification for the Adaptive Multi Rate (AMR) speech codec and an
implementation for the 3GPP TS 26.173 specification for the Adaptive
Multi-Rate - Wideband (AMR-WB) speech decoder. The implementation is
derived from the OpenCORE framework, part of the Google Android
project.

%package devel
Summary:	Header files for opencore-amr library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for opencore-amr library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %ghost %{_libdir}/libopencore-*.so.?
%attr(755,root,root) %{_libdir}/libopencore-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopencore-*.so
%{_libdir}/libopencore-*.la
%{_includedir}/opencore-*
%{_pkgconfigdir}/opencore-*.pc

