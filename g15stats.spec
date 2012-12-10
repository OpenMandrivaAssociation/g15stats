Name:                   g15stats
Version:                1.9.2
Release:                4
Summary:                CPU/Memory/Swap usage meter for G15Daemon
License:                GPLv2+
Group:                  System/Configuration/Hardware
URL:                    http://g15daemon.sourceforge.net/
Source0:                http://downloads.sourceforge.net/g15daemon/g15stats-%{version}.tar.bz2
Patch0:                 g15stats-1.9.2-rosa-linkage.patch
BuildRequires:          g15-devel
BuildRequires:          g15daemon_client-devel
BuildRequires:          g15render-devel
BuildRequires:          pkgconfig(libgtop-2.0)

%description
A CPU/Memory/Swap usage meter for G15Daemon.

This first version of G15Stats requires libgtop development packages to be
installed before compilation.

Features:
CPU Screen displays graphs of User/System/Nice and Idle time, along with
LoadAVG and Uptime.

Memory Screen displays Memory Total & Free, and graph of Used vs
Buffered+Cached Memory.

Swap Screen displays Used, Free and Total swap space, along with the number
of pages currently paged in/out.

Network Screen displays Total bytes In/Out, history graph, Peak speed.

%prep
%setup -q
%patch0 -p1

%build
./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std
%__rm -r %{buildroot}%{_docdir}

%files 
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog README
%defattr(-,root,root,0755)
%{_bindir}/g15stats


%changelog
* Thu Feb 03 2011 Funda Wang <fwang@mandriva.org> 1.9.2-3mdv2011.0
+ Revision: 635486
- tighten BR

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.2-2mdv2011.0
+ Revision: 610783
- rebuild

* Fri Dec 11 2009 Jérôme Brenier <incubusss@mandriva.org> 1.9.2-1mdv2010.1
+ Revision: 476531
- new version 1.9.2
- use ./autogen.sh / %%configure
- fix license tag

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2010.0
+ Revision: 428989
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2009.0
+ Revision: 245592
- rebuild

* Fri Feb 08 2008 David Walluck <walluck@mandriva.org> 1.0-1mdv2008.1
+ Revision: 163937
- import g15stats


