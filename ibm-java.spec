%define 	__spec_install_post	exit 0
%define		halfname		ibm-java
%define		ver			1.3

Summary:	IBM Java virtual machine
Summary(pl):	Implementacja Javy firmy IBM
Name:		%{halfname}-%{ver}
Version:	0
Release:	1
License:	Look into documentation
Group:		Development/Languages/Java
Source0:	IBMJava2-JRE-13.tgz
Patch0:		%{halfname}-bash.patch
URL:		http://www.ibm.com/developer/java/
Provides:	jre = %{ver}
Provides:	jar
PreReq:		java-env
Requires:	java-env
PreReq:		java-env
Requires(post,preun,postun): java-env
BuildRequires:	java-env
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		java		IBMJava2-13
%define		javadir		%{_libdir}/%{name}
%define		javacfgdir	/etc/sysconfig/java

%description
This is IBM's Java implementation.

%description -l pl
Pakiet zawiera implementacjê Javy firmy IBM.

%prep
%setup -q -n %{java}
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d \
    $RPM_BUILD_ROOT%{javadir} \
    $RPM_BUILD_ROOT%{javacfgdir}

cp -a jre/* $RPM_BUILD_ROOT%{javadir}

# create some config files
echo "MAINDIR=%{name}" > $RPM_BUILD_ROOT%{javacfgdir}/jre.%{name}

%define	lnfile	$RPM_BUILD_ROOT%{javacfgdir}/links.jre.%{name}

echo "%{javadir} %{_libdir}/java-jre"
for bin in $RPM_BUILD_ROOT%{javadir}/bin/exe/*; do
	nbin=$(basename "$bin")
	echo "%{javadir}/bin/${nbin} %{_bindir}/${nbin}" >> %{lnfile}
done

# cp files
javacpmgr --findjars $RPM_BUILD_ROOT > $RPM_BUILD_ROOT%{javacfgdir}/cp.jre.%{name}
# end of config files creation

%clean
rm -rf $RPM_BUILD_ROOT

%post
javaenv --setjava

%preun
javaenv --erasejavaif "jre.%{name}"

%postun
javaenv --setjava

%files
%defattr(644,root,root,755)
%doc docs/*

%dir %{javadir}
%dir %{javadir}/bin
%attr(755,root,root) %{javadir}/bin/JavaPluginControlPanel
%attr(755,root,root) %{javadir}/bin/jvmtcf
%attr(755,root,root) %{javadir}/bin/libdt_socket.so
%attr(755,root,root) %{javadir}/bin/libjitc.so
%attr(755,root,root) %{javadir}/bin/oldjava
%attr(755,root,root) %{javadir}/bin/awt_robot
%attr(755,root,root) %{javadir}/bin/keytool
%attr(755,root,root) %{javadir}/bin/libfontmanager.so
%attr(755,root,root) %{javadir}/bin/libjpeg.so
%attr(755,root,root) %{javadir}/bin/oldjavaw
%attr(755,root,root) %{javadir}/bin/libJdbcOdbc.so
%attr(755,root,root) %{javadir}/bin/libhpi.so
%attr(755,root,root) %{javadir}/bin/libjsound.so
%attr(755,root,root) %{javadir}/bin/policytool
%attr(755,root,root) %{javadir}/bin/libagent.so
%attr(755,root,root) %{javadir}/bin/libhprof.so
%attr(755,root,root) %{javadir}/bin/libnet.so
%attr(755,root,root) %{javadir}/bin/rmid
%attr(755,root,root) %{javadir}/bin/java
%attr(755,root,root) %{javadir}/bin/libawt.so
%attr(755,root,root) %{javadir}/bin/libjava.so
%attr(755,root,root) %{javadir}/bin/liborb.so
%attr(755,root,root) %{javadir}/bin/rmiregistry
%attr(755,root,root) %{javadir}/bin/javaplugin.so
%attr(755,root,root) %{javadir}/bin/libcmm.so
%attr(755,root,root) %{javadir}/bin/libjavaplugin12.so
%attr(755,root,root) %{javadir}/bin/libxhpi.so
%attr(755,root,root) %{javadir}/bin/tnameserv
%attr(755,root,root) %{javadir}/bin/javaw
%attr(755,root,root) %{javadir}/bin/libdcpr.so
%attr(755,root,root) %{javadir}/bin/libjdwp.so
%attr(755,root,root) %{javadir}/bin/libzip.so

%dir %{javadir}/bin/exe
%attr(755,root,root) %{javadir}/bin/exe/java
%attr(755,root,root) %{javadir}/bin/exe/javaw
%attr(755,root,root) %{javadir}/bin/exe/keytool
%attr(755,root,root) %{javadir}/bin/exe/oldjava
%attr(755,root,root) %{javadir}/bin/exe/oldjavaw
%attr(755,root,root) %{javadir}/bin/exe/policytool
%attr(755,root,root) %{javadir}/bin/exe/rmid
%attr(755,root,root) %{javadir}/bin/exe/rmiregistry
%attr(755,root,root) %{javadir}/bin/exe/tnameserv

%dir %{javadir}/bin/classic
%{javadir}/bin/classic/Xusage.txt
%attr(755,root,root) %{javadir}/bin/classic/libjvm.so

%dir %{javadir}/lib
%{javadir}/lib/*

%config(noreplace) %verify(not size mtime md5) %{javacfgdir}/cp.*
%{javacfgdir}/links.*
%{javacfgdir}/jre.*
