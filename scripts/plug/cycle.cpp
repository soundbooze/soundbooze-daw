/* helper:
 *
 * g++ cycle.cpp -o cycle `pkg-config --libs --cflags libusb-1.0` mustang.o
 * 
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

    cabinets cabStart = OFF;
    cabinets cabEnd = cabSS112;
    int s = OFF;

    memset(names, 0x00, 100 * 32);

    Mustang mustang;

    mustang.start_amp(names, name, &amplifier_set, effects_set);

    int slot = 0;

    while (1) {

      mustang.load_memory_bank(i++, name, &amplifier_set, effects_set);
      if (i >= 25)
        i = 0;

      sleep(2);

    }

    mustang.stop_amp();

    return 0; 

} 
