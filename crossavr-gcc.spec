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
Version:	4.5.3
Release:	1
Epoch:		1
# Patches 1xx are taken form Atmel official AVR8-GNU toolchain version 3.3.1.481.
Patch100:	200-gcc-4.5.1-libiberty-Makefile.in.patch
Patch101:	300-gcc-4.5.1-fixedpoint-3-4-2010.patch
Patch102:	301-gcc-4.5.1-xmega-v14.patch
Patch103:	302-gcc-4.5.1-avrtiny10.patch
Patch104:	303-gcc-4.5.1-osmain.patch
Patch105:	304-gcc-4.5.1-builtins-v6.patch
Patch106:	305-gcc-4.5.1-avrtiny10-non-fixedpoint.patch
Patch107:	306-gcc-4.5.1-option-list-devices.patch
Patch108:	400-gcc-4.5.1-new-devices.patch
Patch109:	401-gcc-4.5.1-atmega32_5_50_90_pa.patch
Patch110:	402-gcc-4.5.1-attiny1634.patch
Patch111:	403-gcc-4.5.1-atmega48pa.patch
Patch112:	404-gcc-4.5.1-atxmega_16_32_a4u.patch
Patch113:	405-gcc-4.5.1-atxmega64_128_192_256a3u.patch
Patch114:	406-gcc-4.5.1-atmegarfr2_a2.patch
Patch115:	407-gcc-4.5.1-atmega165pa.patch
Patch116:	408-gcc-4.5.1-atxmega384c3.patch
Patch117:	409-gcc-4.5.1-attiny80.patch
Patch118:	410-gcc-4.5.1-atxmega128a4u.patch
Patch119:	411-gcc-4.5.1-atxmega64d4.patch
Patch120:	412-gcc-4.5.1-atmega164pa_168pa_32a_64a.patch
Patch121:	413-gcc-4.5.1-atxmega32x1.patch
Patch122:	414-gcc-4.5.1-atxmega64_128_b3.patch
Patch123:	415-gcc-4.5.1-atxmega64b1.patch
Patch124:	416-gcc-4.5.1-atmega_8a_128a_1284.patch
Patch125:	417-gcc-4.5.1-atxmega64a4u.patch
Patch126:	418-gcc-4.5.1-atxmega128d4.patch
Patch127:	419-gcc-4.5.1-atmxt336s.patch
Patch128:	420-gcc-4.5.1-atxmega16c4_32c4_128c3_256c3.patch
Patch129:	421-gcc-4.5.1-atxmega384d3.patch
Patch130:	422-gcc-4.5.1-atmega48hvf.patch
Patch131:	423-gcc-4.5.1-atmega26hvg.patch
Patch132:	424-gcc-4.5.1-atmxt224_224e.patch
Patch133:	424-gcc-4.5.1-atxmega192c3.patch
Patch134:	500-gcc-4.5.1-bug13473.patch
Patch135:	501-gcc-4.5.1-bug13579.patch
Patch136:	502-gcc-4.5.1-bug-18145-v4.patch
Patch137:	503-gcc-4.5.1-avrtiny10-bug-12510.patch
Patch138:	504-gcc-4.5.1-bug12915.patch
Patch139:	505-gcc-4.5.1-bug13932.patch
Patch140:	506-gcc-4.5.1-bug13789.patch
Patch141:	507-gcc-4.5.1-bug14415.patch
License:	GPL
Group:		Development/Languages
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-%{version}.tar.bz2
# Source0-md5:	8e0b5c12212e185f3e4383106bfa9cc6
BuildRequires:	/bin/bash
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	crossavr-binutils
BuildRequires:	elfutils-devel >= 0.145-1
BuildRequires:	flex
BuildRequires:	gmp-devel >= 4.1
BuildRequires:	libmpc-devel
BuildRequires:	mpfr-devel >= 2.3.0
BuildRequires:	perl-tools-pod
BuildRequires:	rpmbuild(macros) >= 1.565
BuildRequires:	sed >= 4.0
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
cd gcc/config/%{target} && %undos -f c,h && cd -
%patch100 -p0
%patch101 -p0
%patch102 -p0
%patch103 -p0
%patch104 -p0
%patch105 -p0
%patch106 -p0
%patch107 -p0
%patch108 -p0
%patch109 -p0
%patch110 -p0
%patch111 -p0
%patch112 -p0
%patch113 -p0
%patch114 -p0
%patch115 -p0
%patch116 -p0
%patch117 -p0
%patch118 -p0
%patch119 -p0
%patch120 -p0
%patch121 -p0
%patch122 -p0
%patch123 -p0
%patch124 -p0
%patch125 -p0
%patch126 -p0
%patch127 -p0
%patch128 -p0
%patch129 -p0
%patch130 -p0
%patch131 -p0
%patch132 -p0
%patch133 -p0
%patch134 -p0
%patch135 -p0
%patch136 -p0
%patch137 -p0
%patch138 -p0
%patch139 -p0
%patch140 -p0
%patch141 -p0

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
%attr(755,root,root) %{gcclib}/lto-wrapper
%attr(755,root,root) %{gcclib}/lto1
%{gcclib}/libg*.a
%{gcclib}/%{target}*
%{gcclib}/plugin
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
