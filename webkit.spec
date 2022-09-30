#FIXME
# For some unknown (yet) reason webkit on aarch64 can be build only on mcbin. Synquacer causing strange issue.

%define _empty_manifest_terminate_build 0
%define _disable_lto 1
%define Werror_cflags %nil

%define oname webkitgtk

%define api 4.0
%define api4 4.1
%define api5 5.0

%define javascriptcoregtk4_major 18
%define libjavascriptcoregtk4 %mklibname javascriptcoregtk %{api}
%define javascriptcoregtk_gir4 %mklibname javascriptcore-gir %{api}

%define javascriptcoregtk4.1_major 0
%define libjavascriptcoregtk4.1 %mklibname javascriptcoregtk %{api4}
%define javascriptcoregtk_gir4.1 %mklibname javascriptcore-gir %{api4}

%define javascriptcoregtk_major 0
%define libjavascriptcoregtk %mklibname javascriptcoregtk %{api5}
%define javascriptcoregtk_gir %mklibname javascriptcore-gir %{api5}

%define webkit2_major 37
%define libwebkit2 %mklibname webkit2gtk %{api}
%define webkit2_gir %mklibname webkit2gtk-gir %{api}

%define webkit2_major 0
%define libwebkit4.1 %mklibname webkit2gtk %{api4}
%define webkit4.1_gir %mklibname webkit2gtk-gir %{api4}

%define webkit5_major 0
%define libwebkit5 %mklibname webkit2gtk %{api5}
%define webkit5_gir %mklibname webkit2gtk-gir %{api5}

%define develname %mklibname -d webkit5
%define develname4.1 %mklibname -d webkit4.1
%define develname4 %mklibname -d webkit2

Summary:	Web browser engine
Name:		webkit
Version:	2.38.0
Release:	2
License:	BSD and LGPLv2+
Group:		System/Libraries
Source0:	http://webkitgtk.org/releases/%{oname}-%{version}.tar.xz
# (cb) force disable lto when building the typelibs
#Patch1:		webkitgtk-2.10.4-nolto.patch
Patch3:		webkit-gtk-2.24.4-eglmesaext-include.patch
# imported from mga
Patch4:		webkitgtk-linking.patch
URL:		http://www.webkitgtk.org
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	bubblewrap
BuildRequires:	ccache
BuildRequires:	flex
BuildRequires:	gperf
BuildRequires:	hyphen-devel
BuildRequires:	perl-JSON-PP
BuildRequires:	xdg-dbus-proxy
BuildRequires:  ruby
BuildRequires:  rubygems
BuildRequires:  cmake
BuildRequires:	libatomic-devel
BuildRequires:	egl-devel
# For wayland-scanner
BuildRequires:	wayland-tools
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(geoclue-2.0)
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libavif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwoff2dec)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:	pkgconfig(manette-0.2)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wpe-1.0)
BuildRequires:  pkgconfig(wpebackend-fdo-1.0)
BuildRequires:  pkgconfig(xt)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libwoff2common)
BuildRequires:	pkgconfig(libwoff2enc)
BuildRequires:	pkgconfig(libwoff2dec)
BuildRequires:	woff2-devel

Requires:	%{libwebkit2} = %{version}
%rename		webkit2

%description
WebKit is an open source web browser engine.

%package -n %{name}4.1
Summary:	Version of the WebKit engine for older libraries
Group:		System/Libraries

%description -n %{name}4.1
Version of the WebKit engine for older libraries

%package -n %{name}4
Summary:	Version of the WebKit engine for older libraries
Group:		System/Libraries

%description -n %{name}4
Version of the WebKit engine for older libraries

%package	jsc4
Summary:	JavaScriptCore shell for old WebKit GTK+
Group:		Development/GNOME and GTK+

%description	jsc4
jsc4 is a shell for old JavaScriptCore, WebKit's JavaScript engine. It
allows you to interact with the JavaScript engine directly.

%package	jsc4.1
Summary:	JavaScriptCore shell for old WebKit GTK+
Group:		Development/GNOME and GTK+

%description	jsc4.1
jsc4 is a shell for old JavaScriptCore, WebKit's JavaScript engine. It
allows you to interact with the JavaScript engine directly.

%package	jsc
Summary:	JavaScriptCore shell for WebKit GTK+
Group:		Development/GNOME and GTK+

%description	jsc
jsc is a shell for JavaScriptCore, WebKit's JavaScript engine. It
allows you to interact with the JavaScript engine directly.

%package -n	%{libwebkit2}
Summary:	GTK+ port of WebKit web browser engine
Group:		System/Libraries
Requires:	%{name}4 = %{version}

%description -n	%{libwebkit2}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%package -n	%{libwebkit4.1}
Summary:	GTK+ port of WebKit web browser engine
Group:		System/Libraries
Requires:	%{name}4.1 = %{version}

%description -n	%{libwebkit4.1}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%package -n	%{libwebkit5}
Summary:	GTK+ port of WebKit web browser engine
Group:		System/Libraries
Requires:	%{name} = %{version}

%description -n	%{libwebkit5}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%package -n	%{libjavascriptcoregtk4}
Summary:        GTK+ port of WebKit web browser engine for old libraries
Group:          System/Libraries

%description -n	%{libjavascriptcoregtk4}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

This version is for use with old libraries

%package -n	%{libjavascriptcoregtk4.1}
Summary:        GTK+ port of WebKit web browser engine for old libraries
Group:          System/Libraries

%description -n	%{libjavascriptcoregtk4.1}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

This version is for use with old libraries

%package -n	%{libjavascriptcoregtk}
Summary:        GTK+ port of WebKit web browser engine
Group:          System/Libraries

%description -n	%{libjavascriptcoregtk}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%package -n	%{develname4}
Summary:	Development files for WebKit GTK+ port for old libraries
Group:		Development/GNOME and GTK+
Provides:	%{name}2-devel = %{version}-%{release}
Provides:	libwebkit2gtk-devel = %{version}-%{release}
Requires:	%{libjavascriptcoregtk4} = %{version}
Requires:	%{libwebkit2} = %{version}
Requires:	%{javascriptcoregtk_gir4} = %{version}
Requires:	%{webkit2_gir} = %{version}

%description -n	%{develname4}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux. This package contains development headers for use with old
libraries.

%package -n	%{develname4.1}
Summary:	Development files for WebKit GTK+ port for old libraries
Group:		Development/GNOME and GTK+
Provides:	%{name}4.1-devel = %{version}-%{release}
Provides:	libwebkit4.1gtk-devel = %{version}-%{release}
Requires:	%{libjavascriptcoregtk4.1} = %{version}
Requires:	%{libwebkit4.1} = %{version}
Requires:	%{javascriptcoregtk_gir4.1} = %{version}
Requires:	%{webkit4.1_gir} = %{version}

%description -n	%{develname4.1}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux. This package contains development headers for use with old
libraries.

%package -n	%{develname}
Summary:	Development files for WebKit GTK+ port
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libwebkit5gtk-devel = %{version}-%{release}
Requires:	%{libjavascriptcoregtk} = %{version}
Requires:	%{libwebkit5} = %{version}
Requires:	%{javascriptcoregtk_gir} = %{version}
Requires:	%{webkit5_gir} = %{version}

%description -n	%{develname}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux. This package contains development headers.

%package -n	%{javascriptcoregtk_gir}
Summary:        GObject Introspection interface description for JSCore
Group:          System/Libraries
Requires:       %{libjavascriptcoregtk} = %{version}-%{release}

%description -n	%{javascriptcoregtk_gir}
GObject Introspection interface description for JSCore.

%package -n	%{javascriptcoregtk_gir4.1}
Summary:        GObject Introspection interface description for JSCore
Group:          System/Libraries
Requires:       %{libjavascriptcoregtk4.1} = %{version}-%{release}

%description -n	%{javascriptcoregtk_gir4.1}
GObject Introspection interface description for JSCore.

%package -n	%{javascriptcoregtk_gir4}
Summary:        GObject Introspection interface description for JSCore
Group:          System/Libraries
Requires:       %{libjavascriptcoregtk4} = %{version}-%{release}

%description -n	%{javascriptcoregtk_gir4}
GObject Introspection interface description for JSCore.

%package -n	%{webkit2_gir}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries
Requires:       %{libwebkit2} = %{version}-%{release}

%description -n	%{webkit2_gir}
GObject Introspection interface description for WebKit.

%package -n	%{webkit4.1_gir}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries
Requires:       %{libwebkit4.1} = %{version}-%{release}

%description -n	%{webkit4.1_gir}
GObject Introspection interface description for WebKit.

%package -n	%{webkit5_gir}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries
Requires:       %{libwebkit5} = %{version}-%{release}

%description -n	%{webkit5_gir}
GObject Introspection interface description for WebKit.

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
# (tpg) do not build debug code
# (cb) clang segfaults at Oz
# (cb) ensure lto disabled
%global optflags %(echo %{optflags} -fno-lto | sed -e 's/-g3 /-g0 /' -e 's/-g /-g0 /' -e 's/-gdwarf-4//' -e 's/-Oz/-O1/')

# fix weird memory allocation
export GIGACAGE_ENABLED=0

#ifarch %{ix86} %{arm} %{armx}
# clang wont build this on i586:
# /bits/atomic_base.h:408:16: error: cannot compile this atomic library call yet
#      { return __atomic_add_fetch(&_M_i, 1, memory_order_seq_cst); }
# ARMv7hnl build failed on Clang, use again GCC.
%ifarch %{arm}
export CC=gcc
export CXX=g++
%endif

# Clang 14 and webkit 2.36.0 crashing at compile
# Clang 15 and webkit 2.38.0 compiles fine but hardly crashing at runtime. Back to GCC.
export CC=gcc
export CXX=g++

export CFLAGS="%{optflags} -DNDEBUG -DG_DISABLE_CAST_CHECKS"
export CXXFLAGS="%{optflags} -DNDEBUG -DG_DISABLE_CAST_CHECKS"
export LDFLAGS="%{ldflags} -fuse-ld=bfd -Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
export CMAKE_BUILD_DIR=build-4.0
%cmake	-DPORT=GTK \
	-DUSE_SOUP2=ON \
	-DUSE_LD_GOLD=OFF \
	-DUSE_WOFF2:BOOL=ON \
	-DLIB_INSTALL_DIR:PATH=%{_libdir} \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_C_FLAGS_RELEASE="" \
	-DPYTHON_EXECUTABLE=%{_bindir}/python3 \
	-DUSE_WPE_RENDERER=ON \
	-DUSE_AVIF=ON \
%ifarch aarch64 %{ix86} %{arm}
	-DENABLE_JIT=OFF \
	-DUSE_SYSTEM_MALLOC=ON \
%endif
%ifarch aarch64
	-DWTF_CPU_ARM64_CORTEXA53=OFF \
%endif
%ifarch %{ix86}
	-DCMAKE_CXX_LIBRARY_ARCHITECTURE=%{_arch} \
%endif
	-DCMAKE_C_FLAGS_DEBUG="" \
	-DCMAKE_CXX_FLAGS_RELEASE="" \
	-DCMAKE_CXX_FLAGS_DEBUG=""
cd ..

export CMAKE_BUILD_DIR=build-4.1
%cmake	-DPORT=GTK \
	-DUSE_SOUP2=OFF \
	-DUSE_LD_GOLD=OFF \
	-DUSE_WOFF2:BOOL=ON \
	-DLIB_INSTALL_DIR:PATH=%{_libdir} \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_C_FLAGS_RELEASE="" \
	-DPYTHON_EXECUTABLE=%{_bindir}/python3 \
	-DUSE_WPE_RENDERER=ON \
	-DUSE_AVIF=ON \
%ifarch aarch64 %{ix86} %{arm}
	-DENABLE_JIT=OFF \
	-DUSE_SYSTEM_MALLOC=ON \
%endif
%ifarch aarch64
	-DWTF_CPU_ARM64_CORTEXA53=OFF \
%endif
%ifarch %{ix86}
	-DCMAKE_CXX_LIBRARY_ARCHITECTURE=%{_arch} \
%endif
	-DCMAKE_C_FLAGS_DEBUG="" \
	-DCMAKE_CXX_FLAGS_RELEASE="" \
	-DCMAKE_CXX_FLAGS_DEBUG=""
cd ..

export CMAKE_BUILD_DIR=build-5.0
%cmake	-DPORT=GTK \
	-DUSE_GTK4=ON \
	-DUSE_LD_GOLD=OFF \
	-DUSE_WOFF2:BOOL=ON \
	-DLIB_INSTALL_DIR:PATH=%{_libdir} \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_C_FLAGS_RELEASE="" \
	-DPYTHON_EXECUTABLE=%{_bindir}/python3 \
	-DUSE_WPE_RENDERER=ON \
	-DUSE_AVIF=ON \
	-DUSE_SOUP2=OFF \
%ifarch aarch64 %{ix86} %{arm}
	-DENABLE_JIT=OFF \
	-DUSE_SYSTEM_MALLOC=ON \
%endif
%ifarch aarch64
	-DWTF_CPU_ARM64_CORTEXA53=OFF \
%endif
%ifarch %{ix86}
	-DCMAKE_CXX_LIBRARY_ARCHITECTURE=%{_arch} \
%endif
	-DCMAKE_C_FLAGS_DEBUG="" \
	-DCMAKE_CXX_FLAGS_RELEASE="" \
	-DCMAKE_CXX_FLAGS_DEBUG=""
cd ..

%make_build -C build-4.0
%make_build -C build-4.1
%make_build -C build-5.0

%install
%make_install -C build-4.0

%find_lang WebKit2GTK-%{api}

%make_install -C build-4.1

%find_lang WebKit2GTK-%{api4.1}

%make_install -C build-5.0

%find_lang WebKit2GTK-%{api5}

%files -n %{name}4 -f WebKit2GTK-%{api}.lang
%doc %{_datadir}/gtk-doc/html/
%dir %{_libexecdir}/webkit2gtk-%{api}
%{_bindir}/WebKitWebDriver
%{_libexecdir}/webkit2gtk-%{api}/*
%exclude %{_libexecdir}/webkit2gtk-%{api}/jsc
%dir %{_libdir}/webkit2gtk-%{api}
%dir %{_libdir}/webkit2gtk-%{api}/injected-bundle
%{_libdir}/webkit2gtk-%{api}/injected-bundle/libwebkit2gtkinjectedbundle.so

%files -n %{name}4.1 -f WebKit2GTK-%{api4.1}.lang
%doc %{_datadir}/gtk-doc/html/
%dir %{_libexecdir}/webkit2gtk-%{api4.1}
%{_bindir}/WebKitWebDriver
%{_libexecdir}/webkit2gtk-%{api4.1}/*
%exclude %{_libexecdir}/webkit2gtk-%{api4.1}/jsc
%dir %{_libdir}/webkit2gtk-%{api4.1}
%dir %{_libdir}/webkit2gtk-%{api4.1}/injected-bundle
%{_libdir}/webkit2gtk-%{api4.1}/injected-bundle/libwebkit2gtkinjectedbundle.so

%files -f WebKit2GTK-%{api5}.lang
%dir %{_libexecdir}/webkit2gtk-%{api5}
%{_libexecdir}/webkit2gtk-%{api5}/*
%exclude %{_libexecdir}/webkit2gtk-%{api5}/jsc
%dir %{_libdir}/webkit2gtk-%{api5}
%dir %{_libdir}/webkit2gtk-%{api5}/injected-bundle
%{_libdir}/webkit2gtk-%{api5}/injected-bundle/libwebkit2gtkinjectedbundle.so

%files jsc4
%{_libexecdir}/webkit2gtk-%{api}/jsc

%files jsc4.1
%{_libexecdir}/webkit2gtk-%{api4.1}/jsc

%files jsc
%{_libexecdir}/webkit2gtk-%{api5}/jsc

%files -n %{libjavascriptcoregtk4}
%{_libdir}/libjavascriptcoregtk-%{api}.so.%{javascriptcoregtk4_major}
%{_libdir}/libjavascriptcoregtk-%{api}.so.%{javascriptcoregtk4_major}.*

%files -n %{libjavascriptcoregtk4.1}
%{_libdir}/libjavascriptcoregtk-%{api4.1}.so.%{javascriptcoregtk4.1_major}
%{_libdir}/libjavascriptcoregtk-%{api4.1}.so.%{javascriptcoregtk4.1_major}.*

%files -n %{libjavascriptcoregtk}
%{_libdir}/libjavascriptcoregtk-%{api5}.so.%{javascriptcoregtk_major}
%{_libdir}/libjavascriptcoregtk-%{api5}.so.%{javascriptcoregtk_major}.*

%files -n %{libwebkit2}
%{_libdir}/libwebkit2gtk-%{api}.so.%{webkit2_major}
%{_libdir}/libwebkit2gtk-%{api}.so.%{webkit2_major}.*

%files -n %{libwebkit4.1}
%{_libdir}/libwebkit2gtk-%{api4.1}.so.%{webkit4.1_major}
%{_libdir}/libwebkit2gtk-%{api4.1}.so.%{webkit4.1_major}.*

%files -n %{libwebkit5}
%{_libdir}/libwebkit2gtk-%{api5}.so.%{webkit5_major}
%{_libdir}/libwebkit2gtk-%{api5}.so.%{webkit5_major}.*

%files -n %{develname}
%{_includedir}/webkitgtk-%{api5}
%{_libdir}/*-%{api5}.so
%{_libdir}/pkgconfig/*-%{api5}.pc
%{_datadir}/gir-1.0/*-%{api5}.gir

%files -n %{develname4.1}
%{_includedir}/webkitgtk-%{api4.1}
%{_libdir}/*-%{api4.1}.so
%{_libdir}/pkgconfig/*-%{api4.1}.pc
%{_datadir}/gir-1.0/*-%{api4.1}.gir

%files -n %{develname4}
%{_includedir}/webkitgtk-%{api}
%{_libdir}/*-%{api}.so
%{_libdir}/pkgconfig/*-%{api}.pc
%{_datadir}/gir-1.0/*-%{api}.gir

%files -n %{javascriptcoregtk_gir}
%{_libdir}/girepository-1.0/JavaScriptCore-%{api5}.typelib

%files -n %{javascriptcoregtk_gir4.1}
%{_libdir}/girepository-1.0/JavaScriptCore-%{api4.1}.typelib

%files -n %{javascriptcoregtk_gir4}
%{_libdir}/girepository-1.0/JavaScriptCore-%{api}.typelib

%files -n %{webkit2_gir}
%{_libdir}/girepository-1.0/WebKit2-%{api}.typelib
%{_libdir}/girepository-1.0/WebKit2WebExtension-%{api}.typelib

%files -n %{webkit4.1_gir}
%{_libdir}/girepository-1.0/WebKit2-%{api4.1}.typelib
%{_libdir}/girepository-1.0/WebKit2WebExtension-%{api4.1}.typelib

%files -n %{webkit5_gir}
%{_libdir}/girepository-1.0/WebKit2-%{api5}.typelib
%{_libdir}/girepository-1.0/WebKit2WebExtension-%{api5}.typelib
