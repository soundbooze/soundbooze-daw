export LESSHISTFILE=/dev/null
export HISTFILE=/dev/null

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

alias dir='dir --color'
alias ls='ls -lh --color --group-directories-first'
alias ll='ls'
alias df='df -h'
alias blk='lsblk'
alias free='free -m'
alias uname='uname -ap'

alias vim='vim -i NONE'
alias sysinfo='procinfo && iostat && vmstat && mpstat -P ALL && pidstat'

alias set-sink="pacmd set-default-sink "
alias set-source="pacmd set-default-source "

alias cards='cat /proc/asound/cards'
alias list-sinks="pacmd list-sinks | grep -e 'name:' -e 'index:'"
alias list-sources="pacmd list-sources | grep -e 'index:' -e device.string -e 'name:'"
alias audio='cards && list-sinks && list-sources'
alias drum='aplaymidi -p 14:0'
alias synth='aplaymidi -p 130:0'

alias youtube='youtube-dl -x --audio-format wav'
#alias explorer='wine ~/.wine/drive_c/windows/explorer.exe'

alias p='python3 -W ignore'

alias redzeppelin='jalv http://gareus.org/oss/lv2/avldrums#RedZeppelinMulti'
alias blackpearl='jalv http://gareus.org/oss/lv2/avldrums#BlackPearlMulti'

alias clone='git clone'
alias cache="git config --global credential.helper 'cache --timeout=14400'"
alias clearcache="git credential-cache exit"
alias commit='git commit -m 'Updated' -a'
alias push='git push'
alias pull='git pull'

alias psaudio="ps axu|egrep 'jack|pulse'"
alias calfdrumstack='calfjackhost multibandcompressor ! multibandlimiter ! eq8 ! reverb !'
alias calfusb='calfjackhost flanger ! saturator ! crusher ! vintagedelay ! eq5 !'
alias calfmin='calfjackhost flanger ! saturator ! crusher ! eq5 ! vintagedelay !'
alias acousticladspa='carla-single ladspa /usr/lib/ladspa/tap_tubewarmth.so & carla-single ladspa /usr/lib/ladspa/tap_dynamics_st.so & carla-single ladspa /usr/lib/ladspa/stereo-plugins.so &'
#alias record='jack_capture -d 60 -p system:capture* -f wav out.wav'
#alias record='jack_capture -d 60 -p system:playback* -f wav out.wav'
alias record='jack_capture -p system:playback* -f wav out.wav'
#alias record='jack_capture -d 60 -p "Calf Studio Gear:Equalizer*" -f wav out.wav'
#alias record='jack_capture -d 60 -p "Calf Studio Gear:Vintage*" -f wav out.wav'
alias carla-single='CARLA_BRIDGE_PLUGIN_BINARY_TYPE=win64 /usr/local/bin/carla-single vst '

alias x='startx'
alias reposition='~/soundbooze-mame/reposition.sh'

export PYTHONDONTWRITEBYTECODE=1

alias pyhttp='cd /var/www/html && python -m SimpleHTTPServer'
alias installtensorflow='npm -y init && npm install @tensorflow/tfjs-node'

export CSCOPE_EDITOR=`which gvim`
alias ctags='ctags -R *'
alias initCscope="echo find . -name "*.c" -o -name "*.h" > cscope.files"
alias buildCscope="cscope -q -R -b -i cscope.files"

alias explorer='wine ~/.wine/drive_c/windows/explorer.exe &'

if [ -f `which powerline-daemon` ]; then
  powerline-daemon -q
  POWERLINE_BASH_CONTINUATION=1
  POWERLINE_BASH_SELECT=1
  . /usr/share/powerline/bindings/bash/powerline.sh
fi

export PATH=$PATH:/opt/node-v10.15.2-linux-x64/bin/
