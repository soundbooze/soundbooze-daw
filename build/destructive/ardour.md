## Destructive patches

### Audacity external launch - menu [patch]

```
gtk2_ardour/
- editor.h
- editor.cc
- editor_actions.cc

- editor_ops.cc

/* UDUK */

#include "ardour/session_directory.h"

...


void
Editor::audacity_region ()
{
	if (!_session) {
		return;
	}

	RegionSelection rs = get_regions_from_selection_and_entered ();

  gchar **dotsplit = g_strsplit ((const gchar *) rs.front()->region()->name().c_str(), ".", -1);

  gchar *audacity_cmdR = g_strdup_printf("%s \"%s/%s\%R.wav\"", "/usr/local/bin/audacity", _session->session_directory().sound_path().c_str(), dotsplit[0]);
  gchar *audacity_cmdL = g_strdup_printf("%s \"%s/%s\%%L.wav\"", "/usr/local/bin/audacity", _session->session_directory().sound_path().c_str(), dotsplit[0]);

  printf("%s\n", audacity_cmdR);
  printf("%s\n", audacity_cmdL);

  g_spawn_command_line_async (audacity_cmdR, NULL);
  g_spawn_command_line_async (audacity_cmdL, NULL);

  g_strfreev(dotsplit);
  g_free(audacity_cmdR);
  g_free(audacity_cmdL);

	if (rs.empty()) {
		return;
	}
}

```

- ardour.menus.in
  - RegionMenu
  - PopupRegionMenu
 
- ardour-sae.menus
- trx.menus.in
 
 <menuitem action='audacity-region'/>

## CSCOPE keywords

### AUDIO

- Rename...
- Reverse 

### MIDI

- midi_region_view.cc

- MidiRegionView::transpose 
- MidiRegionView::change_note_note 

...
