#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-DependencyCheck
Version  : 4.0.2
Release  : 3
URL      : https://repo1.maven.org/maven2/org/owasp/dependency-check-core/4.0.2/dependency-check-core-4.0.2.jar
Source0  : https://repo1.maven.org/maven2/org/owasp/dependency-check-core/4.0.2/dependency-check-core-4.0.2.jar
Source1  : https://repo1.maven.org/maven2/org/owasp/dependency-check-core/3.1.0/dependency-check-core-3.1.0.jar
Source2  : https://repo1.maven.org/maven2/org/owasp/dependency-check-core/3.1.0/dependency-check-core-3.1.0.pom
Source3  : https://repo1.maven.org/maven2/org/owasp/dependency-check-core/4.0.2/dependency-check-core-4.0.2.pom
Source4  : https://repo1.maven.org/maven2/org/owasp/dependency-check-gradle/3.1.0/dependency-check-gradle-3.1.0.jar
Source5  : https://repo1.maven.org/maven2/org/owasp/dependency-check-gradle/3.1.0/dependency-check-gradle-3.1.0.pom
Source6  : https://repo1.maven.org/maven2/org/owasp/dependency-check-parent/3.1.0/dependency-check-parent-3.1.0.pom
Source7  : https://repo1.maven.org/maven2/org/owasp/dependency-check-parent/4.0.2/dependency-check-parent-4.0.2.pom
Source8  : https://repo1.maven.org/maven2/org/owasp/dependency-check-utils/3.1.0/dependency-check-utils-3.1.0.jar
Source9  : https://repo1.maven.org/maven2/org/owasp/dependency-check-utils/3.1.0/dependency-check-utils-3.1.0.pom
Source10  : https://repo1.maven.org/maven2/org/owasp/dependency-check-utils/4.0.2/dependency-check-utils-4.0.2.jar
Source11  : https://repo1.maven.org/maven2/org/owasp/dependency-check-utils/4.0.2/dependency-check-utils-4.0.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: mvn-DependencyCheck-data = %{version}-%{release}
Requires: mvn-DependencyCheck-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
The H2 database engine (http://www.h2database.com/) is dual licensed and available under a modified version of the MPL 1.1 (Mozilla Public License) or under the (unmodified) EPL 1.0 (Eclipse Public License).
An original copy of the license agreement can be found at: http://www.h2database.com/html/license.html

%package data
Summary: data components for the mvn-DependencyCheck package.
Group: Data

%description data
data components for the mvn-DependencyCheck package.


%package license
Summary: license components for the mvn-DependencyCheck package.
Group: Default

%description license
license components for the mvn-DependencyCheck package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-DependencyCheck
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-DependencyCheck/LICENSE.txt
cp licenses/StupidTablePlugin/LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-DependencyCheck/licenses_StupidTablePlugin_LICENSE.txt
cp licenses/commons-compress/LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-DependencyCheck/licenses_commons-compress_LICENSE.txt
cp licenses/commons-io/LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-DependencyCheck/licenses_commons-io_LICENSE.txt
cp licenses/jquery/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-DependencyCheck/licenses_jquery_MIT-LICENSE.txt
cp licenses/jsoup/LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-DependencyCheck/licenses_jsoup_LICENSE.txt
cp licenses/lucene/LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-DependencyCheck/licenses_lucene_LICENSE.txt
cp licenses/velocity/LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-DependencyCheck/licenses_velocity_LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-core/4.0.2
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-core/4.0.2/dependency-check-core-4.0.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-core/3.1.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-core/3.1.0/dependency-check-core-3.1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-core/3.1.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-core/3.1.0/dependency-check-core-3.1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-core/4.0.2
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-core/4.0.2/dependency-check-core-4.0.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-gradle/3.1.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-gradle/3.1.0/dependency-check-gradle-3.1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-gradle/3.1.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-gradle/3.1.0/dependency-check-gradle-3.1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-parent/3.1.0
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-parent/3.1.0/dependency-check-parent-3.1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-parent/4.0.2
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-parent/4.0.2/dependency-check-parent-4.0.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-utils/3.1.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-utils/3.1.0/dependency-check-utils-3.1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-utils/3.1.0
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-utils/3.1.0/dependency-check-utils-3.1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-utils/4.0.2
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-utils/4.0.2/dependency-check-utils-4.0.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-utils/4.0.2
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/owasp/dependency-check-utils/4.0.2/dependency-check-utils-4.0.2.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/owasp/dependency-check-core/3.1.0/dependency-check-core-3.1.0.jar
/usr/share/java/.m2/repository/org/owasp/dependency-check-core/3.1.0/dependency-check-core-3.1.0.pom
/usr/share/java/.m2/repository/org/owasp/dependency-check-core/4.0.2/dependency-check-core-4.0.2.jar
/usr/share/java/.m2/repository/org/owasp/dependency-check-core/4.0.2/dependency-check-core-4.0.2.pom
/usr/share/java/.m2/repository/org/owasp/dependency-check-gradle/3.1.0/dependency-check-gradle-3.1.0.jar
/usr/share/java/.m2/repository/org/owasp/dependency-check-gradle/3.1.0/dependency-check-gradle-3.1.0.pom
/usr/share/java/.m2/repository/org/owasp/dependency-check-parent/3.1.0/dependency-check-parent-3.1.0.pom
/usr/share/java/.m2/repository/org/owasp/dependency-check-parent/4.0.2/dependency-check-parent-4.0.2.pom
/usr/share/java/.m2/repository/org/owasp/dependency-check-utils/3.1.0/dependency-check-utils-3.1.0.jar
/usr/share/java/.m2/repository/org/owasp/dependency-check-utils/3.1.0/dependency-check-utils-3.1.0.pom
/usr/share/java/.m2/repository/org/owasp/dependency-check-utils/4.0.2/dependency-check-utils-4.0.2.jar
/usr/share/java/.m2/repository/org/owasp/dependency-check-utils/4.0.2/dependency-check-utils-4.0.2.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-DependencyCheck/LICENSE.txt
/usr/share/package-licenses/mvn-DependencyCheck/licenses_StupidTablePlugin_LICENSE.txt
/usr/share/package-licenses/mvn-DependencyCheck/licenses_commons-compress_LICENSE.txt
/usr/share/package-licenses/mvn-DependencyCheck/licenses_commons-io_LICENSE.txt
/usr/share/package-licenses/mvn-DependencyCheck/licenses_jquery_MIT-LICENSE.txt
/usr/share/package-licenses/mvn-DependencyCheck/licenses_jsoup_LICENSE.txt
/usr/share/package-licenses/mvn-DependencyCheck/licenses_lucene_LICENSE.txt
/usr/share/package-licenses/mvn-DependencyCheck/licenses_velocity_LICENSE.txt
