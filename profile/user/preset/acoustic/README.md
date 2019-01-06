```

guitarix OSEM

alias acousticladspa='carla-single ladspa /usr/lib/ladspa/tap_tubewarmth.so & carla-single ladspa /usr/lib/ladspa/tap_dynamics_st.so & carla-single ladspa /usr/lib/ladspa/stereo-plugins.so &'

+ calf multiband enhancer
+ rakarrack nostalgia

misc direct
calfjackhost exciter ! eq5 ! vintagedelay ! reverb !
calfjackhost eq5 ! vintagedelay ! multibandenhancer !

```
