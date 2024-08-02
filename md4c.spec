Name: md4c
Version: 0.5.2
Release: 1
Source0: https://github.com/mity/md4c/archive/refs/tags/release-%{version}.tar.gz
Summary: Library for MarkDown handling
URL: https://github.com/mity/md4c
License: MIT
Group: System/Libraries
BuildSystem: cmake

%description
MD4C is Markdown parser implementation in C

%install -a
%libpackages

echo '%{_includedir}/md4c.h' >>%{specpartsdir}/%{_lib}md4c-devel.specpart
echo '%{_includedir}/md4c-html.h' >>%{specpartsdir}/%{_lib}md4c-html-devel.specpart

%files
%{_bindir}/md2html
%{_mandir}/man1/md2html.1*
