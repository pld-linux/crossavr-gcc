#
# Conditional build:                                                          
%bcond_with	bootstrap	# for bootstraping                              
#                                             
Summary:	Cross AVR GNU binary utility development utilities - gcc
Summary(es.UTF-8):	Utilitarios para desarrollo de binarios de la GNU - AVR gcc
Summary(fr.UTF-8):	Utilitaires de développement binaire de GNU - AVR gcc
Summary(pl.UTF-8):	Skrośne narzędzia programistyczne GNU dla AVR - gcc
Summary(pt_BR.UTF-8):	Utilitários para desenvolvimento de binários da GNU - AVR gcc
Summary(tr.UTF-8):	GNU geliştirme araçları - AVR gcc
Name:		crossavr-gcc
Version:	4.3.5
Release:	1
Patch0:		crossavr-gcc-bug-11259-v3.patch
Patch1:		crossavr-gcc-bug-18145.patch
Patch2:		crossavr-gcc-bug-19636-24894-31644-31786.patch
Patch3:		crossavr-gcc-bug-33009.patch
Patch4:		crossavr-gcc-bug-34210-35508.patch
Patch5:		crossavr-gcc-bug-35013.patch
Patch6:		crossavr-gcc-builtins-v6.patch
Patch7:		crossavr-gcc-libgcc.patch
Patch8:		crossavr-gcc-libiberty-Makefile.in.patch
Patch9:		crossavr-gcc-new-devices.patch
Patch10:	crossavr-gcc-param-inline-call-cost.patch
Patch11:	crossavr-gcc-xmega.patch
Patch12:	crossavr-gcc-osmain.patch
Epoch:		1
License:	GPL
Group:		Development/Languages
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-%{version}.tar.bz2
# Source0-md5:	e588cfde3bf323f82918589b94f14a15
BuildRequires:	/bin/bash
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	crossavr-binutils
BuildRequires:	flex
BuildRequires:	gmp-devel >= 4.1
BuildRequires:	mpfr-devel >= 2.3.0
Requires:	crossavr-binutils >= 2.15.91.0.2
%{!?with_bootstrap:Requires:	crossavr-libc}
Requires:	gcc-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		avr
%define		arch		%{_prefix}/%{target}
%define		gccarch		%{_libdir}/gcc/%{target}
%define		gcclib		%{_libdir}/gcc/%{target}/%{version}
%define		_noautostrip	.*%{gcclib}.*/libgc.*\\.a

%description
This package contains a cross-gcc which allows the creation of
binaries to be run on Atmel AVR on other machines.

%description -l de.UTF-8
Dieses Paket enthält einen Cross-gcc, der es erlaubt, auf einem
anderem Rechner Code für Atmel AVR zu generieren.

%description -l pl.UTF-8
Ten pakiet zawiera skrośny gcc pozwalający na robienie na innych
maszynach binariów do uruchamiania na Atmel AVR.

%package c++
Summary:	C++ support for avr-gcc
Summary(pl.UTF-8):	Obsługa C++ dla avr-gcc
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description c++
This package adds C++ support to the GNU Compiler Collection for AVR.

%description c++ -l pl.UTF-8
Ten pakiet dodaje obsługę C++ do kompilatora gcc dla AVR.

%prep
%setup -q -n gcc-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p0
%patch12 -p0

%build
rm -rf obj-%{target}
install -d obj-%{target}
cd obj-%{target}

CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcflags}" \
TEXCONFIG=false \
../configure \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libdir} \
	--disable-shared \
	--disable-libssp \
	--enable-languages="c,c++" \
	--with-dwarf2 \
	--with-gnu-as \
	--with-gnu-ld \
	--with-system-zlib \
	--with-multilib \
	--without-x \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--target=%{target}

%{__make} CFLAGS_FOR_TARGET="-Os"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C obj-%{target} install \
	DESTDIR=$RPM_BUILD_ROOT

# move fixed includes to proper place
cp $RPM_BUILD_ROOT%{gcclib}/include-fixed/*.h $RPM_BUILD_ROOT%{gcclib}/include

# don't want it here
rm -f $RPM_BUILD_ROOT%{_libdir}/libiberty.a
rm -rf $RPM_BUILD_ROOT%{_infodir}
rm -f $RPM_BUILD_ROOT%{_mandir}/man7/fsf-funding.7
rm -f $RPM_BUILD_ROOT%{_mandir}/man7/gfdl.7
rm -f $RPM_BUILD_ROOT%{_mandir}/man7/gpl.7
rm -f $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/{gcc,cpplib}.mo
rm -rf $RPM_BUILD_ROOT%{gcclib}/include-fixed
rm -rf $RPM_BUILD_ROOT%{gcclib}/install-tools

%if 0%{!?debug:1}
# strip target libraries
%{target}-strip -g $RPM_BUILD_ROOT%{gcclib}{,/avr*}/libg*.a
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-gcc*
%attr(755,root,root) %{_bindir}/%{target}-cpp
%attr(755,root,root) %{_bindir}/%{target}-gcov
%dir %{gccarch}
%dir %{gcclib}
%attr(755,root,root) %{gcclib}/cc1
%attr(755,root,root) %{gcclib}/collect2
%{gcclib}/libg*.a
%{gcclib}/%{target}*
%dir %{gcclib}/include
%{gcclib}/include/*.h
%{_mandir}/man1/%{target}-cpp.1*
%{_mandir}/man1/%{target}-gcc.1*
%{_mandir}/man1/%{target}-gcov.1*

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-g++
%attr(755,root,root) %{_bindir}/%{target}-c++
%attr(755,root,root) %{gcclib}/cc1plus
%{_mandir}/man1/%{target}-g++.1*
