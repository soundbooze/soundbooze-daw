import os

LADSPA_TUBE = "carla-single ladspa /usr/lib/ladspa/tap_tubewarmth.so & carla-single ladspa /usr/lib/ladspa/tap_dynamics_st.so & carla-single ladspa /usr/lib/ladspa/stereo-plugins.so"
os.system(LADSPA_TUBE)
