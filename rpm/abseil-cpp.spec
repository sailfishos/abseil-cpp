Name:           abseil-cpp
Version:        20230125.3
Release:        1
Summary:        C++ Common Libraries

# The entire source is Apache-2.0, except:
#   - The following files are Public Domain:
#       absl/time/internal/cctz/src/tzfile.h
#         ** This file is in the public domain, so clarified as of
#         ** 1996-06-05 by Arthur David Olson.
#       absl/time/internal/cctz/testdata/zoneinfo/iso3166.tab
#         # This file is in the public domain, so clarified as of
#         # 2009-05-17 by Arthur David Olson.
#       absl/time/internal/cctz/testdata/zoneinfo/zone1970.tab
#         # This file is in the public domain.
License:        Apache-2.0 AND Public Domain
URL:            https://abseil.io
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  ninja

%description
Abseil is an open-source collection of C++ library code designed to augment
the C++ standard library. The Abseil library code is collected from
Google's own C++ code base, has been extensively tested and used in
production, and is the same code we depend on in our daily coding lives.

In some cases, Abseil provides pieces missing from the C++ standard; in
others, Abseil provides alternatives to the standard for special needs we've
found through usage in the Google code base. We denote those cases clearly
within the library code we provide you.

Abseil is not meant to be a competitor to the standard library; we've just
found that many of these utilities serve a purpose within our code base,
and we now want to provide those resources to the C++ community as a whole.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
Development headers for %{name}

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%cmake . \
  -GNinja \
  -DABSL_FIND_GOOGLETEST:BOOL=OFF \
  -DABSL_ENABLE_INSTALL:BOOL=ON \
  -DABSL_BUILD_TESTING:BOOL=OFF \
  -DABSL_PROPAGATE_CXX_STD:BOOL=ON \
  -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo
%ninja_build

%install
%ninja_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc FAQ.md README.md UPGRADES.md
%{_libdir}/libabsl_*.so.*

%files devel
%{_includedir}/absl
%{_libdir}/libabsl_*.so
%{_libdir}/cmake/absl
%{_libdir}/pkgconfig/*.pc
