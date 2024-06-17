%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-cartographer-rviz
Version:        2.0.9003
Release:        3%{?dist}%{?release_suffix}
Summary:        ROS cartographer_rviz package

License:        Apache 2.0
URL:            https://github.com/cartographer-project/cartographer_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       abseil-cpp-devel
Requires:       boost-devel
Requires:       eigen3-devel
Requires:       ros-jazzy-cartographer
Requires:       ros-jazzy-cartographer-ros
Requires:       ros-jazzy-cartographer-ros-msgs
Requires:       ros-jazzy-pluginlib
Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-rviz-common
Requires:       ros-jazzy-rviz-ogre-vendor
Requires:       ros-jazzy-rviz-rendering
Requires:       ros-jazzy-ros-workspace
BuildRequires:  abseil-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-cartographer
BuildRequires:  ros-jazzy-cartographer-ros
BuildRequires:  ros-jazzy-cartographer-ros-msgs
BuildRequires:  ros-jazzy-pluginlib
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-rviz-common
BuildRequires:  ros-jazzy-rviz-ogre-vendor
BuildRequires:  ros-jazzy-rviz-rendering
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Cartographer is a system that provides real-time simultaneous localization and
mapping (SLAM) in 2D and 3D across multiple platforms and sensor configurations.
This package provides Cartographer's RViz integration.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Mon Jun 17 2024 Chris Lalancette <clalancette@openrobotics.org> - 2.0.9003-3
- Autogenerated by Bloom

* Thu Apr 18 2024 Chris Lalancette <clalancette@openrobotics.org> - 2.0.9003-2
- Autogenerated by Bloom

* Wed Apr 17 2024 Chris Lalancette <clalancette@openrobotics.org> - 2.0.9003-1
- Autogenerated by Bloom

* Fri Mar 15 2024 Chris Lalancette <clalancette@openrobotics.org> - 2.0.9002-1
- Autogenerated by Bloom

* Tue Mar 05 2024 Chris Lalancette <clalancette@openrobotics.org> - 2.0.9001-2
- Autogenerated by Bloom

