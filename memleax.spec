Name:    memleax
Version: 1.1.1
Release: 1
Summary: Memory lead detection tool
License: GPLv2
URL: https://github.com/WuBingzheng/memleax
Source0: https://github.com/WuBingzheng/memleax/archive/memleax-%{version}.tar.gz

BuildRequires: 	make

%description
cloc is a tool which can help to do program line caculation.

%prep
%setup -q -n %{name}-%{version}/

%build
./configure
make

%install
make install DESTDIR="%{buildroot}"

%pre
%preun
%post
%postun

%check

%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Mar 29 2020 Wei Xiong <myeuler@163.com>
- Package init

