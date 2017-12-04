Name:           ros-kinetic-pose-cov-ops
Version:        0.1.6
Release:        0%{?dist}
Summary:        ROS pose_cov_ops package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/pose_cov_ops
Source0:        %{name}-%{version}.tar.gz

Requires:       mrpt-devel
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-mrpt-bridge
Requires:       ros-kinetic-roscpp
BuildRequires:  mrpt-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-mrpt-bridge
BuildRequires:  ros-kinetic-roscpp

%description
Library with C++ functions for SE(2/3) pose and 2D/3D point composition
operations with uncertainty

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Dec 04 2017 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.6-0
- Autogenerated by Bloom

* Tue Dec 13 2016 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.5-0
- Autogenerated by Bloom

