%define _empty_manifest_terminate_build 0
%define _disable_lto 1
%define Werror_cflags %nil

%define oname webkitgtk

%define api 4.0
%define api41 4.1
%define api6 6.0

%define javascriptcoregtk4_major 18
%define libjavascriptcoregtk4 %mklibname javascriptcoregtk %{api}
%define javascriptcoregtk_gir4 %mklibname javascriptcore-gir %{api}

%define javascriptcoregtk41_major 0
%define libjavascriptcoregtk41 %mklibname javascriptcoregtk %{api41}
%define javascriptcoregtk_gir41 %mklibname javascriptcore-gir %{api41}

%define javascriptcoregtk_major 1
%define libjavascriptcoregtk %mklibname javascriptcoregtk %{api6}
%define javascriptcoregtk_gir %mklibname javascriptcore-gir %{api6}

%define webkit2_major 37
%define libwebkit2 %mklibname webkit2gtk %{api}
%define webkit2_gir %mklibname webkit2gtk-gir %{api}

%define webkit41_major 0
%define libwebkit41 %mklibname webkit2gtk %{api41}
%define webkit41_gir %mklibname webkit2gtk-gir %{api41}

%define webkit6_major 4
%define libwebkit6 %mklibname webkit2gtk %{api6}
%define webkit6_gir %mklibname webkit2gtk-gir %{api6}

%define develname %mklibname -d webkit6
%define develname4 %mklibname -d webkit2
%define develname41 %mklibname -d webkit4.1

Summary:	Web browser engine
Name:		webkit
Version:	2.44.0
Release:	1
License:	BSD and LGPLv2+
Group:		System/Libraries
Source0:	https://webkitgtk.org/releases/%{oname}-%{version}.tar.xz
# (cb) force disable lto when building the typelibs
#Patch1:		webkitgtk-2.10.4-nolto.patch
#Patch3:		webkit-gtk-2.24.4-eglmesaext-include.patch
# Fix build. Alleged build system engineers not knowing what their
# own packages provide is beyond ridiculous.
Patch1:		webkit-2.40.5-gnomes-are-stupid-drunk-monkeys-on-crack.patch
# imported from mga
Patch4:		webkitgtk-linking.patch
URL:		https://www.webkitgtk.org
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	bubblewrap
BuildRequires:	ccache
BuildRequires:	flex
BuildRequires:	gettext
BuildRequires:	gperf
BuildRequires:	hyphen-devel
BuildRequires:	perl-JSON-PP
BuildRequires:	xdg-dbus-proxy
BuildRequires:  ruby
BuildRequires:  rubygems
BuildRequires:  cmake
BuildRequires:	libatomic-devel
BuildRequires:	backstrace-devel
BuildRequires:	unifdef
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
BuildRequires:	pkgconfig(gstreamer-transcoder-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:	pkgconfig(harfbuzz-cairo)
BuildRequires:	pkgconfig(harfbuzz-icu)
BuildRequires:	pkgconfig(harfbuzz-gobject)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libavif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libjxl)
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

Requires:	%{name}-common = %{EVRD}
Requires:	%{libwebkit6} = %{version}
%rename		webkit2

%description
WebKit is an open source web browser engine.

%package common
Summary:	Files needed by every version of the WebKit engine
Group:		System/Libraries

%description common
Files needed by every version of the WebKit engine

%package -n %{name}4.1
Summary:	Version of the WebKit engine for older libraries
Group:		System/Libraries
Requires:	%{name}-common = %{EVRD}

%description -n %{name}4.1
Version of the WebKit engine for older libraries

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

%package -n	%{libwebkit41}
Summary:	GTK+ port of WebKit web browser engine for old libraries
Group:		System/Libraries
Requires:	%{name}4.1 = %{version}

%description -n	%{libwebkit41}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux using old libraries.

%package -n	%{libwebkit6}
Summary:	GTK+ port of WebKit web browser engine
Group:		System/Libraries
Requires:	%{name} = %{version}
Obsoletes:	%{_lib}webkit2gtk5.0 < %{EVRD}

%description -n	%{libwebkit6}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%package -n	%{libjavascriptcoregtk41}
Summary:        GTK+ port of WebKit web browser engine for old libraries
Group:          System/Libraries

%description -n	%{libjavascriptcoregtk41}
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

%package -n	%{develname41}
Summary:	Development files for WebKit GTK+ port for old libraries
Group:		Development/GNOME and GTK+
Provides:	%{name}4.1-devel = %{version}-%{release}
Provides:	libwebkit4.1gtk-devel = %{version}-%{release}
Requires:	%{libjavascriptcoregtk41} = %{version}
Requires:	%{libwebkit41} = %{version}
Requires:	%{javascriptcoregtk_gir41} = %{version}
Requires:	%{webkit41_gir} = %{version}

%description -n	%{develname41}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux. This package contains development headers for use with old
libraries.

%package -n	%{develname}
Summary:	Development files for WebKit GTK+ port
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libwebkit6gtk-devel = %{version}-%{release}
Requires:	%{libjavascriptcoregtk} = %{version}
Requires:	%{libwebkit6} = %{version}
Requires:	%{javascriptcoregtk_gir} = %{version}
Requires:	%{webkit6_gir} = %{version}

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

%package -n	%{javascriptcoregtk_gir41}
Summary:        GObject Introspection interface description for JSCore
Group:          System/Libraries
Requires:       %{libjavascriptcoregtk41} = %{version}-%{release}

%description -n	%{javascriptcoregtk_gir41}
GObject Introspection interface description for JSCore.

%package -n	%{webkit41_gir}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries
Requires:       %{libwebkit41} = %{version}-%{release}

%description -n	%{webkit41_gir}
GObject Introspection interface description for WebKit.

%package -n	%{webkit6_gir}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries
Requires:       %{libwebkit6} = %{version}-%{release}

%description -n	%{webkit6_gir}
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

# Clang 14 and webkit 2.36.0 crashing at compile
# Clang 15 and webkit 2.38.0 compiles fine but hardly crashing at runtime. Back to GCC.
# GCC 13.1 and webkit 2.40.1 failed to build, back to Clang 16, and see if it not cause any issues at runtime.
#export CC=gcc
#export CXX=g++

export CFLAGS="%{optflags} -DNDEBUG -DG_DISABLE_CAST_CHECKS"
export CXXFLAGS="%{optflags} -DNDEBUG -DG_DISABLE_CAST_CHECKS"
export LDFLAGS="%{ldflags} -fuse-ld=bfd -Wl,--no-keep-memory -Wl,--reduce-memory-overheads"

export CMAKE_BUILD_DIR=build-4.1
%cmake	-DPORT=GTK \
	-DUSE_SOUP2=OFF \
	-DUSE_GTK4=OFF \
	-DUSE_LD_GOLD=OFF \
	-DUSE_WOFF2:BOOL=ON \
	-DLIB_INSTALL_DIR:PATH=%{_libdir} \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_C_FLAGS_RELEASE="" \
	-DPYTHON_EXECUTABLE=%{_bindir}/python3 \
	-DUSE_WPE_RENDERER=ON \
	-DUSE_AVIF=ON \
%ifarch %{aarch64} %{ix86} %{arm}
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

export CMAKE_BUILD_DIR=build-6.0
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
%ifarch %{aarch64} %{ix86} %{arm}
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

%make_build -C build-4.1

%make_build -C build-6.0

%install

%make_install -C build-4.1

%find_lang WebKitGTK-%{api41}

%make_install -C build-6.0

%find_lang WebKitGTK-%{api6}

%files common
%{_bindir}/WebKitWebDriver

%files -n %{name}4.1 -f WebKitGTK-%{api41}.lang
%dir %{_libexecdir}/webkit2gtk-%{api41}
%{_libexecdir}/webkit2gtk-%{api41}/*
%exclude %{_libexecdir}/webkit2gtk-%{api41}/jsc
%dir %{_libdir}/webkit2gtk-%{api41}
%dir %{_libdir}/webkit2gtk-%{api41}/injected-bundle
%{_libdir}/webkit2gtk-%{api41}/injected-bundle/libwebkit2gtkinjectedbundle.so

%files -f WebKitGTK-%{api6}.lang
%dir %{_libexecdir}/webkitgtk-%{api6}
%{_libexecdir}/webkitgtk-%{api6}/*
%exclude %{_libexecdir}/webkitgtk-%{api6}/jsc
%dir %{_libdir}/webkitgtk-%{api6}
%dir %{_libdir}/webkitgtk-%{api6}/injected-bundle
%{_libdir}/webkitgtk-%{api6}/injected-bundle/libwebkitgtkinjectedbundle.so

%files jsc4.1
%{_libexecdir}/webkit2gtk-%{api41}/jsc

%files jsc
%{_libexecdir}/webkitgtk-%{api6}/jsc

%files -n %{libjavascriptcoregtk41}
%{_libdir}/libjavascriptcoregtk-%{api41}.so.%{javascriptcoregtk41_major}
%{_libdir}/libjavascriptcoregtk-%{api41}.so.%{javascriptcoregtk41_major}.*

%files -n %{libjavascriptcoregtk}
%{_libdir}/libjavascriptcoregtk-%{api6}.so.%{javascriptcoregtk_major}
%{_libdir}/libjavascriptcoregtk-%{api6}.so.%{javascriptcoregtk_major}.*

%files -n %{libwebkit41}
%{_libdir}/libwebkit2gtk-%{api41}.so.%{webkit41_major}
%{_libdir}/libwebkit2gtk-%{api41}.so.%{webkit41_major}.*

%files -n %{libwebkit6}
%{_libdir}/libwebkitgtk-%{api6}.so.%{webkit6_major}
%{_libdir}/libwebkitgtk-%{api6}.so.%{webkit6_major}.*

%files -n %{develname}
%{_includedir}/webkitgtk-%{api6}
%{_libdir}/*-%{api6}.so
%{_libdir}/pkgconfig/*-%{api6}.pc
%{_datadir}/gir-1.0/*-%{api6}.gir
%doc %{_docdir}/javascriptcoregtk-6.0
%doc %{_docdir}/webkitgtk-6.0
%doc %{_docdir}/webkitgtk-web-process-extension-6.0

%files -n %{develname41}
%{_includedir}/webkitgtk-%{api41}
%{_libdir}/*-%{api41}.so
%{_libdir}/pkgconfig/*-%{api41}.pc
%{_datadir}/gir-1.0/*-%{api41}.gir
%doc %{_docdir}/javascriptcoregtk-4.1
%doc %{_docdir}/webkit2gtk-4.1
%doc %{_docdir}/webkit2gtk-web-extension-4.1

%files -n %{javascriptcoregtk_gir}
%{_libdir}/girepository-1.0/JavaScriptCore-%{api6}.typelib

%files -n %{javascriptcoregtk_gir41}
%{_libdir}/girepository-1.0/JavaScriptCore-%{api41}.typelib

%files -n %{webkit41_gir}
%{_libdir}/girepository-1.0/WebKit2-%{api41}.typelib
%{_libdir}/girepository-1.0/WebKit2WebExtension-%{api41}.typelib

%files -n %{webkit6_gir}
%{_libdir}/girepository-1.0/WebKit-%{api6}.typelib
%{_libdir}/girepository-1.0/WebKitWebProcessExtension-%{api6}.typelib
