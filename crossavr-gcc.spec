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
Version:	4.6.2
Release:	5
Epoch:		1
Patch1:		gcc-bug51969.patch
# Patches 1xx are taken form Atmel official AVR8-GNU toolchain version 3.4.0.663.
Patch100:	200-gcc-libiberty-Makefile.in.patch
Patch101:	300-gcc-fixedpoint-3-4-2010.patch
Patch102:	301-gcc-xmega-v14.patch
Patch103:	302-gcc-avrtiny10.patch
Patch104:	303-gcc-osmain.patch
Patch105:	304-gcc-builtins-v6.patch
Patch106:	305-gcc-avrtiny10-non-fixedpoint.patch
Patch107:	306-gcc-option-list-devices.patch
Patch108:	400-gcc-new-devices.patch
Patch109:	401-gcc-atmega32_5_50_90_pa.patch
Patch110:	402-gcc-attiny1634.patch
Patch111:	403-gcc-atmega48pa.patch
Patch112:	404-gcc-atxmega_16_32_a4u.patch
Patch113:	405-gcc-atxmega64_128_192_256a3u.patch
Patch114:	406-gcc-atmegarfr2_a2.patch
Patch115:	407-gcc-atmega165pa.patch
Patch116:	408-gcc-atxmega384c3.patch
Patch117:	409-gcc-attiny80.patch
Patch118:	410-gcc-atxmega128a4u.patch
Patch119:	411-gcc-atxmega64d4.patch
Patch120:	412-gcc-atmega164pa_168pa_32a_64a.patch
Patch121:	413-gcc-atxmega64_128_b3.patch
Patch122:	414-gcc-atxmega64b1.patch
Patch123:	415-gcc-atmega_8a_128a_1284.patch
Patch124:	416-gcc-atxmega64a4u.patch
Patch125:	417-gcc-atxmega128d4.patch
Patch126:	418-gcc-atmxt336s.patch
Patch127:	419-gcc-atxmega16c4_32c4_128c3_256c3.patch
Patch128:	420-gcc-atxmega384d3.patch
Patch129:	421-gcc-atmega48hvf.patch
Patch130:	422-gcc-atmega26hvg.patch
Patch131:	423-gcc-atmxt224_224e.patch
Patch132:	424-gcc-atxmega192c3.patch
Patch133:	425-gcc-atmxt112sl.patch
Patch134:	426-gcc-atxmega64c3.patch
Patch135:	427-gcc-ata6285_6286.patch
Patch136:	428-gcc-attiny828.patch
Patch137:	429-gcc-ata5790_5790n_5795.patch
Patch138:	430-gcc-ata5272_ata5505.patch
Patch139:	500-gcc-bug13473.patch
Patch140:	501-gcc-avrtiny10-bug-12510.patch
Patch141:	502-gcc-bug12915.patch
Patch142:	503-gcc-bug13789.patch
Patch143:	504-gcc-conditional-register.patch
Patch144:	505-gcc-avrtc381-tiny.patch
License:	GPL
Group:		Development/Languages
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-%{version}.tar.bz2
# Source0-md5:	028115c4fbfb6cfd75d6369f4a90d87e
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
%patch1 -p2
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
%patch142 -p0
%patch143 -p0
%patch144 -p0

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
