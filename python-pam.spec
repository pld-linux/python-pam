#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python PAM module using ctypes
Summary(pl.UTF-8):	Moduł PAM dla Pythona wykorzystujący ctypes
Name:		python-pam
Version:	2.0.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/python-pam/
Source0:	https://files.pythonhosted.org/packages/source/p/python-pam/python-pam-%{version}.tar.gz
# Source0-md5:	1ee6201b3a696d3e022d67643547496c
Patch0:		%{name}-py2.patch
URL:		https://pypi.org/project/python-pam/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools >= 1:44
BuildRequires:	python-six
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.7
BuildRequires:	python3-setuptools >= 1:44
BuildRequires:	python3-six
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python pam module supporting py3 (and py2) for Linux type systems.

%description -l pl.UTF-8
Moduł pam dla Pythona obsługujący py3 (oraz py2) na systemach
linuksowych.

%package -n python3-pam
Summary:	Python PAM module using ctypes
Summary(pl.UTF-8):	Moduł PAM dla Pythona wykorzystujący ctypes
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.7

%description -n python3-pam
Python pam module supporting py3 (and py2) for Linux type systems.

%description -n python3-pam -l pl.UTF-8
Moduł pam dla Pythona obsługujący py3 (oraz py2) na systemach
linuksowych.

%prep
%setup -q
%patch -P 0 -p1

cat >setup.py <<EOF
from setuptools import setup
setup()
EOF

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/pam
%{py_sitescriptdir}/python_pam-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pam
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/pam
%{py3_sitescriptdir}/python_pam-%{version}-py*.egg-info
%endif
