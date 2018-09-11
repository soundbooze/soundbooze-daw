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
main(int argc, char *argv[]) { 

    struct amp_settings amplifier_set;
    struct fx_pedal_settings effects_set[4];
    char names[100][32];
    char name[32];

    short int i = 0;

    amps ampStart = FENDER_57_DELUXE;
    amps ampEnd = METAL_2000;

    memset(names, 0x00, 100*32);

    Mustang mustang;

    mustang.start_amp(names, name, &amplifier_set, effects_set);

    /*
    for (; i < 25; i++)
      printf("%s\n", names[i]);
    */

    printf ("%d %d %d %d %d %d\n", amplifier_set.gain, amplifier_set.volume, 
                                   amplifier_set.treble, amplifier_set.middle, 
                                   amplifier_set.bass, amplifier_set.master_vol);

    int slot = 0;

    //for (i = 0; i < 25; i++) {
    while (1) {
      /*
      mustang.load_memory_bank(i++, name, &amplifier_set, effects_set);
      if (i >= 25)
        i = 0;
        */

      printf ("%d %d %d %d %d %d\n", amplifier_set.gain, amplifier_set.volume, 
                   amplifier_set.treble, amplifier_set.middle, 
                   amplifier_set.bass, amplifier_set.master_vol);

      amplifier_set.gain += 10;
      amplifier_set.volume += 10;
      amplifier_set.master_vol += 10;

      mustang.set_amplifier(amplifier_set);

      sleep(2);
    }

    mustang.stop_amp();

    return 0; 

} 
