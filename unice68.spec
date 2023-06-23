#
# Conditional build:
%bcond_without	static_libs	# static libraries
#
Summary:	Ice packer/depacker program and library
Summary(pl.UTF-8):	Program i biblioteka do pakowania/rozpakowywania archiwów Ice
Name:		unice68
Version:	2.0.0.690
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	https://downloads.sourceforge.net/sc68/%{name}-%{version}.tar.xz
# Source0-md5:	c7e28783047f4de1b40311814b074968
URL:		http://sc68.atari.org/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unice68 project is a C library and a command line program for packing
and depacking !Ice compressed files, known from Atari ST.

%description -l pl.UTF-8
Projekt unice68 to biblioteka C i program linii poleceń do pakowania
i rozpakowywania plików skompresowanych w formacie !Ice, znanym z
Atari ST.

%package devel
Summary:	Header files for unice68 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki unice68
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for unice68 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki unice68.

%package static
Summary:	Static unice68 library
Summary(pl.UTF-8):	Statyczna biblioteka unice68
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static unice68 library.

%description static -l pl.UTF-8
Statyczna biblioteka unice68.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libunice68.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/unice68
%attr(755,root,root) %{_libdir}/libunice68.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/unice68.h
%{_pkgconfigdir}/unice68.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libunice68.a
%endif
