Summary:	Tools for accessing and modifying guest disk images
Name:		guestfs-tools
Version:	1.50.1
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://download.libguestfs.org/guestfs-tools/1.50-stable/%{name}-%{version}.tar.gz
# Source0-md5:	85cf69607bf408b034bb953093a586c6
URL:		https://libguestfs.org/
BuildRequires:	bash-completion-devel >= 1:2.0
BuildRequires:	cdrkit-mkisofs
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-tools
BuildRequires:	jansson-devel >= 2.7
BuildRequires:	libguestfs-devel >= 1.49.8
BuildRequires:	libosinfo-devel
BuildRequires:	libvirt-devel >= 0.10.2
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	ncurses-devel
BuildRequires:	ocaml >= 4.04
BuildRequires:	ocaml-camlp4
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-gettext-devel
BuildRequires:	ocaml-libguestfs-devel
BuildRequires:	pcre2-8-devel
BuildRequires:	perl-Module-Build
BuildRequires:	perl-base
BuildRequires:	perl-hivex
BuildRequires:	perl-libintl
BuildRequires:	perl-modules
BuildRequires:	pkgconfig
BuildRequires:	po4a
BuildRequires:	rpm-build >= 4.6
BuildRequires:	xz
BuildRequires:	xz-devel
Requires:	jansson >= 2.7
Requires:	libguestfs >= 1.49.8
Requires:	libvirt >= 0.10.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guestfs-tools contains tools for accessing and modifying guest disk
images.

%package virt-win-reg
Summary:	Access and modify the Windows Registry of a Windows VM
BuildArch:	noarch

%description virt-win-reg
Virt-win-reg lets you look at and modify the Windows Registry of
Windows virtual machines.

%package -n bash-completion-guestfs-tools
Summary:	bash-completion for guestfs-tools
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-guestfs-tools
bash-completion for guestfs-tools.

%prep
%setup -q

%{__sed} -i -e '1s,.*env perl,#!%{__perl},' win-reg/virt-win-reg.in

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%dir %{_sysconfdir}/virt-builder
%dir %{_sysconfdir}/virt-builder/repos.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/virt-builder/repos.d/libguestfs.conf
%{_sysconfdir}/virt-builder/repos.d/libguestfs.gpg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/virt-builder/repos.d/opensuse.conf
%{_sysconfdir}/virt-builder/repos.d/opensuse.gpg
%attr(755,root,root) %{_bindir}/virt-alignment-scan
%attr(755,root,root) %{_bindir}/virt-builder
%attr(755,root,root) %{_bindir}/virt-builder-repository
%attr(755,root,root) %{_bindir}/virt-cat
%attr(755,root,root) %{_bindir}/virt-customize
%attr(755,root,root) %{_bindir}/virt-df
%attr(755,root,root) %{_bindir}/virt-dib
%attr(755,root,root) %{_bindir}/virt-diff
%attr(755,root,root) %{_bindir}/virt-drivers
%attr(755,root,root) %{_bindir}/virt-edit
%attr(755,root,root) %{_bindir}/virt-filesystems
%attr(755,root,root) %{_bindir}/virt-format
%attr(755,root,root) %{_bindir}/virt-get-kernel
%attr(755,root,root) %{_bindir}/virt-index-validate
%attr(755,root,root) %{_bindir}/virt-inspector
%attr(755,root,root) %{_bindir}/virt-log
%attr(755,root,root) %{_bindir}/virt-ls
%attr(755,root,root) %{_bindir}/virt-make-fs
%attr(755,root,root) %{_bindir}/virt-resize
%attr(755,root,root) %{_bindir}/virt-sparsify
%attr(755,root,root) %{_bindir}/virt-sysprep
%attr(755,root,root) %{_bindir}/virt-tail
%{_mandir}/man1/virt-alignment-scan.1*
%{_mandir}/man1/virt-builder-repository.1*
%{_mandir}/man1/virt-builder.1*
%{_mandir}/man1/virt-cat.1*
%{_mandir}/man1/virt-customize.1*
%{_mandir}/man1/virt-df.1*
%{_mandir}/man1/virt-dib.1*
%{_mandir}/man1/virt-diff.1*
%{_mandir}/man1/virt-drivers.1*
%{_mandir}/man1/virt-edit.1*
%{_mandir}/man1/virt-filesystems.1*
%{_mandir}/man1/virt-format.1*
%{_mandir}/man1/virt-get-kernel.1*
%{_mandir}/man1/virt-index-validate.1*
%{_mandir}/man1/virt-inspector.1*
%{_mandir}/man1/virt-log.1*
%{_mandir}/man1/virt-ls.1*
%{_mandir}/man1/virt-make-fs.1*
%{_mandir}/man1/virt-resize.1*
%{_mandir}/man1/virt-sparsify.1*
%{_mandir}/man1/virt-sysprep.1*
%{_mandir}/man1/virt-tail.1*
%lang(ja) %{_mandir}/ja/man1/virt-alignment-scan.1*
%lang(ja) %{_mandir}/ja/man1/virt-builder.1*
%lang(ja) %{_mandir}/ja/man1/virt-cat.1*
%lang(ja) %{_mandir}/ja/man1/virt-customize.1*
%lang(ja) %{_mandir}/ja/man1/virt-df.1*
%lang(ja) %{_mandir}/ja/man1/virt-dib.1*
%lang(ja) %{_mandir}/ja/man1/virt-diff.1*
%lang(ja) %{_mandir}/ja/man1/virt-edit.1*
%lang(ja) %{_mandir}/ja/man1/virt-filesystems.1*
%lang(ja) %{_mandir}/ja/man1/virt-format.1*
%lang(ja) %{_mandir}/ja/man1/virt-get-kernel.1*
%lang(ja) %{_mandir}/ja/man1/virt-index-validate.1*
%lang(ja) %{_mandir}/ja/man1/virt-inspector.1*
%lang(ja) %{_mandir}/ja/man1/virt-log.1*
%lang(ja) %{_mandir}/ja/man1/virt-ls.1*
%lang(ja) %{_mandir}/ja/man1/virt-make-fs.1*
%lang(ja) %{_mandir}/ja/man1/virt-resize.1*
%lang(ja) %{_mandir}/ja/man1/virt-sparsify.1*
%lang(ja) %{_mandir}/ja/man1/virt-sysprep.1*
%lang(uk) %{_mandir}/uk/man1/virt-alignment-scan.1*
%lang(uk) %{_mandir}/uk/man1/virt-builder.1*
%lang(uk) %{_mandir}/uk/man1/virt-cat.1*
%lang(uk) %{_mandir}/uk/man1/virt-customize.1*
%lang(uk) %{_mandir}/uk/man1/virt-df.1*
%lang(uk) %{_mandir}/uk/man1/virt-dib.1*
%lang(uk) %{_mandir}/uk/man1/virt-diff.1*
%lang(uk) %{_mandir}/uk/man1/virt-edit.1*
%lang(uk) %{_mandir}/uk/man1/virt-filesystems.1*
%lang(uk) %{_mandir}/uk/man1/virt-format.1*
%lang(uk) %{_mandir}/uk/man1/virt-get-kernel.1*
%lang(uk) %{_mandir}/uk/man1/virt-index-validate.1*
%lang(uk) %{_mandir}/uk/man1/virt-inspector.1*
%lang(uk) %{_mandir}/uk/man1/virt-log.1*
%lang(uk) %{_mandir}/uk/man1/virt-ls.1*
%lang(uk) %{_mandir}/uk/man1/virt-make-fs.1*
%lang(uk) %{_mandir}/uk/man1/virt-resize.1*
%lang(uk) %{_mandir}/uk/man1/virt-sparsify.1*
%lang(uk) %{_mandir}/uk/man1/virt-sysprep.1*

%files virt-win-reg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/virt-win-reg
%{_mandir}/man1/virt-win-reg.1*
%lang(ja) %{_mandir}/ja/man1/virt-win-reg.1*
%lang(uk) %{_mandir}/uk/man1/virt-win-reg.1*

%files -n bash-completion-guestfs-tools
%defattr(644,root,root,755)
%{bash_compdir}/virt-alignment-scan
%{bash_compdir}/virt-builder
%{bash_compdir}/virt-cat
%{bash_compdir}/virt-customize
%{bash_compdir}/virt-df
%{bash_compdir}/virt-dib
%{bash_compdir}/virt-diff
%{bash_compdir}/virt-drivers
%{bash_compdir}/virt-edit
%{bash_compdir}/virt-filesystems
%{bash_compdir}/virt-format
%{bash_compdir}/virt-get-kernel
%{bash_compdir}/virt-inspector
%{bash_compdir}/virt-log
%{bash_compdir}/virt-ls
%{bash_compdir}/virt-resize
%{bash_compdir}/virt-sparsify
%{bash_compdir}/virt-sysprep
%{bash_compdir}/virt-tail
%{bash_compdir}/virt-win-reg
