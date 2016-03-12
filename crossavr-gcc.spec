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
Version:	4.7.3
Release:	2
Epoch:		1
Patch0:		gnu_inline-mismatch.patch
# Patches 1xx are taken form Atmel official AVR8-GNU toolchain version 3.4.2
# http://distribute.atmel.no/tools/opensource/Atmel-AVR-Toolchain-3.4.2/avr/avr-patches.tar.gz
Patch100:	300-gcc-xmega-support.patch
Patch101:	301-gcc-tiny-support.patch
Patch102:	302-gcc-mlist-devices.patch
Patch103:	303-ata6289-architecture-correction.patch
Patch104:	400-gcc-public-devices-support.patch
Patch105:	401-gcc-non-public-devices-support.patch
Patch106:	402-gcc-atmega64_128_2564RFR2.patch
Patch107:	403-gcc-atmxts200.patch
Patch108:	501-gcc-avrtc579.patch
Patch109:	502-gcc-pr54796.patch
Patch110:	503-gcc-avrtc-513.patch
Patch111:	504-gcc-avrtc-610.patch
Patch112:	505-gcc-avrtc586.patch
License:	GPL
Group:		Development/Languages
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-%{version}.tar.bz2
# Source0-md5:	86f428a30379bdee0224e353ee2f999e
BuildRequires:	/bin/bash
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	crossavr-binutils >= 2.23.1
BuildRequires:	elfutils-devel >= 0.145-1
BuildRequires:	flex
BuildRequires:	gmp-devel >= 4.1
BuildRequires:	libmpc-devel
BuildRequires:	mpfr-devel >= 2.3.0
BuildRequires:	perl-tools-pod
BuildRequires:	ppl-devel
BuildRequires:	rpmbuild(macros) >= 1.565
BuildRequires:	sed >= 4.0
Requires:	crossavr-binutils >= 2.23.1
%{!?with_bootstrap:Requires:	crossavr-libc}
Requires:	gcc-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		avr
%define		arch		%{_prefix}/%{target}
%define		gccarch		%{_libdir}/gcc/%{target}
%define		gcclib		%{_libdir}/gcc/%{target}/%{version}
%define		_noautostrip	.*%{gcclib}.*/libgc.*\\.a

# functions with printf format attribute but with special parser and also
# receiving non constant format strings
%define		Werror_cflags	%{nil}

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
cd gcc/config/%{target} && %undos -f c,h && cd -
%patch0 -p1
%patch100 -p0
#patch101 -p0
%patch102 -p0
%patch103 -p0
#patch104 -p0
#patch105 -p0
#patch106 -p0
#patch107 -p0
#patch108 -p0
%patch109 -p0
#patch110 -p0
%patch111 -p0
#patch112 -p0

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
	--enable-c99 \
	--enable-languages="c,c++" \
	--enable-long-long \
	--enable-lto \
	--disable-shared \
	--disable-libssp \
	--with-dwarf2 \
	--with-gnu-as \
	--with-gnu-ld \
	--with-system-zlib \
	--with-multilib \
	--with-ppl \
	--disable-ppl-version-check \
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
rm -f $RPM_BUILD_ROOT%{gcclib}/liblto_plugin.la

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
%attr(755,root,root) %{gcclib}/lto-wrapper
%attr(755,root,root) %{gcclib}/lto1
%attr(755,root,root) %{gcclib}/liblto_plugin.so*
%{gcclib}/libg*.a
%{gcclib}/%{target}*
%{gcclib}/plugin
%dir %{gcclib}/tiny-stack
%{gcclib}/tiny-stack/*.a
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
