Summary:	Cross AVR GNU binary utility development utilities - gcc
Summary(es):	Utilitarios para desarrollo de binarios de la GNU - AVR gcc
Summary(fr):	Utilitaires de développement binaire de GNU - AVR gcc
Summary(pl):	Skro¶ne narzêdzia programistyczne GNU dla AVR - gcc
Summary(pt_BR): Utilitários para desenvolvimento de binários da GNU - AVR gcc
Summary(tr):    GNU geliþtirme araçlarý - AVR gcc
Name:		crossavr-gcc
Version:	3.3.2
Release:	2
Epoch:		1
License:	GPL
Group:		Development/Languages
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-%{version}.tar.bz2
# Source0-md5:	65999f654102f5438ac8562d13a6eced
BuildRequires:	autoconf
BuildRequires:	/bin/bash
BuildRequires:	bison
BuildRequires:	crossavr-binutils
BuildRequires:	flex
Requires:	crossavr-binutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		avr
%define		arch		%{_prefix}/%{target}
%define		gccarch		%{_prefix}/lib/gcc-lib/%{target}
%define		gcclib		%{_prefix}/lib/gcc-lib/%{target}/%{version}
%define		no_install_post_strip	1

%description
This package contains a cross-gcc which allows the creation of
binaries to be run on Atmel AVR on i386-machines.

%description -l de
Dieses Paket enthält einen Cross-gcc, der es erlaubt, auf einem
i386-Rechner Code für Atmel AVR zu generieren.

%description -l pl
Ten pakiet zawiera skro¶ny gcc pozwalaj±cy na robienie na maszynach
i386 binariów do uruchamiania na Atmel AVR.

%package c++
Summary:	C++ support for avr-gcc
Summary(pl):	Obs³uga C++ dla avr-gcc
Group:		Development/Languages
Requires:	crossavr-gcc = %{epoch}:%{version}

%description c++
This package adds C++ support to the GNU Compiler Collection for AVR.

%description c++ -l pl
Ten pakiet dodaje obs³ugê C++ do kompilatora gcc dla AVR.

%prep
%setup -q -n gcc-%{version}

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
	--disable-shared \
	--enable-languages="c,c++" \
	--enable-long-long \
	--with-gnu-as \
	--with-gnu-ld \
	--with-system-zlib \
	--with-multilib \
	--without-x \
	--target=%{target}

PATH=$PATH:/sbin:%{_sbindir}

cd ..
#LDFLAGS_FOR_TARGET="%{rpmldflags}"

%{__make} -C obj-%{target}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_datadir},%{_bindir},%{gcclib}}

cd obj-%{target}
PATH=$PATH:/sbin:%{_sbindir}

%{__make} -C gcc install \
	DESTDIR=$RPM_BUILD_ROOT

# c++filt is provided by binutils
#rm -f $RPM_BUILD_ROOT%{_bindir}/i386-mipsel-c++filt

# what is this there for???
rm -f $RPM_BUILD_ROOT%{_libdir}/libiberty.a

# the same... make hardlink
#ln -f $RPM_BUILD_ROOT%{arch}/bin/gcc $RPM_BUILD_ROOT%{_bindir}/%{target}-gcc

%{target}-strip -g $RPM_BUILD_ROOT%{gcclib}/libgcc.a

#%find_lang %{name}

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
#%attr(755,root,root) %{gcclib}/tradcpp0
#%attr(755,root,root) %{gcclib}/cpp0
%attr(755,root,root) %{gcclib}/collect2
%{gcclib}/libgcc.a
%{gcclib}/specs*
%{gcclib}/%{target}*
%dir %{gcclib}/include
%{gcclib}/include/*.h
%{_mandir}/man1/%{target}-gcc.1*

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-g++
%attr(755,root,root) %{_bindir}/%{target}-c++
%attr(755,root,root) %{gcclib}/cc1plus
%{_mandir}/man1/%{target}-g++.1*
