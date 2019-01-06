alias acousticladspa='carla-single ladspa /usr/lib/ladspa/tap_tubewarmth.so & carla-single ladspa /usr/lib/ladspa/tap_dynamics_st.so &'
calfjackhost exciter ! eq5 ! vintagedelay ! reverb !
