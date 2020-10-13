Name:    memleax
Version: 1.1.1
Release: 2
Summary: Memory lead detection tool
License: GPLv2
URL: https://github.com/WuBingzheng/memleax
Source0: https://github.com/WuBingzheng/memleax/archive/v%{version}#/memleax-%{version}.tar.gz

BuildRequires: 	make libunwind-devel elfutils-devel gdb

%description
memleax debugs memory leak of a running process by attaching it.
It hooks the target process's invocation of memory allocation and free,
and reports the memory blocks which live long enough as memory leak, in real time.
The default expire threshold is 10 seconds, however you should always
set it by `-e` option according to your scenarios.

It is very *convenient* to use, and suitable for production environment.
There is no need to recompile the program or restart the target process.
You run `memleax` to monitor the target process, wait for the real-time memory
leak report, and then kill it (e.g. by Ctrl-C) to stop monitoring.

memleax follows new threads, but not forked processes.
If you want to debug multiple processes, just run multiple memleax.

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
* Tue Oct 13 2020 Qingqing Li <liqingqing3@huawei.com>
- update source0

* Sun Mar 29 2020 Wei Xiong <myeuler@163.com>
- Package init

