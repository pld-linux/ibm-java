%define __spec_install_post exit 0
Summary:	IBM Java virtual machine
Summary(pl):	Implementacje Javy firmy IBM
Name:		ibm-java
Version:	1.3
Release:	2
License:	Look into documentation
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Source0:	IBMJava2-JRE-13.tgz
Patch0:		%{name}-bash.patch
URL:		http://www.ibm.com/developer/java/
Provides:	jre = %{version}
Provides:	jar
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		java		IBMJava2-13
%define		jredir		%{_libdir}/%{java}

%description
This is IBM's Java implementation.

%description -l pl
Pakiet zawiera implementacje Javy firmy IBM.

%prep
%setup -q -n %{java}
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir}}

cp -a jre $RPM_BUILD_ROOT%{_libdir}/%{java}
ln -sf %{java} $RPM_BUILD_ROOT%{_libdir}/java-jre 

for bin in $RPM_BUILD_ROOT%{jredir}/bin/exe/*; do
	nbin=$(basename "$bin")
	ln -sf %{jredir}/bin/${nbin} $RPM_BUILD_ROOT%{_bindir}/${nbin}
done

gzip -9nf docs/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.gz

%{_bindir}/*

%dir %{jredir}
%{_libdir}/java-jre

%dir %{jredir}/bin
%attr(755,root,root) %{jredir}/bin/JavaPluginControlPanel
%attr(755,root,root) %{jredir}/bin/jvmtcf
%attr(755,root,root) %{jredir}/bin/libdt_socket.so
%attr(755,root,root) %{jredir}/bin/libjitc.so
%attr(755,root,root) %{jredir}/bin/oldjava
%attr(755,root,root) %{jredir}/bin/awt_robot
%attr(755,root,root) %{jredir}/bin/keytool
%attr(755,root,root) %{jredir}/bin/libfontmanager.so
%attr(755,root,root) %{jredir}/bin/libjpeg.so
%attr(755,root,root) %{jredir}/bin/oldjavaw
%attr(755,root,root) %{jredir}/bin/libJdbcOdbc.so
%attr(755,root,root) %{jredir}/bin/libhpi.so
%attr(755,root,root) %{jredir}/bin/libjsound.so
%attr(755,root,root) %{jredir}/bin/policytool
%attr(755,root,root) %{jredir}/bin/libagent.so
%attr(755,root,root) %{jredir}/bin/libhprof.so
%attr(755,root,root) %{jredir}/bin/libnet.so
%attr(755,root,root) %{jredir}/bin/rmid
%attr(755,root,root) %{jredir}/bin/java
%attr(755,root,root) %{jredir}/bin/libawt.so
%attr(755,root,root) %{jredir}/bin/libjava.so
%attr(755,root,root) %{jredir}/bin/liborb.so
%attr(755,root,root) %{jredir}/bin/rmiregistry
%attr(755,root,root) %{jredir}/bin/javaplugin.so
%attr(755,root,root) %{jredir}/bin/libcmm.so
%attr(755,root,root) %{jredir}/bin/libjavaplugin12.so
%attr(755,root,root) %{jredir}/bin/libxhpi.so
%attr(755,root,root) %{jredir}/bin/tnameserv
%attr(755,root,root) %{jredir}/bin/javaw
%attr(755,root,root) %{jredir}/bin/libdcpr.so
%attr(755,root,root) %{jredir}/bin/libjdwp.so
%attr(755,root,root) %{jredir}/bin/libzip.so

%dir %{jredir}/bin/exe
%attr(755,root,root) %{jredir}/bin/exe/java
%attr(755,root,root) %{jredir}/bin/exe/javaw
%attr(755,root,root) %{jredir}/bin/exe/keytool
%attr(755,root,root) %{jredir}/bin/exe/oldjava
%attr(755,root,root) %{jredir}/bin/exe/oldjavaw
%attr(755,root,root) %{jredir}/bin/exe/policytool
%attr(755,root,root) %{jredir}/bin/exe/rmid
%attr(755,root,root) %{jredir}/bin/exe/rmiregistry
%attr(755,root,root) %{jredir}/bin/exe/tnameserv

%dir %{jredir}/bin/classic
%{jredir}/bin/classic/Xusage.txt
%attr(755,root,root) %{jredir}/bin/classic/libjvm.so

%dir %{jredir}/lib
%{jredir}/lib/*
