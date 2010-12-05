Name:                   g15stats
Version:                1.9.2
Release:                %mkrel 2
Summary:                CPU/Memory/Swap usage meter for G15Daemon
License:                GPLv2+
Group:                  System/Configuration/Hardware
URL:                    http://g15daemon.sourceforge.net/
Source0:                http://downloads.sourceforge.net/g15daemon/g15stats-%{version}.tar.bz2
BuildRequires:          g15-devel
BuildRequires:          g15daemon_client-devel
BuildRequires:          g15render-devel
BuildRequires:          libgtop2.0-devel
BuildRequires:          X11-devel
BuildRequires:          x11-proto-devel
BuildRoot:              %{_tmppath}/%{name}-%{version}-%{release}-root

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

%build
./autogen.sh
%{configure}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__rm} -r %{buildroot}%{_docdir}

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%defattr(-,root,root,0755)
%{_bindir}/g15stats
