%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define beta beta1
%endif

Name:            amsynth
Version:         1.3

%if %branch
Release:        %mkrel -c %beta 1
%else
Release:        %mkrel 1
%endif

Summary:        Virtual-analog polyphonic synthesizer for ALSA, OSS and JACK

%if %branch
Source:         http://%{name}.googlecode.com/files/amSynth-%{version}-beta1.tar.gz
%else
Source:         http://%{name}.googlecode.com/files/amSynth-%{version}.tar.gz
%endif
URL:            http://code.google.com/p/%{name}
License:        GPLv2
Group:          Sound
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  gtkmm2.4-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  jackit-devel
BuildRequires:  alsa-oss-devel
BuildRequires:  sndfile-devel

%description
AmSynth is a standalone polyphonic subtractive synthesizer. It supports
OSS, ALSA and JACK for Audio and MIDI I/O. Features are as follows.

o Dual oscillators with classic waveforms - sine / saw / square / noise
o 24 dB/oct low-pass resonant filter
o Independent ADSR envelopes for filter & amplitude
o LFO which can module the oscillators, filter, and amplitude
o Distortion effect
o Reverb

%prep
%if %branch
%setup -q -n amSynth-%{version}-%{beta}
%else
%setup -q -n amSynth-%{version}
%endif

%build
%configure2_5x --without-lash
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=AmSynth
Comment=Dual-Oscil sub synthesizer
Exec=%{_bindir}/amSynth
Icon=sound_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;
Encoding=UTF-8
EOF


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS
%{_bindir}/amSynth
%{_datadir}/amSynth
%{_datadir}/applications/mandriva-%{name}.desktop

