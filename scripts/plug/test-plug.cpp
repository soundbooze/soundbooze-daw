/* todo:
 *
 * amps setting
 * effects
 *
 * g++ test-plug.cpp -o test-plug `pkg-config --libs --cflags libusb-1.0` mustang.o
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

    memset(names, 0x00, 100 * 32);

    Mustang mustang;

    mustang.start_amp(names, name, &amplifier_set, effects_set);

    /*
    for (; i < 25; i++)
      printf("%s\n", names[i]);
    */

    int slot = 0;

    while (1) {

      mustang.load_memory_bank(i++, name, &amplifier_set, effects_set);
      if (i >= 25)
        i = 0;

      printf("[amp_num : %d ] [gain : %d] [volume : %d] [treble : %d] [middle : %d] [bass : %d] [cabinet : %d] [noise_gate : %d] [master_vol : %d] \n[gain2 : %d] [presence : %d] [threshold : %d] [depth : %d] [bias : %d] [sag : %d] [brightness : %d] [usb_gain : %d]\n\n", amplifier_set.amp_num, amplifier_set.gain, amplifier_set.volume, amplifier_set.treble, amplifier_set.middle, amplifier_set.bass, amplifier_set.cabinet, amplifier_set.noise_gate, amplifier_set.master_vol, amplifier_set.gain2, amplifier_set.presence, amplifier_set.threshold, amplifier_set.depth, amplifier_set.bias, amplifier_set.sag, amplifier_set.brightness, amplifier_set.usb_gain); 

      /*
      amplifier_set.gain += 10;
      amplifier_set.volume += 10;
      amplifier_set.master_vol += 10;

      mustang.set_amplifier(amplifier_set);
      */

      sleep(1);

    }

    mustang.stop_amp();

    return 0; 

} 
