/* todo:
 *
 * amps setting
 * effects
 *
 * 2s sample
 *
 */

#include "mustang.h"

int 
main() { 

    struct amp_settings amplifier_set;
    struct fx_pedal_settings effects_set[4];
    char names[100][32];
    char name[32];

    short int i = 0;

    memset(names, 0x00, 100*32);

    Mustang mustang;

    mustang.start_amp(names, name, &amplifier_set, effects_set);

    /*
    for (; i < 25; i++)
      printf("%s\n", names[i]);
    */

    int slot = 0;
    //for (i = 0; i < 25; i++) {
    while (1) {
      mustang.load_memory_bank(i++, name, &amplifier_set, effects_set);
      if (i >= 25)
        i = 0;
      sleep(1);
    }

    mustang.stop_amp();

    return 0; 

} 
